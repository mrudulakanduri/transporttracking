from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transport.db'
db = SQLAlchemy(app)

# Database Model
class LocationUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/update-location', methods=['POST'])
def update_location():
    data = request.json
    update = LocationUpdate(
        vehicle_id=data['vehicle_id'],
        latitude=data['latitude'],
        longitude=data['longitude']
    )
    db.session.add(update)
    db.session.commit()
    return jsonify({"status": "success"}), 201

@app.route('/locations', methods=['GET'])
def get_locations():
    latest_locations = {}
    updates = LocationUpdate.query.order_by(LocationUpdate.timestamp.desc()).all()
    for u in updates:
        if u.vehicle_id not in latest_locations:
            latest_locations[u.vehicle_id] = {
                "latitude": u.latitude,
                "longitude": u.longitude,
                "timestamp": u.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
    return jsonify(latest_locations)

if __name__ == '__main__':
    app.run(debug=True)
