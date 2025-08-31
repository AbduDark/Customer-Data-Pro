#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUI components for Egyptian Carriers Customer Management System
Enhanced Tkinter version with exact design from image
"""

import tkinter as tk
from tkinter import ttk

class CustomerTableGUI:
    def __init__(self, parent, font, customer_manager):
        self.parent = parent
        self.font = font
        self.customer_manager = customer_manager
        self.selected_customer = None
        
        # Colors exactly matching the provided image
        self.colors = {
            'header_bg': '#4F81BD',        # Blue header
            'orange_bg': '#FFC000',        # Orange carrier - bright orange
            'vodafone_bg': '#FF0000',      # Red/Vodafone - bright red
            'etisalat_bg': '#00B050',      # Green/Etisalat - bright green  
            'we_bg': '#7030A0',            # Purple/WE - deep purple
            'alt_row': '#F2F2F2',          # Light gray alternate rows
            'white_row': '#FFFFFF',        # White rows
            'selected': '#D4EDDA',         # Selected row color
            'text_dark': '#000000',        # Black text
            'text_light': '#FFFFFF',       # White text
            'border': '#000000'            # Black borders
        }
        
        self.setup_table()
    
    def setup_table(self):
        """Setup the customer table with scrollbars"""
        # Main frame
        self.frame = tk.Frame(self.parent, bg='white')
        
        # Create canvas and scrollbars for the table
        self.canvas = tk.Canvas(self.frame, bg='white', highlightthickness=0)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        h_scrollbar = ttk.Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        
        # Configure canvas
        self.canvas.configure(
            yscrollcommand=v_scrollbar.set,
            xscrollcommand=h_scrollbar.set
        )
        
        # Scrollable frame inside canvas
        self.scrollable_frame = tk.Frame(self.canvas, bg='white')
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Add scrollable frame to canvas
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Grid layout
        self.canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        # Configure grid weights
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        # Bind canvas resize
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
        # Mouse wheel scrolling
        self.bind_mousewheel()
        
        # Initialize with empty data
        self.update_data([])
    
    def on_canvas_configure(self, event):
        """Handle canvas resize"""
        # Update scroll region
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        # Resize the frame to fill canvas width
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)
    
    def bind_mousewheel(self):
        """Bind mouse wheel to canvas scrolling"""
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
        def _bind_to_mousewheel(event):
            self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def _unbind_from_mousewheel(event):
            self.canvas.unbind_all("<MouseWheel>")
        
        self.canvas.bind('<Enter>', _bind_to_mousewheel)
        self.canvas.bind('<Leave>', _unbind_from_mousewheel)
    
    def update_data(self, customers_data):
        """Update table with customer data matching the image design"""
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        if not customers_data:
            # Show empty state
            empty_label = tk.Label(
                self.scrollable_frame,
                text="لا توجد بيانات عملاء",
                font=self.font,
                bg='white',
                fg=self.colors['text_dark']
            )
            empty_label.pack(pady=50)
            return
        
        # Create main table container
        table_container = tk.Frame(self.scrollable_frame, bg='white')
        table_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create table header exactly like the image
        self.create_table_header(table_container)
        
        # Create customer rows
        for i, customer in enumerate(customers_data):
            self.create_customer_rows(table_container, customer, i)
    
    def create_table_header(self, parent):
        """Create the exact colored table header from the image"""
        header_frame = tk.Frame(parent, bg='white')
        header_frame.pack(fill=tk.X, pady=(0, 2))
        
        # Configure grid columns
        for i in range(7):
            header_frame.grid_columnconfigure(i, weight=1, minsize=150)
        
        # Customer name header
        name_header = tk.Label(
            header_frame,
            text="اسم العميل",
            font=(self.font[0], self.font[1], 'bold'),
            bg=self.colors['header_bg'],
            fg=self.colors['text_light'],
            relief=tk.SOLID,
            borderwidth=1,
            height=2
        )
        name_header.grid(row=0, column=0, sticky='nsew', padx=1, pady=1)
        
        # National ID header
        id_header = tk.Label(
            header_frame,
            text="الرقم القومي",
            font=(self.font[0], self.font[1], 'bold'),
            bg=self.colors['header_bg'],
            fg=self.colors['text_light'],
            relief=tk.SOLID,
            borderwidth=1,
            height=2
        )
        id_header.grid(row=0, column=1, sticky='nsew', padx=1, pady=1)
        
        # Orange header
        orange_header = tk.Label(
            header_frame,
            text="اورانج",
            font=(self.font[0], self.font[1], 'bold'),
            bg=self.colors['orange_bg'],
            fg=self.colors['text_dark'],
            relief=tk.SOLID,
            borderwidth=1,
            height=2
        )
        orange_header.grid(row=0, column=2, sticky='nsew', padx=1, pady=1)
        
        # Vodafone header
        vodafone_header = tk.Label(
            header_frame,
            text="فودافون",
            font=(self.font[0], self.font[1], 'bold'),
            bg=self.colors['vodafone_bg'],
            fg=self.colors['text_light'],
            relief=tk.SOLID,
            borderwidth=1,
            height=2
        )
        vodafone_header.grid(row=0, column=3, sticky='nsew', padx=1, pady=1)
        
        # Etisalat header
        etisalat_header = tk.Label(
            header_frame,
            text="اتصالات",
            font=(self.font[0], self.font[1], 'bold'),
            bg=self.colors['etisalat_bg'],
            fg=self.colors['text_light'],
            relief=tk.SOLID,
            borderwidth=1,
            height=2
        )
        etisalat_header.grid(row=0, column=4, sticky='nsew', padx=1, pady=1)
        
        # WE header
        we_header = tk.Label(
            header_frame,
            text="وي",
            font=(self.font[0], self.font[1], 'bold'),
            bg=self.colors['we_bg'],
            fg=self.colors['text_light'],
            relief=tk.SOLID,
            borderwidth=1,
            height=2
        )
        we_header.grid(row=0, column=5, sticky='nsew', padx=1, pady=1)
        
        # Notes header
        notes_header = tk.Label(
            header_frame,
            text="ملاحظات",
            font=(self.font[0], self.font[1], 'bold'),
            bg=self.colors['header_bg'],
            fg=self.colors['text_light'],
            relief=tk.SOLID,
            borderwidth=1,
            height=2
        )
        notes_header.grid(row=0, column=6, sticky='nsew', padx=1, pady=1)
    
    def create_customer_rows(self, parent, customer, customer_index):
        """Create rows for a customer exactly like the image"""
        # Customer separator with colored header (blue bar between customers)
        if customer_index > 0:
            separator = tk.Frame(parent, bg=self.colors['header_bg'], height=3)
            separator.pack(fill=tk.X, pady=2)
        
        # Get all phone numbers for each carrier
        orange_phones = customer['carriers']['اورانج']
        vodafone_phones = customer['carriers']['فودافون']
        etisalat_phones = customer['carriers']['اتصالات']
        we_phones = customer['carriers']['وي']
        
        # Calculate maximum rows needed
        max_rows = max(
            len(orange_phones),
            len(vodafone_phones), 
            len(etisalat_phones),
            len(we_phones),
            1  # At least one row
        )
        
        # Create customer row container
        customer_frame = tk.Frame(parent, bg='white')
        customer_frame.pack(fill=tk.X, pady=1)
        
        # Create rows for this customer
        for row_index in range(max_rows):
            row_frame = tk.Frame(customer_frame, bg='white')
            row_frame.pack(fill=tk.X, pady=1)
            
            # حفظ فهرس العميل في الصف للتمييز
            row_frame.customer_index = customer_index
            
            # Configure grid columns
            for i in range(7):
                row_frame.grid_columnconfigure(i, weight=1, minsize=150)
            
            # Row background color alternating
            row_bg = self.colors['white_row'] if customer_index % 2 == 0 else self.colors['alt_row']
            
            # Customer name (only in first row)
            if row_index == 0:
                name_cell = tk.Label(
                    row_frame,
                    text=customer['name'],
                    font=self.font,
                    bg=row_bg,
                    fg=self.colors['text_dark'],
                    relief=tk.SOLID,
                    borderwidth=1,
                    height=3,
                    anchor='center'
                )
            else:
                name_cell = tk.Label(
                    row_frame,
                    text="",
                    bg=row_bg,
                    relief=tk.SOLID,
                    borderwidth=1,
                    height=3
                )
            name_cell.grid(row=0, column=0, sticky='nsew', padx=1, pady=1)
            
            # National ID (only in first row)
            if row_index == 0:
                id_cell = tk.Label(
                    row_frame,
                    text=customer['national_id'],
                    font=self.font,
                    bg=row_bg,
                    fg=self.colors['text_dark'],
                    relief=tk.SOLID,
                    borderwidth=1,
                    height=3,
                    anchor='center'
                )
            else:
                id_cell = tk.Label(
                    row_frame,
                    text="",
                    bg=row_bg,
                    relief=tk.SOLID,
                    borderwidth=1,
                    height=3
                )
            id_cell.grid(row=0, column=1, sticky='nsew', padx=1, pady=1)
            
            # Carrier columns with exact colors from image
            carriers_info = [
                (orange_phones, self.colors['orange_bg'], self.colors['text_dark'], 2, "اورانج"),
                (vodafone_phones, self.colors['vodafone_bg'], self.colors['text_light'], 3, "فودافون"),
                (etisalat_phones, self.colors['etisalat_bg'], self.colors['text_light'], 4, "اتصالات"),
                (we_phones, self.colors['we_bg'], self.colors['text_light'], 5, "وي")
            ]
            
            for phones, bg_color, text_color, col, carrier_name in carriers_info:
                self.create_carrier_cell(
                    row_frame, row_index, phones, bg_color, text_color, col, carrier_name
                )
            
            # Notes column (only in first row)
            if row_index == 0:
                # Truncate notes if too long
                notes_text = customer.get('notes', '')
                if len(notes_text) > 30:
                    notes_text = notes_text[:30] + '...'
                
                notes_cell = tk.Label(
                    row_frame,
                    text=notes_text,
                    font=self.font,
                    bg=row_bg,
                    fg=self.colors['text_dark'],
                    relief=tk.SOLID,
                    borderwidth=1,
                    height=3,
                    anchor='center',
                    wraplength=120
                )
            else:
                notes_cell = tk.Label(
                    row_frame,
                    text="",
                    bg=row_bg,
                    relief=tk.SOLID,
                    borderwidth=1,
                    height=3
                )
            notes_cell.grid(row=0, column=6, sticky='nsew', padx=1, pady=1)
            
            # Make row clickable
            self.make_row_clickable(row_frame, customer)
    
    def create_carrier_cell(self, parent, row_index, phones, bg_color, text_color, column, carrier_name):
        """Create a carrier cell with phone number, notes and checkbox"""
        if row_index < len(phones):
            # Phone exists for this row
            phone_data = phones[row_index]
            
            # Create cell frame with carrier background color
            cell_frame = tk.Frame(parent, bg=bg_color, relief=tk.SOLID, borderwidth=1)
            cell_frame.grid(row=0, column=column, sticky='nsew', padx=1, pady=1)
            
            # Phone number label
            phone_label = tk.Label(
                cell_frame,
                text=phone_data['phone_number'],
                font=(self.font[0], self.font[1], 'bold'),
                bg=bg_color,
                fg=text_color,
                anchor='center'
            )
            phone_label.pack(pady=(2, 0))
            
            # Always show notes area (even if empty) to maintain consistent layout
            notes_text = ""
            if phone_data.get('notes') and phone_data['notes'].strip():
                notes_text = phone_data['notes']
                # Truncate long notes
                if len(notes_text) > 12:
                    notes_text = notes_text[:12] + '...'
                notes_text = f"📝 {notes_text}"
            
            notes_label = tk.Label(
                cell_frame,
                text=notes_text,
                font=(self.font[0], self.font[1]-3),
                bg=bg_color,
                fg=text_color,
                anchor='center',
                wraplength=120,
                height=1
            )
            notes_label.pack(pady=(1, 1))
            
            # Wallet checkbox
            wallet_var = tk.BooleanVar(value=phone_data['has_wallet'])
            wallet_check = tk.Checkbutton(
                cell_frame,
                text="💰",
                variable=wallet_var,
                bg=bg_color,
                fg=text_color,
                selectcolor=bg_color,
                font=(self.font[0], self.font[1]-2),
                activebackground=bg_color,
                activeforeground=text_color,
                command=lambda pId=phone_data['phone_id'], var=wallet_var: 
                    self.on_wallet_change(pId, var.get())
            )
            wallet_check.pack(pady=(0, 2))
            
            # Store reference to original colors for selection handling
            setattr(cell_frame, 'original_bg', bg_color)
            setattr(phone_label, 'original_bg', bg_color)
            setattr(phone_label, 'original_fg', text_color)
            setattr(notes_label, 'original_bg', bg_color)
            setattr(notes_label, 'original_fg', text_color)
            setattr(wallet_check, 'original_bg', bg_color)
            
        else:
            # Empty cell with carrier background color
            empty_cell = tk.Label(
                parent,
                text="",
                bg=bg_color,
                relief=tk.SOLID,
                borderwidth=1,
                height=3
            )
            empty_cell.grid(row=0, column=column, sticky='nsew', padx=1, pady=1)
            
            # Store reference to original color
            setattr(empty_cell, 'original_bg', bg_color)
    
    def make_row_clickable(self, row_frame, customer):
        """Make a row clickable for selection"""
        def on_click(event):
            self.selected_customer = customer
            self.highlight_selected_row(row_frame)
            # إشعار التطبيق الرئيسي بالتحديد
            if hasattr(self, 'selection_callback') and self.selection_callback:
                self.selection_callback(customer)
        
        row_frame.bind("<Button-1>", on_click)
        for child in row_frame.winfo_children():
            child.bind("<Button-1>", on_click)
            try:
                for grandchild in child.winfo_children():
                    grandchild.bind("<Button-1>", on_click)
            except:
                pass
    
    def highlight_selected_row(self, selected_frame):
        """Highlight the selected row"""
        # إزالة التمييز من جميع الصفوف
        self.clear_all_highlights()
        
        # تمييز الصف المحدد
        self.highlight_row_recursive(selected_frame, self.colors['selected'])
        
        # حفظ مرجع للصف المحدد
        self.selected_row_frame = selected_frame
    
    def clear_all_highlights(self):
        """Clear highlights from all rows"""
        if hasattr(self, 'selected_row_frame') and self.selected_row_frame:
            try:
                # إعادة تعيين لون الصف السابق
                customer_index = getattr(self.selected_row_frame, 'customer_index', 0)
                original_bg = self.colors['white_row'] if customer_index % 2 == 0 else self.colors['alt_row']
                self.restore_original_colors(self.selected_row_frame, original_bg)
            except:
                pass
    
    def restore_original_colors(self, widget, default_bg):
        """Restore original colors for widget and its children"""
        try:
            # قائمة ألوان الشبكات
            carrier_colors = [self.colors['orange_bg'], self.colors['vodafone_bg'], 
                            self.colors['etisalat_bg'], self.colors['we_bg'], 
                            self.colors['header_bg']]
            
            # استعادة اللون الأصلي للعنصر
            if hasattr(widget, 'configure') and 'bg' in widget.keys():
                if hasattr(widget, 'original_bg'):
                    # استعادة اللون الأصلي المحفوظ
                    widget.configure(bg=widget.original_bg)
                    # استعادة لون النص الأصلي أيضاً إذا كان محفوظاً
                    if hasattr(widget, 'original_fg') and 'fg' in widget.keys():
                        widget.configure(fg=widget.original_fg)
                else:
                    current_bg = widget.cget('bg')
                    # إعادة تعيين اللون الافتراضي فقط إذا لم يكن من ألوان الشبكات
                    if current_bg not in carrier_colors:
                        widget.configure(bg=default_bg)
            
            # تطبيق الاستعادة على العناصر الفرعية
            for child in widget.winfo_children():
                self.restore_original_colors(child, default_bg)
        except:
            pass
    
    def highlight_row_recursive(self, widget, color):
        """Recursively highlight a row and its children"""
        try:
            # قائمة ألوان الشبكات التي لا يجب تغييرها
            carrier_colors = [self.colors['orange_bg'], self.colors['vodafone_bg'], 
                            self.colors['etisalat_bg'], self.colors['we_bg'], 
                            self.colors['header_bg']]
            
            # تغيير لون الخلفية للعنصر نفسه إذا كان يدعم ذلك
            if hasattr(widget, 'configure') and 'bg' in widget.keys():
                current_bg = widget.cget('bg')
                
                # فحص إذا كان العنصر يحتوي على لون أصلي محفوظ
                if hasattr(widget, 'original_bg'):
                    # لا تغير لون خلايا الشبكات
                    if widget.original_bg in carrier_colors:
                        pass  # احتفظ باللون الأصلي للشبكة
                    else:
                        widget.configure(bg=color)
                else:
                    # تغيير اللون فقط إذا لم يكن من ألوان الشبكات
                    if current_bg not in carrier_colors:
                        widget.configure(bg=color)
            
            # تطبيق التمييز على العناصر الفرعية
            for child in widget.winfo_children():
                self.highlight_row_recursive(child, color)
        except:
            pass
    
    def set_selection_callback(self, callback):
        """Set callback function for selection events"""
        self.selection_callback = callback
    
    def on_wallet_change(self, phone_id, has_wallet):
        """Handle wallet status change"""
        try:
            # Update wallet status in database
            self.customer_manager.update_phone_number_wallet_status(phone_id, has_wallet)
        except Exception as e:
            print(f"Error updating wallet status: {e}")
    
    def get_selected_customer(self):
        """Get the currently selected customer"""
        return self.selected_customer
    
    def refresh(self):
        """Refresh the table display"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class SearchWidget:
    def __init__(self, parent, font, search_callback):
        self.parent = parent
        self.font = font
        self.search_callback = search_callback
        
        self.setup_search()
    
    def setup_search(self):
        """Setup search widget"""
        self.frame = tk.Frame(self.parent, bg='#f8f9fa')
        
        # Search label
        search_label = tk.Label(
            self.frame,
            text="البحث:",
            font=self.font,
            bg='#f8f9fa',
            fg='#495057'
        )
        search_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Search entry
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            self.frame,
            textvariable=self.search_var,
            font=self.font,
            width=30,
            bd=2,
            relief=tk.GROOVE
        )
        self.search_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        # Search button
        search_btn = tk.Button(
            self.frame,
            text="بحث",
            command=self.perform_search,
            font=(self.font[0], self.font[1], 'bold'),
            bg='#007bff',
            fg='white',
            bd=0,
            padx=20,
            pady=5
        )
        search_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        clear_btn = tk.Button(
            self.frame,
            text="مسح",
            command=self.clear_search,
            font=(self.font[0], self.font[1], 'bold'),
            bg='#6c757d',
            fg='white',
            bd=0,
            padx=20,
            pady=5
        )
        clear_btn.pack(side=tk.LEFT)
        
        # Bind Enter key
        self.search_entry.bind('<Return>', lambda e: self.perform_search())
    
    def perform_search(self):
        """Perform search"""
        search_term = self.search_var.get().strip()
        self.search_callback(search_term)
    
    def clear_search(self):
        """Clear search"""
        self.search_var.set("")
        self.search_callback("")

class StatusBar:
    def __init__(self, parent, font):
        self.parent = parent
        self.font = font
        
        self.setup_status_bar()
    
    def setup_status_bar(self):
        """Setup status bar"""
        self.frame = tk.Frame(self.parent, bg='#e9ecef', relief=tk.SUNKEN, bd=1)
        
        # Status label
        self.status_var = tk.StringVar(value="جاهز")
        self.status_label = tk.Label(
            self.frame,
            textvariable=self.status_var,
            font=self.font,
            bg='#e9ecef',
            fg='#495057',
            anchor='w'
        )
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)
        
        # Statistics labels
        self.stats_var = tk.StringVar(value="")
        self.stats_label = tk.Label(
            self.frame,
            textvariable=self.stats_var,
            font=self.font,
            bg='#e9ecef',
            fg='#495057'
        )
        self.stats_label.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def set_status(self, status):
        """Set status message"""
        self.status_var.set(status)
    
    def set_stats(self, stats):
        """Set statistics"""
        self.stats_var.set(stats)