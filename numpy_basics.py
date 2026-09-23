import numpy as np

students = np.array([
    [80, 90, 75],
    [70, 85, 80],
    [95, 88, 92]
])

print(students)


print("Shape:", students.shape)

print("Number of dimensions:", students.ndim)

print("Overall Average:", students.mean())

print("Subject-wise Average:", students.mean(axis=0))

print("Student-wise Average:", students.mean(axis=1))

import numpy as np

marks = np.array([75, 82, 90, 68, 88])

# Indexing
print("First mark:", marks[0])
print("Third mark:", marks[2])

# Filtering
print("Marks above 80:", marks[marks > 80])

# Marks above or equal to 80
print("Marks >= 80:", marks[marks >= 80])

# Marks below 80
print("Marks below 80:", marks[marks < 80])