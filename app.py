from flask import Flask, render_template
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Define the path to your CSV file
    file_path = os.path.join(os.path.dirname(__file__), 'sheltersCSV.csv')
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    locations = df.to_json
    print(locations)

    # Display the DataFrame
    # print(locations)
    # return render_template('index.html', locations = locations)
    print("hello world")

if __name__ == '__main__':
    app.run()
