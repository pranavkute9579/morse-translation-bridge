import tkinter as tk
from tkinter import ttk
import time
import winsound

# ---------------- MORSE DICTIONARIES ----------------
TEXT_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',
    ' ': '/'
}

MORSE_TO_TEXT = {v: k for k, v in TEXT_TO_MORSE.items()}

DOT = 150
DASH = 450
FREQ = 800

# ---------------- FUNCTIONS ----------------
def text_to_morse():
    text = input_box.get("1.0", "end").upper()
    morse = ""
    for char in text:
        morse += TEXT_TO_MORSE.get(char, '') + ' '
    output_box.delete("1.0", "end")
    output_box.insert("end", morse)

def morse_to_text():
    morse = input_box.get("1.0", "end").strip().split(' ')
    text = ""
    for code in morse:
        text += MORSE_TO_TEXT.get(code, '')
    output_box.delete("1.0", "end")
    output_box.insert("end", text)

def play_morse():
    morse = output_box.get("1.0", "end")
    for symbol in morse:
        if symbol == '.':
            winsound.Beep(FREQ, DOT)
        elif symbol == '-':
            winsound.Beep(FREQ, DASH)
        elif symbol == '/':
            time.sleep(0.5)
        time.sleep(0.1)

# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Morse Translation Bridge")
root.geometry("1200x650")
root.configure(bg="#0b0f14")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=12)
style.configure("TLabel", background="#0b0f14", foreground="#f5b041",
                font=("Segoe UI", 16, "bold"))

# ---------------- TITLE ----------------
ttk.Label(root, text="THE TRANSLATION BRIDGE").pack(pady=20)

# ---------------- MAIN FRAME ----------------
frame = tk.Frame(root, bg="#0b0f14")
frame.pack(expand=True)

# ---------------- INPUT ----------------
input_frame = tk.Frame(frame, bg="#0b0f14")
input_frame.grid(row=0, column=0, padx=40)

ttk.Label(input_frame, text="INPUT").pack(pady=10)

input_box = tk.Text(
    input_frame, width=45, height=15,
    bg="#111", fg="#f5b041",
    insertbackground="white",
    font=("Consolas", 12)
)
input_box.pack()

# ---------------- OUTPUT ----------------
output_frame = tk.Frame(frame, bg="#0b0f14")
output_frame.grid(row=0, column=1, padx=40)

ttk.Label(output_frame, text="OUTPUT").pack(pady=10)

output_box = tk.Text(
    output_frame, width=45, height=15,
    bg="#111", fg="#f5b041",
    insertbackground="white",
    font=("Consolas", 12)
)
output_box.pack()

# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(root, bg="#0b0f14")
btn_frame.pack(pady=30)

ttk.Button(btn_frame, text="TEXT → MORSE", command=text_to_morse).grid(row=0, column=0, padx=15)
ttk.Button(btn_frame, text="MORSE → TEXT", command=morse_to_text).grid(row=0, column=1, padx=15)
ttk.Button(btn_frame, text="PLAY MORSE SOUND", command=play_morse).grid(row=0, column=2, padx=15)

# ---------------- RUN ----------------
root.mainloop()
