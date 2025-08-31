import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import time

def list_com_ports():
    """عرض جميع الـ COM Ports المتاحة"""
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

def connect_to_modem(port, baudrate=115200):
    """الاتصال بالمودم"""
    try:
        modem = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # ندي وقت للمودم يتجهز
        return modem
    except Exception as e:
        messagebox.showerror("خطأ", f"فشل الاتصال بالمودم: {e}")
        return None

def send_at_command(modem, command):
    """إرسال أوامر AT وقراءة الرد"""
    modem.write((command + "\r").encode())
    time.sleep(1)
    response = modem.readlines()
    return [line.decode(errors="ignore").strip() for line in response]

def refresh_ports():
    ports = list_com_ports()
    port_menu['values'] = ports
    if ports:
        port_menu.current(0)

def connect():
    port = port_var.get()
    if not port:
        messagebox.showwarning("تنبيه", "من فضلك اختر COM Port")
        return

    modem = connect_to_modem(port)
    if modem:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"📡 متصل بالمودم: {port}\n\n")

        # قراءة الرقم
        output_text.insert(tk.END, "📞 محاولة قراءة رقم الخط...\n")
        response = send_at_command(modem, "AT+CNUM")
        output_text.insert(tk.END, "\n".join(response) + "\n\n")

        # قراءة ICCID
        output_text.insert(tk.END, "💳 محاولة قراءة ICCID...\n")
        response = send_at_command(modem, "AT+CCID")
        output_text.insert(tk.END, "\n".join(response) + "\n")

        modem.close()

# ==============================
# واجهة المستخدم
# ==============================

root = tk.Tk()
root.title("SIM Reader - Orange")
root.geometry("500x400")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# اختيار الـ COM Port
ttk.Label(frame, text="اختر المنفذ (COM Port):").pack(anchor="w")
port_var = tk.StringVar()
port_menu = ttk.Combobox(frame, textvariable=port_var, width=30)
port_menu.pack(fill="x", pady=5)

btn_refresh = ttk.Button(frame, text="🔄 تحديث المنافذ", command=refresh_ports)
btn_refresh.pack(pady=5)

btn_connect = ttk.Button(frame, text="✅ اتصال", command=connect)
btn_connect.pack(pady=5)

# صندوق النتائج
output_text = tk.Text(frame, height=15, wrap="word")
output_text.pack(fill="both", expand=True, pady=10)

# تحديث المنافذ عند بدء التشغيل
refresh_ports()

root.mainloop()
