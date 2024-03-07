""" A Flask application that provides access to dictionary and weather data APIs. """

from typing import Dict
from flask import Flask, render_template, request
import pandas as pd

# Initialize Flask application
app = Flask(__name__)

# Load station data from file and select relevant columns
stations = pd.read_csv("./data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

# Load dictionary data
dictionary_data = pd.read_csv("./dictionary/dictionary.csv", sep=",")


@app.route("/")
def home() -> str:
    """
    Render the home page.
    """
    return render_template("index.html")


@app.route("/api/v1/dictionary", methods=["GET"])
def get_definition() -> str:
    """
    Return the definition of a given word.

    Returns:
    str: A JSON string containing the word and its definition
    """
    word = request.args.get("word")
    definition = dictionary_data.loc[
        dictionary_data["word"] == word, "definition"
    ].values
    if len(definition) > 0:
        return {"word": word, "definition": definition[0]}
    else:
        return {"error": "Word not found in the dictionary."}


@app.route("/api/v1/weather", methods=["GET"])
def get_temperature() -> Dict[str, str]:
    """
    Return the temperature for a given station and date.

    Returns:
    dict: A dictionary containing the station ID, date, and temperature
    """
    station = request.args.get("station")
    date = request.args.get("date")
    file_path = "./data_small/TG_STAID{}.txt".format(station.zfill(6))

    try:
        df = pd.read_csv(file_path, skiprows=20, parse_dates=["    DATE"])
        temperature = df.loc[df["    DATE"] == date]["   TG"].values[0] / 10
        return {"station": station, "date": date, "temperature": str(temperature)}
    except FileNotFoundError:
        return {"error": "Data file for the station not found."}
    except IndexError:
        return {"error": "Temperature data not available for the specified date."}


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
