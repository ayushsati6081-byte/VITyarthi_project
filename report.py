
# report.py

import os


def identify_problem(student):
    problems = []

    if student["attendance"] < 75:
        problems.append("Low attendance")

    if student["stress"] > 70:
        problems.append("High stress")

    if student["money"] < 200:
        problems.append("Financial management")

    if student["academic_score"] < 40:
        problems.append("Low academic performance")

    if student["health"] < 40:
        problems.append("Poor health")

    if student["screen_time"] > 30:
        problems.append("Excessive screen time")

    if student["energy"] < 25:
        problems.append("Low energy")

    if student["happiness"] < 30:
        problems.append("Low happiness")

    if not problems:
        problems.append("No major problem identified")

    return problems


def final_report(student, average_energy, days_completed):
    print("\n")
    print("=" * 45)
    print("             WEEKLY REPORT")
    print("=" * 45)

    print(f"Days Completed      : {days_completed}/7")
    print(f"Money Remaining     : Rs. {student['money']}")
    print(f"Attendance          : {student['attendance']}%")
    print(f"Academic Score      : {student['academic_score']}/100")
    print(f"Health              : {student['health']}/100")
    print(f"Average Energy      : {average_energy}/100")
    print(f"Stress              : {student['stress']}/100")
    print(f"Happiness           : {student['happiness']}/100")
    print(f"Total Screen Time   : {student['screen_time']} hours")

    problems = identify_problem(student)

    print("\nMajor Problem Areas:")

    for problem in problems:
        print("- " + problem)

    print("=" * 45)

    # Save the report to a text file.

    os.makedirs("reports", exist_ok=True)

    file_path = os.path.join("reports", "weekly_report.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("CAMPUS BALANCE - WEEKLY REPORT\n")
        file.write("=" * 35 + "\n")
        file.write(f"Days Completed: {days_completed}/7\n")
        file.write(f"Money Remaining: Rs. {student['money']}\n")
        file.write(f"Attendance: {student['attendance']}%\n")
        file.write(
            f"Academic Score: {student['academic_score']}/100\n"
        )
        file.write(f"Health: {student['health']}/100\n")
        file.write(f"Average Energy: {average_energy}/100\n")
        file.write(f"Stress: {student['stress']}/100\n")
        file.write(f"Happiness: {student['happiness']}/100\n")
        file.write(
            f"Total Screen Time: {student['screen_time']} hours\n"
        )

        file.write("\nMajor Problem Areas:\n")

        for problem in problems:
            file.write("- " + problem + "\n")

    print("\nReport saved successfully!")
    print("Location: reports/weekly_report.txt")