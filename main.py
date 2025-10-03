# Madan Karki, Student ID: 32100247
# COMP1003 Nurse Attrition Project

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import tkinter as tk
from tkinter import ttk



# Step 1: Load the CSV file
data = pd.read_csv("nurse_attrition 01 10 2025.csv")

# Step 2: Display basic info
print("Total rows and columns:", data.shape)
print("First 5 rows of data:")
print(data.head())
# ---- Step 3: Summary Calculations ----

# Total employees
total_employees = len(data)

# Unique departments
departments = data['Department'].unique()

# Count of employees in each department
dept_counts = data['Department'].value_counts()

# Male vs Female count
gender_counts = data['Gender'].value_counts()

# Age statistics
min_age = data['Age'].min()
max_age = data['Age'].max()
avg_age = data['Age'].mean()

# Distance from home stats
min_dist = data['DistanceFromHome'].min()
max_dist = data['DistanceFromHome'].max()
avg_dist = data['DistanceFromHome'].mean()

# Hourly rate stats
min_rate = data['HourlyRate'].min()
max_rate = data['HourlyRate'].max()
avg_rate = data['HourlyRate'].mean()

# Marital status percentages
marital_percent = data['MaritalStatus'].value_counts(normalize=True) * 100

# Average work-life balance
avg_wlb = data['WorkLifeBalance'].mean()

# Total attritions
total_attrition = (data['Attrition'] == "Yes").sum()

# ---- Print results ----
print("\n----- SUMMARY REPORT -----")
print("Total Employees:", total_employees)
print("Departments:", list(departments))
print("\nEmployees per Department:\n", dept_counts)
print("\nGender Distribution:\n", gender_counts)
print(f"\nAge -> Min: {min_age}, Max: {max_age}, Avg: {avg_age:.2f}")
print(f"Distance from Home -> Min: {min_dist}, Max: {max_dist}, Avg: {avg_dist:.2f}")
print(f"Hourly Rate -> Min: {min_rate}, Max: {max_rate}, Avg: {avg_rate:.2f}")
print("\nMarital Status Percentages:\n", marital_percent)
print("Average Work-Life Balance:", round(avg_wlb, 2))
print("Total Attritions:", total_attrition)
# ---- Visualization: Pie Chart ----
def show_pie_chart():
    dept_counts = data['Department'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Employees per Department")
    plt.show()
show_pie_chart()
# ---- Visualization: Bar Chart ----
def show_bar_chart():
    marital_counts = data['MaritalStatus'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.bar(marital_counts.index, marital_counts.values, color=['blue', 'green', 'orange'])
    plt.title("Employees by Marital Status")
    plt.xlabel("Marital Status")
    plt.ylabel("Number of Employees")
    plt.show()
show_bar_chart()
# ---- Visualization: Dashboard with Tkinter ----
def launch_dashboard():
    root = tk.Tk()
    root.title("Madan Karki - 32100247 Nurse Attrition Dashboard")
    root.geometry("400x300")

    # Labels
    ttk.Label(root, text=f"Total Employees: {total_employees}").pack(pady=5)
    ttk.Label(root, text=f"Departments: {', '.join(departments)}").pack(pady=5)
    ttk.Label(root, text=f"Attrition Count: {total_attrition}").pack(pady=5)
    ttk.Label(root, text=f"Average Age: {avg_age:.2f}").pack(pady=5)
    ttk.Label(root, text=f"Average Hourly Rate: {avg_rate:.2f}").pack(pady=5)

    # Buttons for charts
    ttk.Button(root, text="Show Pie Chart", command=show_pie_chart).pack(pady=5)
    ttk.Button(root, text="Show Bar Chart", command=show_bar_chart).pack(pady=5)

    root.mainloop()

# Launch dashboard
launch_dashboard()
total_employees = len(data)

