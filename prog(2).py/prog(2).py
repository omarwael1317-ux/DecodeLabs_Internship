import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
        else:
            result.append(char)
    return "".join(result)

def process_crypto_logic(*args):
    input_text = text_entry.get("1.0", tk.END).strip()
    length = len(input_text)
    
    try:
        shift_key = int(shift_spinner.get())
    except ValueError:
        shift_key = 3

    has_text = length > 0
    has_alpha = any(char.isalpha() for char in input_text)
    key_valid = 1 <= shift_key <= 25
    
    lbl_cond_text.config(fg="#00aa44" if has_text else "#778899", text="✔ Data Payload Loaded" if has_text else "○ Data Payload Loaded")
    lbl_cond_alpha.config(fg="#00aa44" if has_alpha else "#778899", text="✔ Alphabetic Characters Found" if has_alpha else "○ Alphabetic Characters Found")
    lbl_cond_key.config(fg="#00aa44" if key_valid else "#778899", text="✔ Cipher Key Verified" if key_valid else "○ Cipher Key Verified")

    if not has_text:
        canvas.itemconfig(arc, outline="#e0e0e0", extent=0)
        status_label.config(text="SYSTEM IDLE // AWAITING STREAM", fg="#0066cc")
        output_entry.config(state="normal")
        output_entry.delete("1.0", tk.END)
        output_entry.config(state="disabled")
        return

    encrypted_text = caesar_cipher(input_text, shift_key, decrypt=False)
    output_entry.config(state="normal")
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", encrypted_text)
    output_entry.config(state="disabled")

    if not has_alpha:
        canvas.itemconfig(arc, outline="#555555", extent=-90)
        status_label.config(text="PROCESSING ◆ NO ALPHABETIC DATA", fg="#555555")
    elif has_alpha and length < 10:
        canvas.itemconfig(arc, outline="#0066cc", extent=-180)
        status_label.config(text="PROCESSING ◆ WEAK STREAM ENCRYPTION", fg="#0066cc")
    else:
        canvas.itemconfig(arc, outline="#00aa44", extent=-359.9)
        status_label.config(text="SUCCESS ◆ STREAM FULLY OBFUSCATED", fg="#00aa44")

root = tk.Tk()
root.title("CRYPTO MATRIX ANALYZER")
root.geometry("440x700")
root.configure(bg="#ffffff")
root.resizable(False, False)

header_frame = tk.Frame(root, bg="#ffffff")
header_frame.pack(pady=15, fill="x", padx=35)

terminal_title = tk.Label(header_frame, text="CRYPTO MATRIX ANALYZER", font=("Consolas", 13, "bold"), bg="#ffffff", fg="#0066cc")
terminal_title.pack(anchor="w")

terminal_sub = tk.Label(header_frame, text="", font=("Consolas", 8), bg="#ffffff", fg="#778899")
terminal_sub.pack(anchor="w")

canvas = tk.Canvas(root, width=130, height=130, bg="#ffffff", bd=0, highlightthickness=0)
canvas.pack(pady=5)

canvas.create_oval(10, 10, 120, 120, outline="#e0e0e0", width=5)
arc = canvas.create_arc(10, 10, 120, 120, start=90, extent=0, outline="#0066cc", width=7, style="arc")

status_label = tk.Label(root, text="", font=("Consolas", 10, "bold"), bg="#ffffff", fg="#0066cc")
status_label.pack(pady=5)

# Input Box Block
lbl_input = tk.Label(root, text="[ TARGET PLAIN-TEXT STREAM ]", font=("Consolas", 9, "bold"), bg="#ffffff", fg="#0066cc")
lbl_input.pack(anchor="w", padx=40, pady=(10, 0))

text_entry = tk.Text(root, font=("Consolas", 11), width=42, height=4, bg="#f5f7fa", fg="#222222", bd=0, highlightthickness=1, highlightbackground="#d0d5dd", highlightcolor="#0066cc", insertbackground="#222222")
text_entry.pack(pady=5, padx=40)
text_entry.bind("<KeyRelease>", process_crypto_logic)

# Shift Key Configuration Block
config_frame = tk.Frame(root, bg="#ffffff")
config_frame.pack(pady=10, fill="x", padx=40)

lbl_shift = tk.Label(config_frame, text="CIPHER SHIFT KEY (n):", font=("Consolas", 9, "bold"), bg="#ffffff", fg="#222222")
lbl_shift.pack(side="left")

style = ttk.Style()
style.theme_use('clam')
style.configure("TSpinbox", fieldbackground="#f5f7fa", background="#e0e0e0", foreground="#0066cc", borderwidth=0)

shift_spinner = ttk.Spinbox(config_frame, from_=1, to=25, width=5, font=("Consolas", 10, "bold"), style="TSpinbox", command=process_crypto_logic)
shift_spinner.set(3)
shift_spinner.pack(side="left", padx=10)

# Output Box Block
lbl_output = tk.Label(root, text="[ LIVE OBFUSCATED OUTPUT ]", font=("Consolas", 9, "bold"), bg="#ffffff", fg="#0066cc")
lbl_output.pack(anchor="w", padx=40, pady=(10, 0))

output_entry = tk.Text(root, font=("Consolas", 11), width=42, height=4, bg="#edf7ed", fg="#00aa44", bd=0, highlightthickness=1, highlightbackground="#cce8cd", state="disabled")
output_entry.pack(pady=5, padx=40)

# Live Requirements Checklist Frame
frame_rules = tk.LabelFrame(root, text=" Cipher Engine Checklist ", font=("Consolas", 9, "bold"), bg="#ffffff", fg="#0066cc", bd=1, relief="solid", padx=15, pady=8)
frame_rules.pack(pady=15, fill="x", padx=40)

lbl_cond_text = tk.Label(frame_rules, text="○ Data Payload Loaded", font=("Consolas", 9), bg="#ffffff", fg="#778899", anchor="w")
lbl_cond_text.pack(fill="x", pady=2)

lbl_cond_alpha = tk.Label(frame_rules, text="○ Alphabetic Characters Found", font=("Consolas", 9), bg="#ffffff", fg="#778899", anchor="w")
lbl_cond_alpha.pack(fill="x", pady=2)

lbl_cond_key = tk.Label(frame_rules, text="○ Cipher Key Verified", font=("Consolas", 9), bg="#ffffff", fg="#778899", anchor="w")
lbl_cond_key.pack(fill="x", pady=2)

# Footer Layout
decor_line = tk.Frame(root, height=1, bg="#e0e0e0")
decor_line.pack(fill="x", padx=50, pady=5)

system_log_lbl = tk.Label(root, text="SECURE CRYPTO ENGINE STANDARD RUNTIME", font=("Consolas", 8), bg="#ffffff", fg="#778899")
system_log_lbl.pack()

footer = tk.Label(root, text="▲ CORE_DEFENSIVE_STAGE_2 ▲", font=("Consolas", 8, "italic"), bg="#ffffff", fg="#cbd5e1")
footer.pack(side="bottom", pady=10)

root.mainloop()