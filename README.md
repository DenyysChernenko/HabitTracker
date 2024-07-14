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

## Running with Docker

To run this application using Docker, follow these steps:

1. Clone the repository:
```
git clone https://github.com/DenyysChernenko/HabitTracker.git
cd HabitTracker
```

2. Build the Docker image and start the container:
```bash
docker-compose up --build
```

3. Access the application:
```bash
http://localhost:8001
```

4. Initialize the database
```
docker-compose exec web python manage.py migrate
```

## Explanation
1. *Cloning the Repository*: This step remains the same as in the previous sections.
2. *Building and Running Docker*: Use docker-compose up --build to build the Docker image defined in your docker-compose.yml and start the container.
3. *Accessing the Application*: After Docker starts the container, your application should be accessible at ```http://localhost:8001```.
4. *Initializing the Database*: If it's your first time running the application with Docker, you may need to apply initial migrations to set up the database. 
This is done using docker-compose exec web python manage.py migrate

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
