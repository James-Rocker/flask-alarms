from flask import Flask, jsonify, request

from modules.entities import Session, engine, Base
from modules.alarm import Alarms, AlarmSchema

# creating the Flask application
app = Flask(__name__)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/alarms')
def get_alarms():
    # fetching from the database
    session = Session()
    alarm_objects = session.query(Alarms).all()

    # transforming into JSON-serializable objects
    schema = AlarmSchema(many=True)
    alarms = schema.dump(alarm_objects)

    # serializing as JSON
    session.close()
    return jsonify(alarms)


@app.route('/alarms', methods=['POST'])
def add_exam():
    # mount alarm object
    posted_alarm = AlarmSchema(only=('importance', 'description')).load(request.get_json())
    alarm = Alarms(**posted_alarm, created_by="HTTP post request")

    # persist alarm
    session = Session()
    session.add(alarm)
    session.commit()

    # return created alarm
    new_exam = AlarmSchema().dump(alarm)
    session.close()
    return jsonify(new_exam), 201


if __name__ == '__main__':
    app.run()
