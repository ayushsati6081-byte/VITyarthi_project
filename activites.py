
# activities.py

from student import limit_stats


def attend_class(student):
    student["attendance"] += 5
    student["energy"] -= 10
    student["stress"] += 2

    print("\nYou attended your classes.")
    print("Attendance increased.")
    print("Energy decreased by 10.")
    print("Stress increased by 2.")


def study(student):
    student["academic_score"] += 10
    student["energy"] -= 15
    student["stress"] += 5

    print("\nYou studied for 2 hours.")
    print("Academic score increased by 10.")
    print("Energy decreased by 15.")
    print("Stress increased by 5.")


def sleep(student):
    student["energy"] += 25
    student["stress"] -= 10
    student["health"] += 3
    student["sleep_hours"] += 2

    print("\nYou slept for 2 hours.")
    print("Energy increased by 25.")
    print("Stress decreased by 10.")
    print("Health improved.")


def exercise(student):
    student["health"] += 10
    student["energy"] -= 10
    student["stress"] -= 5

    print("\nYou exercised.")
    print("Health increased by 10.")
    print("Energy decreased by 10.")
    print("Stress decreased by 5.")


def socialize(student):
    student["happiness"] += 10
    student["energy"] -= 5
    student["money"] -= 50

    print("\nYou spent time with friends.")
    print("Happiness increased by 10.")
    print("Energy decreased by 5.")
    print("Rs. 50 spent.")


def use_phone(student):
    student["screen_time"] += 2
    student["energy"] -= 3
    student["happiness"] += 3

    print("\nYou used your phone for 2 hours.")
    print("Screen time increased by 2 hours.")
    print("Happiness increased slightly.")


def part_time_work(student):
    student["money"] += 200
    student["energy"] -= 20
    student["stress"] += 5

    print("\nYou worked part-time.")
    print("You earned Rs. 200.")
    print("Energy decreased by 20.")
    print("Stress increased by 5.")


def perform_activity(choice, student):
    # Each activity has a time cost in hours.

    time_costs = {
        1: 3,
        2: 2,
        3: 2,
        4: 1,
        5: 2,
        6: 2,
        7: 4
    }

    if choice == 1:
        attend_class(student)

    elif choice == 2:
        study(student)

    elif choice == 3:
        sleep(student)

    elif choice == 4:
        exercise(student)

    elif choice == 5:
        socialize(student)

    elif choice == 6:
        use_phone(student)

    elif choice == 7:
        part_time_work(student)

    else:
        print("Invalid activity choice.")
        return 0

    limit_stats(student)

    return time_costs[choice]