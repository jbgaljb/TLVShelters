from flask import Flask, render_template
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Define the path to your CSV file
    file_path = os.path.join(os.path.dirname(__file__), 'sheltersCSV.csv')
    
    # Load the CSV file into a pandas DataFrame, and then to json which is served
    df = pd.read_csv(file_path)
    locations = df.to_json
    return locations

if __name__ == '__main__':
    app.run()
