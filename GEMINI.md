This is a full-stack web application for analyzing earthquake data.

**Front-end:**
- HTML, CSS, JavaScript
- Pages: `index.html` (landing), `LogIn.html`, `SignUp.html`, `Home.html` (dashboard)
- `style.css` for all pages.
- `script.js` for all pages.
- `Nav.html` and `Footer.html` are loaded dynamically.
- The dashboard in `Home.html` displays graphs of earthquake data.

**Back-end:**
- Python with FastAPI.
- `main.py` is the entry point.
- `User.py` handles user authentication (sign up, log in) with a MySQL database.
- `encrypt.py` handles password hashing.
- `dataProcessing.py` reads an Excel file, cleans the data, and generates graphs using Matplotlib.

**Data:**
- `DataSets/dataSet1.xlsx` is the raw data.
- `DataSets/dataSet1_cleaned.xlsx` is the cleaned data.
- `Graphs/` folder contains the generated graphs.

**User request:**
- Add a loading bar to `Home.html`.
- The loading bar should be visible for 2-3 seconds.
- After the loading time, the graphs should be displayed.
