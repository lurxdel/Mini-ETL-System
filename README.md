# Mini ETL System

This project is a web-based Extract, Transform, Load (ETL) pipeline built using the Django framework. It simulates a real-world data engineering process by taking raw CSV data, cleaning it, and loading it into a reporting database.

### Features
- **Data Extraction:** Seamlessly handles user-uploaded raw `.csv` data files.
- **Data Transformation:** Automatically cleans and maps missing or incomplete fields (e.g., assigning "Unknown Name" or "Unknown Course" to empty rows).
- **Database Loading:** Safely inserts the transformed data into a SQLite database using the `StudentReport` model.
- **Modern UI Dashboard:** Provides a beautifully styled, glassmorphism-themed frontend for users to upload files and view the fully processed records.

## Guide To Run
To run the system locally, do the following.
> - **Clone this repository** or download it as a **ZIP file.**
> - When cloning the repository, follow these steps.

### 1. Install Python
- You can get it from here. [Python.org](https://www.python.org/)

### 2. Setting up the Backend
Navigate to the backend directory and run the Django development server:

```bash
# Navigate to the correct directory containing manage.py
cd Mini-ETL-System

# (Optional but recommended) Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# Install the required frameworks for this project
pip install django

# Run the database migrations to set up the SQLite tables
python manage.py migrate

# Start the development server
python manage.py runserver
```

The application should now be running. Open your browser and go to `http://127.0.0.1:8000/`.

### 3. Available Pages
To interact with the ETL system, append any of the following to your localhost URL (or use the UI navigation):

- **Upload Dashboard (Extact & Transform):** `/etl/` - Upload your `students.csv` file here.
- **Results View (Reporting):** `/etl/success/` - View the cleaned records loaded into the database.

### Acknowledgment  
We are grateful to our instructors for their guidance and support throughout the development of this project. 

This work reflects my learning journey as a programmer.

## Disclaimer 
<div align="center"> 
  I do not own the images, names, information or references included in this project they are used purely as placeholders. <br> 
  All trademarks, service marks, trade names, and other intellectual property rights belong to their respective owners.  <br><br>

  Made with 💗 by <a href="https://github.com/lurxdel"><strong>Lurxdel</strong></a>
</div>
