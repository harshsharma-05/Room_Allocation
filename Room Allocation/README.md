# Digitalization of Hospitality Process

## Overview
This project aims to develop a web application for digitalizing the hospitality process in group accommodation settings, such as hostels. The application allows users to upload two CSV files: one containing group information and the other containing hostel information. Based on the uploaded data, the system allocates rooms ensuring that group members with the same ID stay together, adhering to hostel capacities, and accommodating boys and girls in their respective hostels.

## Project Structure
The project is structured as follows:
- **frontend/**: Contains HTML, CSS, and JavaScript for the user interface.
- **backend/**: Contains Python scripts using Flask for server-side logic.
  - **app.py**: Flask application handling file uploads and data processing.
  - **csv_handler.py**: Functions for parsing and handling CSV files.
  - **room_allocation.py**: Algorithm for room allocation based on specified criteria.
- **README.md**: Project documentation providing an overview, setup instructions, and usage details.

## Setup Instructions
1. Clone the repository.
2. Navigate to the `backend/` directory and install dependencies: `pip install flask`.
3. Run the Flask application: `python app.py`.
4. Access the application via `http://localhost:5000`.

## Usage
1. Open the web application in a browser.
2. Upload the group CSV file containing group information.
3. Upload the hostel CSV file containing hostel information.
4. Click on "Allocate Rooms" to process the uploaded files.
5. View the allocation result displayed on the screen.

## Dependencies
- Python 3.11.8
- Flask