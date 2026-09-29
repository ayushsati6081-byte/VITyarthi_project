
# events.py

import random
from student import limit_stats


def random_event(student):
    print("\n========== RANDOM EVENT ==========")

    event = random.randint(1, 5)

    if event == 1:
        print("Unexpected expense! You need to pay Rs. 150.")

        print("1. Pay the expense")
        print("2. Delay the payment")

        choice = input("Enter your choice: ")

        if choice == "1":
            student["money"] -= 150
            print("You paid Rs. 150.")

        elif choice == "2":
            student["stress"] += 10
            print("Payment delayed. Stress increased.")

        else:
            print("Invalid choice. You delayed the payment.")
            student["stress"] += 10

    elif event == 2:
        print("You have a surprise quiz!")

        print("1. Take the quiz")
        print("2. Skip the quiz")

        choice = input("Enter your choice: ")

        if choice == "1":
            student["academic_score"] += 5
            student["stress"] += 5
            print("Quiz completed. Academic score increased.")

        elif choice == "2":
            student["attendance"] -= 5
            print("You skipped the quiz and lost attendance.")

        else:
            print("Invalid choice. Quiz skipped.")
            student["attendance"] -= 5

    elif event == 3:
        print("Your friend invited you to go out!")

        print("1. Go with your friend")
        print("2. Stay and study")

        choice = input("Enter your choice: ")

        if choice == "1":
            student["happiness"] += 10
            student["money"] -= 50
            print("You enjoyed time with your friend.")

        elif choice == "2":
            student["academic_score"] += 5
            student["stress"] += 2
            print("You studied instead.")

        else:
            print("Invalid choice. You stayed at home.")

    elif event == 4:
        print("A college club activity is available!")

        print("1. Participate")
        print("2. Decline")

        choice = input("Enter your choice: ")

        if choice == "1":
            student["happiness"] += 5
            student["health"] += 2
            print("You participated in the club activity.")

        elif choice == "2":
            print("You declined the opportunity.")

        else:
            print("Invalid choice. Opportunity declined.")

    elif event == 5:
        print("There is a transport problem!")

        print("1. Pay Rs. 100 for alternative transport")
        print("2. Walk instead")

        choice = input("Enter your choice: ")

        if choice == "1":
            student["money"] -= 100
            print("You paid for alternative transport.")

        elif choice == "2":
            student["energy"] -= 10
            student["health"] += 2
            print("You walked to your destination.")

        else:
            print("Invalid choice. You walked instead.")
            student["energy"] -= 10

    limit_stats(student)

    print("Random event completed.")
    print("==================================")