from flask import Flask
from flask_cors import CORS
from src.models.settings.connections import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

from src.main.routes.events_routes import event_route_bp
app.register_blueprint(event_route_bp)
from src.main.routes.attendees_routes import attendee_route_bp
app.register_blueprint(attendee_route_bp)
from src.main.routes.check_in_routes import check_in_bp
app.register_blueprint(check_in_bp)