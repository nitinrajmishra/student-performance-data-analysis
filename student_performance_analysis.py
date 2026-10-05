import csv
import math
import statistics

def mean(values):
    return sum(values) / len(values)

def correlation(x, y):
    mx, my = mean(x), mean(y)
    numerator = sum((a - mx) * (b - my) for a, b in zip(x, y))
    denominator = math.sqrt(
        sum((a - mx) ** 2 for a in x) *
        sum((b - my) ** 2 for b in y)
    )
    return numerator / denominator if denominator else 0

# Read dataset
students = []
with open("student_performance_dataset.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "name": row["Student"],
            "attendance": float(row["Attendance_Percent"]),
            "maths": float(row["Maths"]),
            "python": float(row["Python"]),
            "dbms": float(row["DBMS"])
        })

attendance = [s["attendance"] for s in students]
maths = [s["maths"] for s in students]
python_marks = [s["python"] for s in students]
dbms = [s["dbms"] for s in students]

average_marks = []
for s in students:
    avg = (s["maths"] + s["python"] + s["dbms"]) / 3
    average_marks.append(avg)

print("Average attendance:", mean(attendance))
print("Average Maths marks:", mean(maths))
print("Average Python marks:", mean(python_marks))
print("Average DBMS marks:", mean(dbms))

print("Median Maths marks:", statistics.median(maths))
print("Mode Maths marks:", statistics.mode(maths))
print("Maths variance:", statistics.pvariance(maths))
print("Maths standard deviation:", statistics.pstdev(maths))

print("Correlation between attendance and average marks:",
      correlation(attendance, average_marks))

best_index = average_marks.index(max(average_marks))
print("Top student:", students[best_index]["name"])
print("Top student's average:", average_marks[best_index])
