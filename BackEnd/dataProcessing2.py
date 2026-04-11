import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

sns.set_theme(style="whitegrid")

FILE_NAME = '/home/soham/Desktop/Code/pbl-1/PBLFullStack/DataSets/dataSet1_cleaned.xlsx'
OUTPUT_DIR = '/home/soham/Desktop/Code/pbl-1/PBLFullStack/Graphs/Graphs2'

os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_data_and_generate_graphs():
    df = pd.read_excel(FILE_NAME)
    
    plt.figure(figsize=(15, 8))
    mmax_df = df.dropna(subset=['Observed maximum magnitude (Mmax)', 'Country'])
    mmax_df['Observed maximum magnitude (Mmax)'] = pd.to_numeric(mmax_df['Observed maximum magnitude (Mmax)'], errors='coerce')
    mmax_df = mmax_df.dropna(subset=['Observed maximum magnitude (Mmax)'])
    
    # Group by country and get the highest magnitude recorded
    country_mmax = mmax_df.groupby('Country')['Observed maximum magnitude (Mmax)'].max().sort_values(ascending=False).head(15)
    
    plt.subplot(1, 1, 1)
    sns.barplot(x=country_mmax.values, y=country_mmax.index, hue=country_mmax.index, palette='viridis', legend=False)
    plt.title('Top 15 Countries by Highest Observed Maximum Magnitude (Mmax)', fontsize=15)
    plt.xlabel('Maximum Magnitude (Mmax)', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'mmax_by_country.png'))
    plt.close()
    print(f"Saved: {os.path.join(OUTPUT_DIR, 'mmax_by_country.png')} - Shows maximum seismic intensity per country.")

    # 2. Relation: Depth of Magnitude (Mmax) vs Country
    # This graph illustrates the depth at which the strongest earthquakes occur across different countries.
    plt.figure(figsize=(15, 8))
    depth_df = df.dropna(subset=['Depth of Mmax (m)', 'Country'])
    # Convert depth to numeric and meters to kilometers for better readability
    depth_df['Depth of Mmax (km)'] = pd.to_numeric(depth_df['Depth of Mmax (m)'], errors='coerce') / 1000.0
    depth_df = depth_df.dropna(subset=['Depth of Mmax (km)'])
    
    # Take top 10 countries by record count to keep graph clean
    top_countries = df['Country'].value_counts().head(10).index
    depth_subset = depth_df[depth_df['Country'].isin(top_countries)]
    
    sns.boxplot(data=depth_subset, x='Country', y='Depth of Mmax (km)', hue='Country', palette='Set2', legend=False)
    plt.title('Depth Distribution of Strongest Earthquakes (Top 10 Countries)', fontsize=15)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Depth (km)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'depth_relation_country.png'))
    plt.close()
    print(f"Saved: {os.path.join(OUTPUT_DIR, 'depth_relation_country.png')} - Shows the depth distribution of Mmax events.")

    # 3. Individual Country Bar Graphs: Cause vs Frequency
    # This loop generates a bar graph for each country showing the distribution of earthquake causes.
    # Each graph is saved in a dedicated folder named after the country.
    countries = df['Country'].dropna().unique()
    
    for country in countries:
        # Filter data for the specific country
        country_df = df[df['Country'] == country]
        
        # Count causes for this country
        cause_counts = country_df['Earthquake cause (main class)'].dropna().value_counts()
        
        # Only create folder and plot if the country has MORE than one unique cause
        if len(cause_counts) > 1:
            # Sanitize country name for folder paths (remove slashes, etc.)
            safe_country_name = str(country).replace('/', '_').replace('\\', '_').strip()
            
            # Create country-specific directory
            country_dir = os.path.join(OUTPUT_DIR, safe_country_name)
            os.makedirs(country_dir, exist_ok=True)
            
            plt.figure(figsize=(12, 6))
            sns.barplot(x=cause_counts.index, y=cause_counts.values, hue=cause_counts.index, palette='viridis', legend=False)
            
            plt.title(f'Seismic Triggers in {country}', fontsize=15)
            plt.xlabel('Earthquake Cause (Main Class)', fontsize=12)
            plt.ylabel('Number of Events', fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            
            save_name = f"{safe_country_name}_cause_frequency.png"
            save_path = os.path.join(country_dir, save_name)
            plt.savefig(save_path)
            plt.close()

            # 4. Individual Country Bar Graphs: Earthquake cause (subclass) vs Frequency
            # Added as per user request to use "Earthquake cause (subclass)" which is often column C
            sub_cause_counts = country_df['Earthquake cause (subclass)'].dropna().value_counts()
            
            if not sub_cause_counts.empty:
                plt.figure(figsize=(12, 6))
                sns.barplot(x=sub_cause_counts.index, y=sub_cause_counts.values, hue=sub_cause_counts.index, palette='magma', legend=False)
                
                plt.title(f'Detailed Seismic Causes in {country}', fontsize=15)
                plt.xlabel('Earthquake Cause (Subclass)', fontsize=12)
                plt.ylabel('Number of Events', fontsize=12)
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                
                sub_save_name = f"{safe_country_name}_sub_cause_frequency.png"
                sub_save_path = os.path.join(country_dir, sub_save_name)
                plt.savefig(sub_save_path)
                plt.close()
            
            # print(f"Generated: {save_path}") # Commented out to prevent terminal spam
        else:
            # If it only has one cause, we don't need a graph or folder
            pass

if __name__ == "__main__":
    process_data_and_generate_graphs()
