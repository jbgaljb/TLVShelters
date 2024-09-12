from flask import Flask
import os
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/')
def index():
    # Define the path to your CSV file (commented out - local context)
    file_path = os.path.join(os.path.dirname(__file__), 'sheltersCSV.csv')
    # file_path = os.path.join(r'C:\Users\galre\Documents\jhonBrice\sheltersProj\backend', 'sheltersCSV.csv')
    
    # Load the CSV file into a pandas DataFrame, and then to json which is served
    df = pd.read_csv(file_path)
    locations = df.to_json(orient='records')
    return locations

if __name__ == '__main__':
    app.run()
