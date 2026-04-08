from server.app import app
from server.models import db, Workout, Exercise, WorkoutExercise

with app.app_context():
    # Clear tables
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    # Create exercises
    e1 = Exercise(name="Push Ups", category="Strength", equipment_needed=False)
    e2 = Exercise(name="Running", category="Cardio", equipment_needed=False)

    # Create workouts
    w1 = Workout(date="2026-04-06", duration_minutes=45, notes="Morning")
    w2 = Workout(date="2026-04-07", duration_minutes=60, notes="Evening")

    db.session.add_all([e1, e2, w1, w2])
    db.session.commit()

    # Link them
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, reps=10, sets=3)
    we2 = WorkoutExercise(workout_id=w2.id, exercise_id=e2.id, duration_seconds=600)

    db.session.add_all([we1, we2])
    db.session.commit()

    print("Seeded database with sample workouts and exercises")