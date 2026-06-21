# Import internal library
import codecademylib3

# 1
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load rankings data
GTAW_wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
print(GTAW_wood.head())

GTAW_steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
print(GTAW_steel.head())

# 2
# Create a function to plot rankings over time for 1 roller coaster
def ranking_over_time(name, material, park):
    if material == "wood":
        df = GTAW_wood
    else: 
        df = GTAW_steel
    
    name_df = df[(df.Name == name) & (df.Park == park)]
    x = name_df["Year of Rank"]
    y = name_df["Rank"]
    
    plt.plot(x, y)
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.title(f"{name} Ranking Over Time")
    plt.show()
    plt.clf()

# 3
# Create a plot of El Toro ranking over time
ranking_over_time("El Toro", "wood", "Six Flags Great Adventure")

# Create a plot of El Toro and Boulder Dash hurricanes
def compare_ranking_over_time(name1, name2, material, park1, park2):
    if material == "wood":
        df = GTAW_wood
    else: 
        df = GTAW_steel
    
    name1_df = df[(df.Name == name1) & (df.Park == park1)]
    name2_df = df[(df.Name == name2) & (df.Park == park2)]
    
    x1 = name1_df["Year of Rank"]
    y1 = name1_df["Rank"]
    x2 = name2_df["Year of Rank"]
    y2 = name2_df["Rank"]
    
    plt.plot(x1, y1, label=name1)
    plt.plot(x2, y2, label=name2)
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.title(f"{name1} vs {name2} Ranking Over Time")
    plt.legend()
    plt.show()
    plt.clf()

compare_ranking_over_time("El Toro", "Boulder Dash", "wood", "Six Flags Great Adventure", "Lake Compounce")

# 4
# Create a function to plot top n rankings over time
def top_n_coasters(n, df):
    df_filtered = df[df.Rank <= n]
    
    for coaster in set(df_filtered["Name"]):
        ranking = df_filtered[df_filtered["Name"] == coaster]
        plt.plot(ranking["Year of Rank"], ranking["Rank"], label=coaster)
    
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.title(f"Top {n} Roller Coasters Over Time")
    plt.legend()
    plt.show()
    plt.clf()

# Create a plot of top n rankings over time
top_n_coasters(5, GTAW_wood)

# 5
# Load roller coaster data
coasters_df = pd.read_csv("roller_coasters.csv")
print(coasters_df.head())

# 6
# Create a function to plot histogram of column values
def histogram(col, df):
    if col == "height":
        df = df[df.height <= 140]
    
    plt.hist(df[col].dropna())
    plt.xlabel(col)
    plt.ylabel("Number")
    plt.title(f"Histogram of {col}")
    plt.show()
    plt.clf()

# Create histogram of roller coaster speed
histogram("speed", coasters_df)

# Create histogram of roller coaster length
histogram("length", coasters_df)

# Create histogram of roller coaster number of inversions
histogram("num_inversions", coasters_df)

# Create a function to plot histogram of height values
def histogram_height(df):
    df_filtered = df[df.height <= 140]
    plt.hist(df_filtered["height"].dropna())
    plt.xlabel("Height")
    plt.ylabel("Number")
    plt.title("Histogram of Roller Coaster Height")
    plt.show()
    plt.clf()

# Create a histogram of roller coaster height
histogram_height(coasters_df)

# 7
# Create a function to plot inversions by coaster at park
def inversions(df, park):
    df_park = df[df["park"] == park]
    x_coaster_names = df_park["name"]
    y_inversions = df_park["num_inversions"]
    
    ax = plt.subplot()
    plt.bar(range(len(x_coaster_names)), y_inversions)
    ax.set_xticks(range(len(x_coaster_names)))
    ax.set_xticklabels(x_coaster_names, rotation=90)
    plt.ylabel("Inversions")
    plt.title(f"Inversions by Roller Coaster at {park}")
    plt.show()
    plt.clf()

# Create barplot of inversions by roller coasters
inversions(coasters_df, "Parc Asterix")

# 8
# Create a function to plot pie chart of status.operating
def num_operating_coasters(df):
    status = [
        len(df[df["status"] == "status.operating"]),
        len(df[df["status"] == "status.closed.definitely"])
    ]
    
    plt.pie(status, labels=["operating", "closed"], autopct="%0.2f%%")
    plt.axis("equal")
    plt.legend()
    plt.title("Roller Coaster Status")
    plt.show()
    plt.clf()

# Create pie chart of roller coasters
num_operating_coasters(coasters_df)

# 9
# Create a function to plot scatter of any two columns
def scatter(col1, col2, df):
    if (col1 == "height") | (col2 == "height"):
        df = df[df["height"] <= 140]
    
    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title(f"{col2} vs {col1}")
    plt.show()
    plt.clf()

# Create a function to plot scatter of speed vs height
def scatter_speed_height(df):
    df_filtered = df[df["height"] <= 140]
    plt.scatter(df_filtered["speed"], df_filtered["height"])
    plt.xlabel("Speed")
    plt.ylabel("Height")
    plt.title("Roller Coaster Height by Speed")
    plt.show()
    plt.clf()

# Create a scatter plot of roller coaster height by speed
scatter("speed", "height", coasters_df)
