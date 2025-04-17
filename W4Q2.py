import pandas as pd

# Creating a DataFrame with student details
data = {
    "Roll Number": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "Gender": ["F", "M", "M", "M", "F", "M", "F", "M", "F", "M"],
    "Marks1": [85, 76, 90, 65, 78, 89, 92, 56, 74, 88],
    "Marks2": [72, 81, 39, 45, 67, 78, 34, 55, 60, 49],
    "Marks3": [88, 90, 75, 80, 85, 79, 95, 83, 70, 77]
}

df = pd.DataFrame(data)

# a. Create a new column with total marks
df["Total Marks"] = df["Marks1"] + df["Marks2"] + df["Marks3"]

# b. Find the lowest marks in Marks1
lowest_marks1 = df["Marks1"].min()
print("Lowest Marks in Marks1:", lowest_marks1)

# c. Find the highest marks in Marks2
highest_marks2 = df["Marks2"].max()
print("Highest Marks in Marks2:", highest_marks2)

# d. Find the average marks in Marks3
average_marks3 = df["Marks3"].mean()
print("Average Marks in Marks3:", average_marks3)

# e. Find the student name with the highest average marks
df["Average Marks"] = df["Total Marks"] / 3
top_student = df.loc[df["Average Marks"].idxmax(), "Name"]
print("Student with Highest Average Marks:", top_student)

# f. Find how many students failed in Marks2 (<40)
failed_students = (df["Marks2"] < 40).sum()
print("Number of students who failed in Marks2:", failed_students)

# Display the DataFrame
print(df)
