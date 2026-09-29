
# main.py

from data import INITIAL_STUDENT, ACTIVITIES, TOTAL_DAYS, DAILY_TIME
from student import show_status, check_warnings, limit_stats
from activites import perform_activity
from events import random_event
from report import final_report


def main():
    # Create a separate copy of the initial student data.
    student = INITIAL_STUDENT.copy()

    total_energy = 0
    days_completed = 0

    print("=" * 45)
    print("             CAMPUS BALANCE")
    print(" Student Life Management Simulator")
    print("=" * 45)

    print("\nWelcome to Campus Balance!")
    print(f"You will manage your college life for {TOTAL_DAYS} days.")

    print("\nStarting Statistics:")
    show_status(student)

    # Repeat the simulation for 7 days.
    for day in range(1, TOTAL_DAYS + 1):
        print("\n")
        print("=" * 45)
        print(f"                 DAY {day}")
        print("=" * 45)

        available_time = DAILY_TIME

        print(f"\nAvailable time today: {available_time} hours")

        # Allow multiple activities each day.
        while available_time > 0:
            print("\nChoose an activity:")

            for i, activity in enumerate(ACTIVITIES, start=1):
                print(f"{i}. {activity}")

            print("8. Finish the day")

            print(f"\nRemaining time: {available_time} hours")

            choice = input("Enter your choice (1-8): ")

            # Validate that the input is a number.
            if not choice.isdigit():
                print("Please enter a number between 1 and 8.")
                continue

            choice = int(choice)

            if choice == 8:
                print("\nYou decided to finish the day.")
                break

            if choice < 1 or choice > 7:
                print("Invalid choice. Please try again.")
                continue

            # Calculate how much time the activity consumes.
            time_costs = {
                1: 3,
                2: 2,
                3: 2,
                4: 1,
                5: 2,
                6: 2,
                7: 4
            }

            required_time = time_costs[choice]

            if required_time > available_time:
                print("Not enough time for this activity!")
                continue

            # Check whether the student has enough energy.
            energy_costs = {
                1: 10,
                2: 15,
                3: 0,
                4: 10,
                5: 5,
                6: 3,
                7: 20
            }

            if student["energy"] < energy_costs[choice]:
                if choice != 3:
                    print("You are too tired for this activity.")
                    print("Try sleeping to restore your energy.")
                    continue

            # Perform the selected activity.
            used_time = perform_activity(choice, student)

            available_time -= used_time

            print(f"\nTime remaining: {available_time} hours")

            # Display updated statistics.
            show_status(student)

            # Check for warnings.
            check_warnings(student)

        # A random event happens at the end of each day.
        print("\nEnd of day", day)

        random_event(student)

        # Restore a small amount of energy overnight.
        student["energy"] += 10
        limit_stats(student)

        print("\nOvernight rest restored 10 energy points.")

        total_energy += student["energy"]
        days_completed += 1

        print("\nDay", day, "completed!")

    # Calculate the average energy across the 7 days.
    average_energy = round(total_energy / days_completed)

    # Display and save the final report.
    final_report(student, average_energy, days_completed)

    print("\nThank you for playing Campus Balance!")


if __name__ == "__main__":
    main()