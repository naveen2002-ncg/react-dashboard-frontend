from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Naveen@localhost/dashboard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Home Route (Fixes 404 Error)
@app.route('/')
def home():
    return "Welcome to the Data Visualization API! Use /data to get the insights."

# Define Data Model
class Insight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intensity = db.Column(db.Integer, nullable=True)
    likelihood = db.Column(db.Integer, nullable=True)
    relevance = db.Column(db.Integer, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    country = db.Column(db.String(100), nullable=True)
    topics = db.Column(db.String(200), nullable=True)
    region = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)

# API Route to Fetch All Data
@app.route('/data', methods=['GET'])
def get_data():
    insights = Insight.query.all()
    data = [
        {
            "id": i.id,
            "intensity": i.intensity,
            "likelihood": i.likelihood,
            "relevance": i.relevance,
            "year": i.year,
            "country": i.country,
            "topics": i.topics,
            "region": i.region,
            "city": i.city
        }
        for i in insights
    ]
    return jsonify(data)

# Run the Flask API
if __name__ == '__main__':
    app.run(debug=True)
