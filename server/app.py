import os
from flask import Flask, jsonify, request
from server.models import db, Workout, Exercise, WorkoutExercise

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "app.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "<h1>Workout API Running</h1>"


# -------------------
# WORKOUT ROUTES
# -------------------

@app.route("/workouts")
def get_workouts():
    workouts = Workout.query.all()

    result = []
    for w in workouts:
        result.append({
            "id": w.id,
            "date": w.date,
            "duration_minutes": w.duration_minutes,
            "notes": w.notes
        })

    return jsonify(result)


@app.route("/workouts/<int:id>")
def get_workout(id):
    w = Workout.query.get(id)

    if not w:
        return {"error": "Workout not found"}, 404

    exercises = []
    for we in w.workout_exercises:
        exercises.append({
            "exercise": we.exercise.name,
            "reps": we.reps,
            "sets": we.sets,
            "duration_seconds": we.duration_seconds
        })

    return jsonify({
        "id": w.id,
        "date": w.date,
        "duration_minutes": w.duration_minutes,
        "notes": w.notes,
        "exercises": exercises
    })


@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.get_json()

    new_workout = Workout(
        date=data["date"],
        duration_minutes=data["duration_minutes"],
        notes=data.get("notes")
    )

    db.session.add(new_workout)
    db.session.commit()

    return {"message": "Workout created"}, 201


@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    w = Workout.query.get(id)

    if not w:
        return {"error": "Not found"}, 404

    db.session.delete(w)
    db.session.commit()

    return {"message": "Deleted"}
    

# -------------------
# EXERCISE ROUTES
# -------------------

@app.route("/exercises")
def get_exercises():
    exercises = Exercise.query.all()

    return jsonify([
        {
            "id": e.id,
            "name": e.name,
            "category": e.category,
            "equipment_needed": e.equipment_needed
        }
        for e in exercises
    ])


@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.get_json()

    e = Exercise(
        name=data["name"],
        category=data["category"],
        equipment_needed=data["equipment_needed"]
    )

    db.session.add(e)
    db.session.commit()

    return {"message": "Exercise created"}, 201


@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    e = Exercise.query.get(id)

    if not e:
        return {"error": "Not found"}, 404

    db.session.delete(e)
    db.session.commit()

    return {"message": "Exercise deleted"}


# -------------------
# ADD EXERCISE TO WORKOUT
# -------------------

@app.route("/workouts/<int:w_id>/exercises/<int:e_id>", methods=["POST"])
def add_exercise(w_id, e_id):
    data = request.get_json()

    we = WorkoutExercise(
        workout_id=w_id,
        exercise_id=e_id,
        reps=data.get("reps"),
        sets=data.get("sets"),
        duration_seconds=data.get("duration_seconds")
    )

    db.session.add(we)
    db.session.commit()

    return {"message": "Exercise added to workout"}, 201


if __name__ == "__main__":
    app.run(debug=True)