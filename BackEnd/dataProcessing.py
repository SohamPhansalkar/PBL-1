import pandas as pd
import re
from dateutil import parser
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import numpy as np

fileName = './DataSets/dataSet1.xlsx'
fileNameCleaned = "./DataSets/dataSet1_cleaned.xlsx"

mainDf = pd.read_excel(fileName)
try:
    mainDfCleaned = pd.read_excel(fileNameCleaned)
except:
    mainDfCleaned = mainDf.copy() 

def getHeadders():
    df = pd.read_excel(fileName, nrows=0)
    for i in df.columns.tolist():
        print(i)

def standardize_date(date_val):
    date_str = str(date_val).strip()
    if date_str == 'nan' or not date_str:
        return None
    date_str = date_str.replace(',', '')
    date_str = re.sub(r'(\d{4})s', r'\1', date_str)
    try:
        clean_str = re.sub(r'[()]', '', date_str)
        dt = parser.parse(clean_str, default=datetime(2000, 1, 1)) 
        return dt.strftime('%d-%m-%Y')
    except:
        if re.match(r'^\d{4}$', date_str):
            return f"01-01-{date_str}"
        return None

def cleanDate():
    mainDf['Project start date'] = mainDf['Project start date'].apply(standardize_date)
    mainDf['Project end date'] = mainDf['Project end date'].apply(standardize_date)
    mainDf.to_excel('dataSet1_cleaned.xlsx', index=False)
    print("File saved successfully as dataSet1_cleaned.xlsx")

def getAllCountriesList():
    countries = mainDfCleaned['Country'].dropna().astype(str).str.strip().unique().tolist()
    countries.sort()
    return countries

def getAllMainCausesList():
    mainCauses = mainDfCleaned['Earthquake cause (main class)'].dropna().astype(str).str.strip().unique().tolist()
    mainCauses.sort() 
    return mainCauses

# --- Bar Charts ---

def plotCountryFrequencyBar():
    counts = mainDfCleaned['Country'].dropna().astype(str).str.strip().str.title().value_counts()
    mask = counts >= 5
    plot_data = counts[mask]
    others_count = counts[~mask].sum()
    if others_count > 0:
        plot_data = pd.concat([plot_data, pd.Series({'Others': others_count})])

    plt.figure(figsize=(12, 6))
    plot_data.sort_values(ascending=False).plot(kind='bar', color='#3498db', edgecolor='black')
    plt.title('Earthquake Occurrences by Country', fontsize=14)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('./Graphs/country_frequency_bar.png')
    print("Saved: ./Graphs/country_frequency_bar.png")

def plotMainCauseFrequencyBar():
    header = 'Earthquake cause (main class)'
    counts = mainDfCleaned[header].dropna().astype(str).str.strip().str.title().value_counts()
    mask = counts >= 5
    plot_data = counts[mask]
    others_count = counts[~mask].sum()
    if others_count > 0:
        plot_data = pd.concat([plot_data, pd.Series({'Others': others_count})])

    plt.figure(figsize=(12, 6))
    plot_data.sort_values(ascending=False).plot(kind='bar', color='#e67e22', edgecolor='black')
    plt.title('Earthquake Main Causes', fontsize=14)
    plt.xlabel('Main Cause', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('./Graphs/main_cause_frequency_bar.png')
    print("Saved: ./Graphs/main_cause_frequency_bar.png")

# --- Pie Charts (Fixed cmap error) ---

def plotCountryFrequencyPie():
    counts = mainDfCleaned['Country'].dropna().astype(str).str.strip().str.title().value_counts()
    mask = counts >= 10
    plot_data = counts[mask]
    others_count = counts[~mask].sum()
    if others_count > 0:
        plot_data = pd.concat([plot_data, pd.Series({'Others': others_count})])

    # Generate colors from colormap manually
    colors = cm.Spectral(np.linspace(0, 1, len(plot_data)))

    plt.figure(figsize=(12, 7))
    wedges, texts, autotexts = plt.pie(
        plot_data, autopct='%1.1f%%', startangle=140, pctdistance=0.85,
        colors=colors, wedgeprops={'width': 0.5, 'edgecolor': 'w'}
    )
    plt.legend(wedges, plot_data.index, title="Countries", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title('Distribution by Country', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('./Graphs/country_frequency_pie.png')
    print("Saved: ./Graphs/country_frequency_pie.png")

def plotMainCauseFrequencyPie():
    header = 'Earthquake cause (main class)'
    counts = mainDfCleaned[header].dropna().astype(str).str.strip().str.title().value_counts()
    mask = counts >= 10
    plot_data = counts[mask]
    others_count = counts[~mask].sum()
    if others_count > 0:
        plot_data = pd.concat([plot_data, pd.Series({'Others': others_count})])

    # Generate colors from colormap manually
    colors = cm.Set3(np.linspace(0, 1, len(plot_data)))

    plt.figure(figsize=(12, 7))
    wedges, texts, autotexts = plt.pie(
        plot_data, autopct='%1.1f%%', startangle=140, pctdistance=0.85,
        colors=colors, wedgeprops={'width': 0.5, 'edgecolor': 'w'}
    )
    plt.legend(wedges, plot_data.index, title="Causes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title('Distribution by Main Cause', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('./Graphs/main_cause_frequency_pie.png')
    print("Saved: ./Graphs/main_cause_frequency_pie.png")

# Execution
if __name__ == "__main__":
    plotCountryFrequencyBar()
    plotCountryFrequencyPie()
    plotMainCauseFrequencyBar()
    plotMainCauseFrequencyPie()