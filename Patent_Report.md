# FORM 2
# THE PATENTS ACT, 1970
# (39 of 1970)
# &
# THE PATENTS RULES, 2003
# COMPLETE SPECIFICATION
# (See section 10 and rule 13)

## 1. TITLE OF THE INVENTION
**A DATA-DRIVEN SYSTEM AND METHOD FOR MONITORING, ANALYZING, AND VISUALIZING HUMAN-INDUCED SEISMIC ACTIVITIES**

## 2. APPLICANT(S)
1. **Name:** Tanmay Chandrashekhar Sheware
   **Nationality:** Indian
   **Address:** [User's Address to be inserted]

2. **Name:** Soham Prasad Phansalkar
   **Nationality:** Indian
   **Address:** [User's Address to be inserted]

## 3. PREAMBLE TO THE DESCRIPTION
The following specification particularly describes the invention and the manner in which it is to be performed.

---

## 4. DESCRIPTION

### FIELD OF THE INVENTION
The present invention relates generally to the field of geophysics and seismic data analysis. More specifically, the invention relates to a computer-implemented system and method for identifying, categorizing, and visualizing the effects of human-induced activities on earthquake occurrence.

### BACKGROUND OF THE INVENTION
Natural earthquakes are caused by the sudden release of energy in the Earth's lithosphere that creates seismic waves. However, an increasing number of seismic events are being attributed to human activities, a phenomenon known as "induced seismicity." Activities such as hydraulic fracturing (fracking), large-scale mining, reservoir-induced seismicity (due to dam construction), and geothermal energy extraction can significantly destabilize the Earth's crust.

By injecting high-pressure fluids into the subsurface or removing massive amounts of rock, human activities inadvertently lubricate fault lines or alter stress distributions. Current seismic monitoring systems often focus on natural events and lack a centralized, user-friendly platform specifically designed to correlate and visualize the distribution of earthquakes triggered by specific industrial projects. There is a need for a system that can ingest diverse datasets, clean inconsistent metadata, and provide clear analytical insights into the geographic and causal distribution of human-induced earthquakes.

### OBJECTS OF THE INVENTION
The primary object of the present invention is to provide a system that can quantitatively analyze the impact of various human activities on earthquake occurrences.
Another object of the invention is to provide an automated data-cleaning module that standardizes inconsistent date and location formats in seismic records.
Yet another object of the invention is to provide a visualization dashboard that offers both geographic and causal perspectives on induced seismicity through dynamically generated charts.

### SUMMARY OF THE INVENTION
The present invention provides a software framework (referred to as "EcoPulse") comprising a backend processing engine and a frontend visualization layer. The system is designed to:
1. Ingest raw seismic datasets containing information about project-related seismic events.
2. Automatically clean and standardize metadata, specifically handling inconsistent date formats and geographic markers using regular expression-based algorithms.
3. Categorize seismic events based on their "Main Cause," such as Mining, Fracking, Reservoir-induced seismicity, etc.
4. Generate comparative visualizations, including frequency bar charts and distribution pie charts, to illustrate global trends.
5. Provide a secure, web-based interface with user authentication for authorized researchers and environmental agencies to access these insights.

### BRIEF DESCRIPTION OF THE DRAWINGS
The features of the present invention will become more fully apparent from the following description, taken in conjunction with the accompanying graphical outputs:
- **Figure 1:** A Bar Chart illustrating the frequency of human-induced earthquakes across different countries.
- **Figure 2:** A Pie Chart showing the percentage distribution of seismic events categorized by their primary human-induced cause.
- **Figure 3:** A screenshot of the web-based dashboard showing the integrated visualization interface.

### DETAILED DESCRIPTION OF THE INVENTION
The invention is implemented using a modular architecture comprising a Data Ingestion Module, a Cleaning and Standardization Module, a Statistical Processing Module, and a Visualization Layer.

**1. Data Ingestion and Storage:**
The system utilizes a data ingestion module configured to read structured data files (such as .xlsx or .csv). In the preferred embodiment, the system processes a dataset containing columns for "Project start date," "Project end date," "Country," and "Earthquake cause (main class)."

**2. Cleaning and Standardization Module:**
A critical component of the invention is the automated cleaning module. It employs regular expressions to identify and extract year and date components from inconsistent strings (e.g., handling "1970s", bracketed dates, and varied separators). The module standardizes all dates into a uniform DD-MM-YYYY format using a parser that defaults to a specific epoch for incomplete entries, ensuring temporal consistency across the dataset.

**3. Statistical Processing and Categorization:**
The system uses high-performance data structures (such as Pandas DataFrames) to aggregate seismic occurrences. It categorizes events by their "Main Cause" and "Country." It also implements threshold-based filtering (e.g., grouping countries with fewer than 5 occurrences into an "Others" category) to ensure the clarity of the resulting visualizations.

**4. Visualization Engine:**
The visualization module utilizes plotting libraries (such as Matplotlib and NumPy) to generate high-resolution PNG images. It maps counts to specific colormaps (e.g., 'Spectral', 'Set3') to provide visually distinct segments for different causes and regions.

**5. Web Interface and Security:**
The backend is powered by a FastAPI framework, providing RESTful endpoints for the frontend. A secure authentication module (User.py) manages user registrations and logins, employing encryption for password storage to protect sensitive research data.

---

## 5. CLAIMS
**We Claim:**

1. A computer-implemented system for monitoring and analyzing human-induced seismic activities, the system comprising:
   a) a data ingestion module configured to receive seismic event records from external data sources;
   b) a cleaning and standardization module that utilizes regular expression patterns to transform inconsistent date strings and geographic labels into a standardized format;
   c) a statistical processing engine configured to categorize said records based on human-induced triggers; and
   d) a visualization module configured to generate high-resolution graphical representations of the distribution of seismic activities.

2. The system as claimed in claim 1, wherein the cleaning and standardization module is configured to handle varied date formats including decade-based strings and bracketed notations, converting them into a uniform DD-MM-YYYY format.

3. The system as claimed in claim 1, wherein the visualization module generates both frequency-based bar charts and percentage-based pie charts for multi-dimensional analysis of seismic triggers.

4. The system as claimed in claim 1, wherein the statistical processing engine includes a threshold-filtering mechanism that aggregates low-frequency occurrences into a consolidated category to enhance visualization clarity.

5. The system as claimed in claim 1, wherein the system further comprises a secure web dashboard providing authenticated access to the generated seismic insights and visualizations.

---

## 6. ABSTRACT
**A DATA-DRIVEN SYSTEM AND METHOD FOR MONITORING, ANALYZING, AND VISUALIZING HUMAN-INDUCED SEISMIC ACTIVITIES**

The present invention provides a method and system for analyzing the impact of human activities on earthquake occurrences. By processing large datasets of seismic events and correlating them with specific human projects (such as mining, fracking, and reservoir construction), the system provides clear visualizations of geographic and causal distributions. The system includes an automated data-cleaning module for standardizing inconsistent metadata and a secure web interface for data dissemination. The invention aids in seismic risk assessment and assists environmental policy-makers in understanding the anthropogenic influences on geological stability.
