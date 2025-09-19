# INF601 - Advanced Programming in Python
# Jeff Johnson
# Mini Project 2

#Please submit a link to your GitHub project. Do not submit your project files here!
#This project will be using Pandas dataframes. This isn't intended to be full blown data science project. The goal here is to come up with some question and then see what API or datasets you can use to get the information needed to answer that question.

# ✓(5/5 points) Initial comments with your name, class and project at the top of your .py file.
# ✓(5/5 points) Proper import of packages used.
# ✓(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
# "How many BMW M3s were sold in North America?"
# "How many BMW M3s were in North America were automatics?"
# ✓(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# ✓(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# ✓(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# ✓(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# ✓(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.
# pip install pandas
# pip install kagglehub
# pip install kagglehub[pandas-datasets]
# pip install matplotlib
# pip freeze > requirements.txt

#Import needed packages
import pandas as pd
import kagglehub
from pathlib import Path
import shutil
import os
import matplotlib.pyplot as plt

#Declare functions
def save_chart(chart_title):
    #Save chart
    outfile = output_directory / f"{chart_title}.png"
    plt.savefig(outfile)
    plt.show()

def plot_barh(col_names: object, values: object,  plot_title: str, plot_xaxis_title: str, plot_yaxis_title: str, color: object, hatch: object, edgecolor: str = "Black", linewidth: float = 1):
    #Plot model data to a graph
    plt.barh(col_names, values, color=color, hatch=hatch, edgecolor=edgecolor, linewidth=linewidth)
    #Add title to chart
    plt.title(plot_title)
    #Add label to X axis
    plt.xlabel(plot_xaxis_title)
    #Add label to Y axis
    plt.ylabel(plot_yaxis_title)
    plt.tight_layout()

def plot_bar(col_names: object, values: object, plot_title: str, plot_xaxis_title: str, plot_yaxis_title: str, color: object, edgecolor: str = "Cyan", linewidth: float = 5):
    #Plot model data to a graph
    plt.bar(col_names, values, color=color, edgecolor=edgecolor, linewidth=linewidth)
    #Add title to chart
    plt.title(plot_title)
    #Add label to X axis
    plt.xlabel(plot_xaxis_title)
    #Add label to Y axis
    plt.ylabel(plot_yaxis_title)
    plt.tight_layout()

#Initialize variables
bmw_sales_data = ['Models','Colors','Transmissions']

#Initialize project root, and data and charts output directories
project_root = Path().resolve()
output_directory = project_root / "charts"
data_directory = project_root / "data"
os.environ['KAGGLEHUB_CACHE'] = str(data_directory)

#Create output_directory
if not output_directory.exists():
    #Create output directory
    output_directory.mkdir(parents=True, exist_ok=True)
else:
    #Remove output directory
    shutil.rmtree(output_directory)
    #Create output directory
    output_directory.mkdir(parents=True, exist_ok=True)

#Create data_directory
if not data_directory.exists():
    #Create data directory
    data_directory.mkdir(parents=True, exist_ok=True)
else:
    #Remove data directory
    shutil.rmtree(data_directory)
    #Create data directory
    data_directory.mkdir(parents=True, exist_ok=True)

#Download latest dataset version
file_path = Path(kagglehub.dataset_download("eshummalik/bmw-sales-dataset", force_download=True))

print("Downloading dataset to:", file_path)

for file in file_path.rglob("*.csv"):

    print("Processing Dataset:", file.name)

    #Create dataset from csv file
    df = pd.read_csv(str(file_path / file.name))
    #print(df.head())

    for item in bmw_sales_data:
        if item == "Models":
            #Set plot labels
            title = "BMW Models"
            xaxis_title = "Count"
            yaxis_title = "Models"

            #Set plot data
            models = df[["Model"]].value_counts()
            seven_series = models["7 Series"]
            i3 = models["i3"]
            i8 = models["i8"]
            three_series = models["3 Series"]
            five_series = models["5 Series"]
            x1 = models["X1"]
            x3 = models["X3"]
            x5 = models["X5"]
            m5 = models["M5"]
            x6 = models["X6"]
            m3 = models["M3"]

            #Call plot_barh function
            plot_barh(["3 series", "5 series", "7 series", "i3", "i8", "x1", "x3", "x5", "x6", "m3", "m5"],
                      [int(three_series), int(five_series), int(seven_series), int(i3), int(i8), int(x1), int(x3), int(x5), int(x6), int(m3), int(m5)],
                      title,
                      xaxis_title,
                      yaxis_title,
                      color=['g', 'm', 'b', 'g', 'm', 'b', 'g', 'm', 'b', 'g', 'm'],
                      hatch="|",
                      edgecolor="Black",)

            #Call save_chart function
            save_chart(title)

        if item == "Colors":
            #Set plot labels
            title = "BMW Colors"
            xaxis_title = "Colors"
            yaxis_title = "Count"

            #Set plot data
            colors = df[["Color"]].value_counts()
            red = colors["Red"]
            silver = colors["Silver"]
            grey = colors["Grey"]
            white = colors["White"]
            black = colors["Black"]
            blue = colors["Blue"]

            #Call plot_bar function
            plot_bar(["Red", "Silver", "Grey", "White", "Black", "Blue"],
                    [red, silver, grey, white, black, blue],
                    title,
                    xaxis_title,
                    yaxis_title,
                    color=['c', 'b', 'k', 'c', 'b', 'k'])

            #Call save_chart function
            save_chart(title)

        if item == "Transmissions":
            #Set plot labels
            title = "BMW Transmissions"
            xaxis_title = "Count"
            yaxis_title = "Transmission"

            #Set plot data
            transmissions = df[["Transmission"]].value_counts()
            automatic = transmissions["Automatic"]
            manual = transmissions["Manual"]

            #Call plot_barh function
            plot_barh(["Automatic", "Manual"],
                      [automatic, manual],
                      title,
                      xaxis_title,
                      yaxis_title,
                      color=['y', 'w'],
                      hatch="x")

            #Call save_chart function
            save_chart(title)

print("Exiting now...")