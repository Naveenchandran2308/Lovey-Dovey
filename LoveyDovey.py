import tkinter as tk
import random

# ------------------ CONFIG ------------------
girlfriend_names = [
    "MADHUMITHA NATARAJAN.N",
    "MADHUMITHA NATARAJAN",
    "MADHU",
]

# ------------------ MAIN WINDOW ------------------
root = tk.Tk()
root.title("💖 Just for You 💖")
root.geometry("1280x720")
root.config(bg="pink")

# ------------------ CANVAS ------------------
canvas = tk.Canvas(root, width=1280, height=720, bg="pink", highlightthickness=0)
canvas.place(x=0, y=0)

hearts = []

def animate_hearts():
    for _ in range(10):
        heart = canvas.create_text(
            random.randint(50, 1230),
            720,
            text=random.choice(["💖", "❤️", "💘", "💞", "😘"]),
            font=("Arial", random.randint(20, 40))
        )
        hearts.append(heart)
    move_hearts()

def move_hearts():
    for heart in hearts:
        canvas.move(heart, 0, -3)
        x, y = canvas.coords(heart)
        if y < -50:
            canvas.coords(heart, x, 720)
    root.after(50, move_hearts)

# ------------------ BUTTON CONFIG ------------------
yes_width = 150
yes_height = 60
growth_factor = 50
no_width = 150
no_height = 60

# ------------------ FUNCTIONS ------------------
def check_name():
    entered_name = name_entry.get().upper()
    if entered_name in girlfriend_names:
        message_label.config(text="💖 Love is in the air! 💖", fg="hot pink")
        marry_label.place(relx=0.5, y=380, anchor="n")
        yes_button.place(x=480, y=450, width=yes_width, height=yes_height)
        no_button.place(x=650, y=450, width=no_width, height=no_height)
        animate_hearts()
    else:
        message_label.config(text="😡 Get lost! 😡", fg="red")
        marry_label.place_forget()
        yes_button.place_forget()
        no_button.place_forget()

def no_clicked():
    global yes_width, yes_height
    yes_width += growth_factor
    yes_height += growth_factor // 2
    yes_width = min(yes_width, 1280)
    yes_height = min(yes_height, 720)
    yes_button.place(x=(1280 - yes_width)//2, y=(720 - yes_height)//2, width=yes_width, height=yes_height)
    yes_button.tkraise()
    message_label.place(x=640, y=550, anchor="n")
    message_label.config(text="💖 Try again! 💖", fg="hot pink")

def yes_clicked():
    # Remove first page widgets
    for widget in [title_label, name_label, name_entry, check_button, marry_label, message_label, yes_button, no_button]:
        widget.place_forget()
    
    # Show love page in same window
    show_love_page()

# ------------------ LOVE PAGE ------------------
def show_love_page():
    canvas.delete("all")  # Clear old hearts

    # Use separate list for love-page hearts
    love_hearts = []

    def animate_love_hearts():
        for _ in range(15):
            heart = canvas.create_text(
                random.randint(50, 1230),
                720,
                text=random.choice(["💖", "❤️", "💘", "💞", "😘"]),
                font=("Arial", random.randint(20, 40))
            )
            love_hearts.append(heart)
        move_love_hearts()

    def move_love_hearts():
        for heart in love_hearts:
            canvas.move(heart, 0, -3)
            x, y = canvas.coords(heart)
            if y < -50:
                canvas.coords(heart, x, 720)
        root.after(50, move_love_hearts)

    animate_love_hearts()

    # Sweet message
    sweet_label = tk.Label(root, text="💖 My Dearest Madhumitha 💖", font=("Arial", 36, "bold"), bg="pink", fg="hot pink")
    sweet_label.place(relx=0.5, rely=0.1, anchor="n")

    # I LOVE YOU label
    love_label = tk.Label(root, text="💖 I LOVE YOU 💖", font=("Arial", 36, "bold"), bg="pink", fg="white")
    love_label.place(relx=0.5, rely=0.2, anchor="n")

    # Poem
    poem_text = """Roses are red 🌹
Violets are blue 💙
Every moment I spend 💕
I just think of you 😘

You are my sunshine ☀️
My heart, my delight 💖
I love you forever ❤️
And hold you tight 💞
"""
    poem_label = tk.Label(root, text=poem_text, font=("Arial", 28, "bold"), bg="pink", fg="white", justify="center")
    poem_label.place(relx=0.5, rely=0.35, anchor="n")

    # Final small close button FAR below
    final_heart_btn = tk.Button(root, text="💖 Close 💖", font=("Arial", 22, "bold"), bg="white", fg="hot pink", command=root.quit)
    final_heart_btn.place(relx=0.5, rely=0.98, anchor="s")  # almost bottom

# ------------------ MAIN UI ------------------
title_label = tk.Label(root, text="💖💖💖 Hello, Beautiful! 💖💖💖", font=("Arial", 30, "bold"), bg="pink", fg="white")
title_label.place(relx=0.5, rely=0.1, anchor="center")

name_label = tk.Label(root, text="Type your name:", font=("Arial", 20), bg="pink", fg="white")
name_label.place(relx=0.5, rely=0.25, anchor="center")

name_entry = tk.Entry(root, font=("Arial", 20), justify="center")
name_entry.place(relx=0.5, rely=0.32, anchor="center", width=400)

check_button = tk.Button(root, text="Check Name 💌", font=("Arial", 18, "bold"), bg="white", fg="hot pink", command=check_name)
check_button.place(relx=0.5, rely=0.4, anchor="center")

marry_label = tk.Label(root, text="💍 Will you marry me? 💍", font=("Arial", 28, "bold"), bg="pink", fg="hot pink")
marry_label.place_forget()

message_label = tk.Label(root, text="", font=("Arial", 24, "bold"), bg="pink")
message_label.place(relx=0.5, rely=0.5, anchor="center")

yes_button = tk.Button(root, text="YES 💍", font=("Arial", 24, "bold"), bg="white", fg="hot pink", command=yes_clicked)
yes_button.place_forget()

no_button = tk.Button(root, text="NO 😢", font=("Arial", 24, "bold"), bg="white", fg="hot pink", command=no_clicked)
no_button.place_forget()

root.mainloop()