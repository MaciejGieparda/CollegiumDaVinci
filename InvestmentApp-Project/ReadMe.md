# InvestmentApp Project

## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#project-motivation)
3. [File Descriptions](#file-descriptions)
4. [Interaction](#interaction)
5. [Author](#author)

### Installation <a name="installation"></a>

To get this project up and running locally, you'll need to follow these steps:

**Libraries:**
This application is written in Python and requires Python 3.8 or above. The necessary libraries are listed in the `requirements.txt` file. They can be installed by running the following command:


pip install -r requirements.txt

**Tools:**  
- Flask: A lightweight WSGI web application framework.
- Pandas: A fast, powerful, flexible and easy to use open source data analysis and manipulation tool.
- Plotly: A graphing library makes interactive, publication-quality graphs online.

### Project Motivation <a name="project-motivation"></a>
The InvestmentApp is designed to provide users with an interactive platform to explore stock data. The motivation behind this project is to make stock data more accessible and understandable for users with any level of investment experience.

### File Descriptions <a name="file-descriptions"></a>
- `app.py`: The main file that runs the Flask application and contains the routing logic.
- `api_connection.py`: Handles the connection to the stock information API and retrieves data.
- `data_processing.py`: Contains functions to process data and prepare it for visualization.
- `stock_prediction.py`: Implements stock prediction algorithms.
- `utils.py`: Helper functions used across the application.
- `templates/`: Directory containing HTML templates for the application's frontend.
- `requirements.txt`: Required libraries for the project to run.
- `symbols.csv`: The dataset containing symbols information.

### Interaction <a name="interaction"></a>
To run the application, use the following command:

python app.py

Once the server starts, you can visit `http://127.0.0.1:5000/` in your web browser to interact with the application.

### Author <a name="author"></a>
The InvestmentApp was developed by Maciej Gieparda. Feel free to contact me at maciej.gieparda@gmail.com for any questions or feedback regarding this project.
