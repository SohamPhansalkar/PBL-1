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
The features of the present invention will become more fully apparent from the following description and appended claims, taken in conjunction with the accompanying drawings. In the drawings, like numerals represent like components throughout the several views:
- **FIG. 1** is a block diagram illustrating the high-level system architecture, showing the interconnection between multiple user devices (106-1 through 106-n) and the backend infrastructure (100) via a network (104);
- **FIG. 2** is a schematic diagram illustrating the component interaction flow from the frontend web interface to the database, including API communication layers;
- **FIG. 3** is a block diagram detailing the data processing and storage architecture, specifically the utilization of datasets during the automated processing phase;
- **FIG. 4** is a graphical representation in the form of a bar chart illustrating the frequency of human-induced earthquakes across different geographic regions; and
- **FIG. 5** is a graphical representation in the form of a pie chart showing the percentage distribution of seismic events categorized by their primary human-induced cause.

### DETAILED DESCRIPTION OF THE INVENTION
The invention is implemented using a modular architecture comprising a Data Ingestion Module, a Cleaning and Standardization Module, a Statistical Processing Module, and a Visualization Layer.

**1. System Architecture (FIG. 1 and FIG. 2):**
Referring to FIG. 1, the high-level architecture includes a plurality of user devices (106-1, 106-2, ..., 106-n) connected via a communication network (104) to the backend infrastructure (100). As illustrated in FIG. 2, the interaction flow moves from the web interface and frontend components through API calls to the backend and eventually to the database, ensuring seamless data communication across the system.

**2. Data Ingestion, Storage, and Processing (FIG. 3):**
Referring to FIG. 3, the system utilizes a data ingestion and processing module configured to handle structured seismic datasets. The backend processes the "Data Set" (108) and commits results to the database (112). In the preferred embodiment, the system processes datasets containing "Project start date," "Project end date," "Country," and "Earthquake cause."

**3. Cleaning and Standardization Module:**
A critical component of the invention is the automated cleaning module. It employs regular expressions to identify and extract year and date components from inconsistent strings (e.g., handling "1970s", bracketed dates, and varied separators). The module standardizes all dates into a uniform DD-MM-YYYY format, ensuring temporal consistency.

**4. Statistical Processing and Categorization:**
The system uses high-performance data structures to aggregate seismic occurrences. It categorizes events by "Main Cause" and "Country" and implements threshold-based filtering to group low-frequency occurrences into an "Others" category, enhancing clarity in FIG. 4 and FIG. 5.

**5. Visualization Engine (FIG. 4 and FIG. 5):**
The visualization module utilizes plotting libraries to generate graphical representations of the data. FIG. 4 depicts a frequency bar chart of seismic occurrences by region, while FIG. 5 illustrates the percentage distribution of causes in a pie chart format, enabling multi-dimensional analysis.

**6. Web Interface and Security:**
The backend is powered by a FastAPI framework. A secure authentication module (User.py) manages registrations and logins, employing encryption to protect sensitive data.

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
