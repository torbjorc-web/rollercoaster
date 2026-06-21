Roller Coaster Analysis
This project analyzes roller coaster rankings and coaster attributes using Python, pandas, and matplotlib.

Overview
The goal of this project is to explore two datasets:

Roller coaster rankings over time.

Roller coaster attributes such as speed, height, length, inversions, and status.

The analysis includes line charts, histograms, bar charts, pie charts, and scatter plots.

Files
Golden_Ticket_Award_Winners_Wood.csv: rankings for wooden roller coasters.

Golden_Ticket_Award_Winners_Steel.csv: rankings for steel roller coasters.

roller_coasters.csv: roller coaster attribute data.

script.py: the main Python analysis script.

Features
Plots ranking changes for individual roller coasters over time.

Compares rankings of two roller coasters.

Plots the top N roller coasters over time.

Creates histograms for coaster speed, length, inversions, and height.

Shows inversions by coaster at a specific park.

Displays a pie chart of operating vs. closed coasters.

Makes scatter plots for any two coaster features.

Requirements
Python 3

pandas

matplotlib

If you are running this inside Codecademy, codecademylib3 may already be available. If you are running locally, you may need to remove that import.

Installation
Install the required libraries with:

bash
pip install pandas matplotlib
How to Run
Download or place the CSV files in the same folder as the Python script.

Open a terminal in that folder.

Run the script:

bash
python script.py
Review the generated plots.

Example Usage
python
ranking_over_time("El Toro", "wood", "Six Flags Great Adventure")
compare_ranking_over_time("El Toro", "Boulder Dash", "wood", "Six Flags Great Adventure", "Lake Compounce")
top_n_coasters(5, GTAW_wood)
histogram("speed", coasters_df)
inversions(coasters_df, "Parc Asterix")
num_operating_coasters(coasters_df)
scatter("speed", "height", coasters_df)
Notes
Some plots
