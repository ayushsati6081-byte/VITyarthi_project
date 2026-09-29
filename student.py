
# student.py


def show_status(student):
    print("\n========== STUDENT STATUS ==========")
    print(f"Money          : Rs. {student['money']}")
    print(f"Energy         : {student['energy']}/100")
    print(f"Health         : {student['health']}/100")
    print(f"Stress         : {student['stress']}/100")
    print(f"Attendance     : {student['attendance']}%")
    print(f"Academic Score : {student['academic_score']}/100")
    print(f"Happiness      : {student['happiness']}/100")
    print(f"Screen Time    : {student['screen_time']} hours")
    print(f"Sleep          : {student['sleep_hours']} hours")
    print("====================================")


def limit_stats(student):
    # Keep statistics between 0 and 100
    for key in [
        "energy",
        "health",
        "stress",
        "attendance",
        "academic_score",
        "happiness"
    ]:
        student[key] = max(0, min(100, student[key]))

    # These values cannot be negative
    student["money"] = max(0, student["money"])
    student["screen_time"] = max(0, student["screen_time"])


def check_warnings(student):
    print("\n---------- WARNINGS ----------")

    warning_found = False

    if student["energy"] < 20:
        print("WARNING: Your energy is very low!")
        warning_found = True

    if student["health"] < 30:
        print("WARNING: Your health is very low!")
        warning_found = True

    if student["stress"] > 80:
        print("WARNING: Your stress is very high!")
        warning_found = True

    if student["attendance"] < 75:
        print("WARNING: Attendance is below 75%!")
        warning_found = True

    if student["money"] < 200:
        print("WARNING: You are running low on money!")
        warning_found = True

    if student["screen_time"] > 30:
        print("WARNING: Your screen time is very high!")
        warning_found = True

    if not warning_found:
        print("No major problems right now.")

    print("------------------------------")