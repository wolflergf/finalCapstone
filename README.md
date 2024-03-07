
# Flask Weather Station API

Welcome to the Flask Weather Station API! This application serves as a versatile tool that provides real-time temperature data for various weather stations alongside a handy dictionary API. Whether you're a weather enthusiast or need quick access to word definitions, this Flask app has got you covered!

## Key Features

- **Weather Station Information**: Access a comprehensive home page that showcases a curated list of weather stations.
- **Temperature Data Retrieval**: Utilize an API endpoint to fetch temperature data for a specific weather station and date.
- **Dictionary API**: A convenient endpoint to retrieve definitions for any word you're curious about.

## API Endpoints

- `GET /`: Retrieves the homepage displaying an array of weather stations.
- `GET /api/v1/station/<station_id>/<date>`: Fetches the temperature for a specified station and date. Here, `<station_id>` should be replaced with the station's ID and `<date>` with the desired date in YYYYMMDD format.
- `GET /api/v1/definition/<word>`: Provides the definition for the specified word. Replace `<word>` with the word you wish to define.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```bash
    git clone [repository-url]
    ```

2. **Install Dependencies**: Navigate to the cloned repository's directory and install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    This will install Flask and pandas, which are essential for the application to run.

3. **Launch the Application**: Start the server with the following command:

    ```bash
    python main.py
    ```

    Once the server is running, access the application via `http://localhost:5000` in your web browser.

## Data Sources

- **Weather Station Data**: Located at `./data_small/stations.txt`, this file includes IDs and names of various weather stations.
- **Temperature Data**: Stored in `./data_small/TG_STAID{}.txt`, where `{}` should be replaced with the station ID. Each file contains specific station temperature data.
- **Dictionary Data**: Found at `./dictionary/dictionary.csv`, this file lists words along with their respective definitions.

## Dependencies

- **Flask**: A minimalistic framework for building web applications in Python.
- **Pandas**: An extensive library providing high-performance, easy-to-use data structures and data analysis tools for Python.

## How to Contribute

Interested in contributing? We welcome contributions of all forms! Here's how you can help:

1. **Fork the Repository**: Create your own copy of the project to work on.
2. **Create a Feature Branch**: Make your changes in a new branch.
3. **Submit a Pull Request**: Once you've made your changes, submit a pull request to merge your changes with the main project.

## License

This project is licensed under [appropriate license type] - see the LICENSE.md file for details.

## Acknowledgments

- Thanks to all the contributors who have helped shape this project!
- Special thanks to [any special acknowledgments].