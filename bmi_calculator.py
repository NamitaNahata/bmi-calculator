import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create or connect to SQLite database
conn = sqlite3.connect("bmi_data.db")
cursor = conn.cursor()

# Create table if it doesn’t exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bmi_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT
    )
''')
conn.commit()

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create or connect to SQLite database
conn = sqlite3.connect("bmi_data.db")
cursor = conn.cursor()

# Create table if it doesn’t exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bmi_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT
    )
''')
conn.commit()

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)

        # Classify BMI
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi < 25:
            category = "Normal weight"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        # Store data in SQLite
        cursor.execute("INSERT INTO bmi_records (weight, height, bmi, category) VALUES (?, ?, ?, ?)",
                       (weight, height, bmi, category))
        conn.commit()

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}", fg=color)
        messagebox.showinfo("Success", "BMI calculated and saved successfully!")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

# Function to view stored BMI records
def view_records():
    cursor.execute("SELECT * FROM bmi_records")
    records = cursor.fetchall()

    if not records:
        messagebox.showinfo("BMI Records", "No records found.")
        return

    records_text = "ID | Weight (kg) | Height (m) | BMI | Category\n" + "-" * 50 + "\n"
    for record in records:
        records_text += f"{record[0]} | {record[1]} | {record[2]} | {record[3]:.2f} | {record[4]}\n"

    messagebox.showinfo("BMI Records", records_text)

# Create the main window
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#2C3E50")  # Dark background

# Title Label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

# Weight Input
tk.Label(root, text="Enter Weight (kg):", font=("Arial", 12), bg="#2C3E50", fg="white").pack(pady=5)
weight_entry = tk.Entry(root, font=("Arial", 12), width=15)
weight_entry.pack()

# Height Input
tk.Label(root, text="Enter Height (m):", font=("Arial", 12), bg="#2C3E50", fg="white").pack(pady=5)
height_entry = tk.Entry(root, font=("Arial", 12), width=15)
height_entry.pack()

# Calculate Button
calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12, "bold"), bg="#27AE60", fg="white",
                             width=20, command=calculate_bmi)
calculate_button.pack(pady=10)

# View Records Button
view_button = tk.Button(root, text="View Saved Records", font=("Arial", 12, "bold"), bg="#2980B9", fg="white",
                        width=20, command=view_records)
view_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="BMI will be displayed here", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white")
result_label.pack(pady=20)

# Run the application
root.mainloop()

