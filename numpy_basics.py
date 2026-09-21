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