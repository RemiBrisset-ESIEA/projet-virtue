from flask import request, jsonify
from app.models import db, User, Car, Booking
from datetime import date

def register_routes(app):
    # Route pour récupérer toutes les voitures
    @app.route('/cars', methods=['GET'])
    def get_cars():
        cars = Car.query.all()
        return jsonify([{
            "id": car.id,
            "model": car.model,
            "price_per_day": car.price_per_day,
            "available": car.available
        } for car in cars])

    # Route pour ajouter une nouvelle voiture
    @app.route('/cars', methods=['POST'])
    def add_car():
        data = request.json
        car = Car(model=data['model'], price_per_day=data['price_per_day'])
        db.session.add(car)
        db.session.commit()
        return jsonify({"message": "Car added successfully"}), 201

    # Route pour réserver une voiture
    @app.route('/bookings', methods=['POST'])
    def book_car():
        data = request.json
        car = Car.query.get(data['car_id'])
        if car and car.available:
            booking = Booking(
                user_id=data['user_id'], 
                car_id=data['car_id'], 
                booking_date=date.today()
            )
            car.available = False
            db.session.add(booking)
            db.session.commit()
            return jsonify({"message": "Car booked successfully"}), 201
        return jsonify({"error": "Car not available"}), 400