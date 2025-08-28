
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Egyptian Telecom Customer Management System Launcher
Production-ready version with modern UI enhancements
"""

import sys
import os
import traceback
import tkinter as tk
from tkinter import messagebox

def check_dependencies():
    """Check if all required dependencies are available"""
    missing_modules = []
    
    try:
        import sqlite3
    except ImportError:
        missing_modules.append("sqlite3")
    
    try:
        from tkinter import ttk
    except ImportError:
        missing_modules.append("tkinter")
        
    try:
        from PIL import Image, ImageTk
    except ImportError:
        print("تحذير: مكتبة PIL غير متوفرة - بعض ميزات الصور قد لا تعمل")
