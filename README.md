# HabitTracker

The **Habit Tracker App** is a Django-based web application designed 
to help users track their habits and set reminders.

## Features
1. **User Management**: Register, login, and manage user accounts.
2. **Habit Tracking**: Create habits with descriptions, start and end dates.
3. **Reminders**: Be encouraged into process by reminders.
4. **User Experience Points (XP)**: Earn experience points for completing habits.
5. **Achievements**: Get all achievements, beat other users!

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
```
git clone https://github.com/DenyysChernenko/HabitTracker.git
cd HabitTracker
```
2. Create a virtual environment:
```
python -m venv venv
```
3. Activate the virtual environment:
```
On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Apply database migrations:
```
python manage.py migrate
```
6. Run the development server:
```
python manage.py runserver
```

## Usage
1. **Create a Habit**:
Log in or register if you are a new user.
Navigate to the "Create Habit" page.
Fill in the habit details such as name, description, start date, end date, etc.
Submit the form to create the habit.
2. **Set a Reminder**:
After creating a habit, navigate to the habit detail page.
Click on "Set Reminder".
Enter the reminder details such as time, frequency, and message.
Save the reminder.
3. **Track Habits and XP**:
As you complete habits, update the habit status.
Earn experience points (XP) based on your habits and streaks.

## Acknowledgments
This project was inspired by the need to develop good habits and track progress effectively.
Thanks to the Django community for providing a robust framework.
