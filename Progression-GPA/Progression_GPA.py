import matplotlib.pyplot as plt

sgpa = []
cgpa = []
total = 0

n = int(input("Enter number of semesters: "))

for i in range(1, n + 1):
    value = float(input(f"Enter SGPA for Semester {i}: "))
    sgpa.append(value)
    total += value
    cgpa.append(total / i)

semesters = list(range(1, n + 1))
final_cgpa = cgpa[-1]

plt.plot(semesters, sgpa, marker='o', label="SGPA")
plt.plot(semesters, cgpa, marker='o', label="CGPA")

plt.xlabel("Semester")
plt.ylabel("Grade Point")
plt.title("SGPA and CGPA Progression")
plt.legend()

plt.subplots_adjust(bottom=0.2)
plt.figtext(
    0.5, 0.05,
    f"CGPA: {final_cgpa:.2f}",
    ha="center",
    fontsize=12,
    weight="bold"
)

plt.show()
