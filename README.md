 Campus Balance

Campus Balance is a command-line student life management simulator written in Python. Play through a seven-day college week by balancing studies, attendance, health, happiness, money, energy, stress, and screen time.

Each day, you have 12 hours to spend on activities. Random events add unexpected choices, and a weekly report summarizes your results and highlights potential problem areas.

## Features

- Simulate a student’s college life over seven days.
- Choose from seven activities:
  - Attend classes
  - Study
  - Sleep
  - Exercise
  - Socialize
  - Use a phone
  - Work part-time
- Manage daily time and energy.
- Track money, health, stress, attendance, academic score, happiness, screen time, and sleep.
- Receive warnings when statistics reach concerning levels.
- Encounter a random event at the end of each day.
- View a weekly summary and identified problem areas.
- Save the final report to reports/weekly_report.txt.

## Technologies and Tools

- Python 3
- Python standard library:
  - random for random events
  - os for creating the report directory and saving the report

No third-party packages are required.

## Installation and Run

1. Install Python 3 if it is not already installed.
2. Place the project files in the same directory:

   ```text
   main.py
   activities.py=
   data.py
   events.py
   report.py
   student.py
1. Check the activity module import in main.py. The supplied code uses activites, but the module filename is activities.py.     Update the import to:
  from activities import perform_activity
2. Open a terminal in the project directory and run:
       python main.py
3.  Depending on your system, you may need to use:
      python3 main.py
