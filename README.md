# Workout API

## Project Overview
- This is a Flask REST API for managing workouts and exercises
- It allows creation, retrieval, and deletion of workouts and exercises
- It also supports linking exercises to specific workouts

## Features
- Create workouts
- View all workouts
- View single workout with exercises
- Delete workouts
- Create exercises
- View all exercises
- Delete exercises
- Link exercises to workouts using a join table

## Tech Stack
- Python
- Flask
- Flask SQLAlchemy
- SQLite

## Project Structure
- server/app.py contains the Flask application and routes
- server/models.py contains database models
- server/seed.py contains sample data for testing
- app.db is the SQLite database file

## Database Models

### Workout
- id
- date
- duration_minutes
- notes

### Exercise
- id
- name
- category
- equipment_needed

### WorkoutExercise
- id
- workout_id
- exercise_id
- reps
- sets
- duration_seconds

## Setup Instructions
- Clone the repository
- Create a virtual environment
- Install dependencies:
  - pip install -r requirements.txt
- Run database setup by starting the app or running seed file
- Start the server:
  - python -m server.app

## API Endpoints
- GET /workouts
- GET /workouts/<id>
- POST /workouts
- DELETE /workouts/<id>
- GET /exercises
- POST /exercises
- DELETE /exercises/<id>
- POST /workouts/<workout_id>/exercises/<exercise_id>

## Seeding Data
- Run:
  - python -m server.seed

## Notes
- Ensure virtual environment is activated before running commands
- Database is stored locally using SQLite
- Use browser or curl to test endpoints

## Author
- Priscillah Kamau