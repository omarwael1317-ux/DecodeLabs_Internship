import tkinter as tk

def calculate_entropy_and_update(*args):
    password = password_entry.get()
    length = len(password)
    
    length_valid = length >= 8
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)
    
    lbl_cond_len.config(fg="#00ffcc" if length_valid else "#555566", text="✔ Min 8 Characters" if length_valid else "○ Min 8 Characters")
    lbl_cond_upper.config(fg="#00ffcc" if has_upper else "#555566", text="✔ Uppercase [A-Z]" if has_upper else "○ Uppercase [A-Z]")
    lbl_cond_digit.config(fg="#00ffcc" if has_digit else "#555566", text="✔ Number [0-9]" if has_digit else "○ Number [0-9]")
    lbl_cond_symbol.config(fg="#00ffcc" if has_symbol else "#555566", text="✔ Special Symbol" if has_symbol else "○ Special Symbol")
    
    if length == 0:
        canvas.itemconfig(arc, outline="#1f1f2e", extent=0)
        status_label.config(text="SYSTEM IDLE", fg="#888899")
        entropy_label.config(text="0%", fg="#888899")
        return
        
    if not length_valid:
        score = 1
    else:
        score = 1 + sum([has_upper, has_digit, has_symbol])
        
    if score == 1:
        canvas.itemconfig(arc, outline="#ff0055", extent=-90)
        status_label.config(text="CRITICAL RISK ◆ WEAK", fg="#ff0055")
        entropy_label.config(text=f"{min(25, length * 3)}%", fg="#ff0055")
    elif score == 2:
        canvas.itemconfig(arc, outline="#ffcc00", extent=-180)
        status_label.config(text="VULNERABLE ◆ LOW", fg="#ffcc00")
        entropy_label.config(text="45%", fg="#ffcc00")
    elif score == 3:
        canvas.itemconfig(arc, outline="#9900ff", extent=-270)
        status_label.config(text="SECURED ◆ MEDIUM", fg="#9900ff")
        entropy_label.config(text="75%", fg="#9900ff")
    elif score == 4:
        canvas.itemconfig(arc, outline="#00ffcc", extent=-359.9)
        status_label.config(text="ENCRYPTED ◆ STRONG", fg="#00ffcc")
        entropy_label.config(text="100%", fg="#00ffcc")

root = tk.Tk()
root.title("PASSWORD ANALYZER")
root.geometry("420x660") 
root.configure(bg="#0d0d13")
root.resizable(False, False)

# Header Section
header_frame = tk.Frame(root, bg="#0d0d13")
header_frame.pack(pady=15, fill="x", padx=30)

terminal_title = tk.Label(header_frame, text="PASSWORD ANALYZER ", font=("Consolas", 14, "bold"), bg="#0d0d13", fg="#00eeff")
terminal_title.pack(anchor="w")

terminal_sub = tk.Label(header_frame, text="", font=("Consolas", 8), bg="#0d0d13", fg="#555566")
terminal_sub.pack(anchor="w")

# Circular Gauge
canvas = tk.Canvas(root, width=160, height=160, bg="#0d0d13", bd=0, highlightthickness=0)
canvas.pack(pady=10)

canvas.create_oval(10, 10, 150, 150, outline="#1f1f2e", width=6)
arc = canvas.create_arc(10, 10, 150, 150, start=90, extent=0, outline="#9900ff", width=8, style="arc")

entropy_label = tk.Label(root, text="0%", font=("Consolas", 22, "bold"), bg="#0d0d13", fg="#888899")
entropy_label.place(x=175, y=145)

status_label = tk.Label(root, text="", font=("Consolas", 11, "bold"), bg="#0d0d13", fg="#888899")
status_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#1a1a26", highlightthickness=1, highlightbackground="#9900ff")
input_frame.pack(pady=15, padx=40, fill="x")

password_var = tk.StringVar()
password_var.trace_add("write", calculate_entropy_and_update)

password_entry = tk.Entry(input_frame, textvariable=password_var, font=("Consolas", 14), show="*", width=20, bd=0, bg="#1a1a26", fg="#ffffff", insertbackground="#9900ff")
password_entry.pack(pady=8, padx=10, fill="x")
password_entry.focus()

entry_hint = tk.Label(root, text="[ ENTER YOUR PASSWORD ]", font=("Consolas", 8), bg="#0d0d13", fg="#555566")
entry_hint.pack()

# Requirements Checklist Frame
frame_rules = tk.LabelFrame(root, text=" Requirements Checklist ", font=("Consolas", 9, "bold"), bg="#0d0d13", fg="#00eeff", bd=1, relief="solid", padx=15, pady=12)
frame_rules.pack(pady=20, fill="x", padx=40)

lbl_cond_len = tk.Label(frame_rules, text="○ Min 8 Characters", font=("Consolas", 10), bg="#0d0d13", fg="#555566", anchor="w")
lbl_cond_len.pack(fill="x", pady=3)

lbl_cond_upper = tk.Label(frame_rules, text="○ Uppercase [A-Z]", font=("Consolas", 10), bg="#0d0d13", fg="#555566", anchor="w")
lbl_cond_upper.pack(fill="x", pady=3)

lbl_cond_digit = tk.Label(frame_rules, text="○ Number [0-9]", font=("Consolas", 10), bg="#0d0d13", fg="#555566", anchor="w")
lbl_cond_digit.pack(fill="x", pady=3)

lbl_cond_symbol = tk.Label(frame_rules, text="○ Special Symbol", font=("Consolas", 10), bg="#0d0d13", fg="#555566", anchor="w")
lbl_cond_symbol.pack(fill="x", pady=3)

# UI Aesthetics & Footer
decor_line = tk.Frame(root, height=1, bg="#1f1f2e")
decor_line.pack(fill="x", padx=50, pady=10)

system_log_lbl = tk.Label(root, text="", font=("Consolas", 8), bg="#0d0d13", fg="#555566")
system_log_lbl.pack()

footer = tk.Label(root, text="", font=("Consolas", 8, "italic"), bg="#0d0d13", fg="#333344")
footer.pack(side="bottom", pady=15)

root.mainloop()