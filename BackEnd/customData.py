import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def process_custom_dataset(file_path, safe_email):
    """
    Processes the custom dataset and generates graphs.
    Saves them in Graphs/CustomGraphs/{safe_email}_{country}
    """
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise Exception(f"Failed to read Excel file: {str(e)}")

    # Clean column names (strip whitespace)
    df.columns = [c.strip() for c in df.columns]

    # Required fields mapping (to handle minor variations)
    # Looking for: Country, Earthquake Cause (Main), Earthquake Cause (Sub-class)
    target_cols = {
        'country': ['Country', 'country'],
        'main_cause': [
            'Earthquake Cause (Main)', 
            'Earth Quake Cause (Main)',
            'Main Cause', 
            'cause (main)', 
            'Earthquake cause (main class)'
        ],
        'sub_cause': [
            'Earthquake Cause (Sub-class)', 
            'Earth Quake Cause (Sub-Class)',
            'Sub-class Cause', 
            'cause (sub-class)', 
            'Earthquake cause (subclass)'
        ]
    }

    # Column name mapping
    mapping = {}
    for key, variants in target_cols.items():
        found = False
        for col in df.columns:
            if col.strip().lower() in [v.lower() for v in variants]:
                mapping[key] = col
                found = True
                break
        if not found:
            # Check for generic Fallbacks if specific columns aren't found
            # This makes the tool more robust to different Excel exports
            raise Exception(f"Missing required column: {variants[0]}. Found columns: {list(df.columns)}")

    countries = df[mapping['country']].dropna().unique().tolist()
    print(f"DEBUG: Countries found: {countries}")
    
    # Base directory using absolute path to be sure
    base_graphs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Graphs", "CustomGraphs")
    os.makedirs(base_graphs_dir, exist_ok=True)
    print(f"DEBUG: Saving all graphs into: {base_graphs_dir}")

    for country in countries:
        # Sanitize country name
        safe_country = str(country).replace("/", "_").replace("\\", "_").strip()
        folder_name = f"{safe_email}_{safe_country}"
        save_dir = os.path.join(base_graphs_dir, folder_name)
        os.makedirs(save_dir, exist_ok=True)

        # Filter data for this country
        country_df = df[df[mapping['country']] == country]

        # 1. Main Cause Frequency Bar Plot
        plt.figure(figsize=(10, 6))
        sns.countplot(y=mapping['main_cause'], data=country_df, hue=mapping['main_cause'], palette='viridis', legend=False)
        plt.title(f"Main Cause Distribution - {country}")
        plt.xlabel("Frequency")
        plt.ylabel("Cause")
        plt.tight_layout()
        plt.savefig(os.path.join(save_dir, f"{safe_country}_main_cause.png"))
        plt.close()

        # 2. Sub-Cause Frequency Bar Plot
        plt.figure(figsize=(12, 8))
        sns.countplot(y=mapping['sub_cause'], data=country_df, hue=mapping['sub_cause'], palette='magma', legend=False)
        plt.title(f"Sub-class Cause Distribution - {country}")
        plt.xlabel("Frequency")
        plt.ylabel("Sub-class")
        plt.tight_layout()
        plt.savefig(os.path.join(save_dir, f"{safe_country}_sub_cause.png"))
        plt.close()

    return countries
