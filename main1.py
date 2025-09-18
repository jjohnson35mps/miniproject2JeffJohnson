# INF601 - Advanced Programming in Python
# Jeff Johnson
# Mini Project 2
import numpy as np
#Please submit a link to your GitHub project. Do not submit your project files here!
#This project will be using Pandas dataframes. This isn't intended to be full blown data science project. The goal here is to come up with some question and then see what API or datasets you can use to get the information needed to answer that question.

# ✓(5/5 points) Initial comments with your name, class and project at the top of your .py file.
# ✓(5/5 points) Proper import of packages used.
# ✓(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
# "How many BMW M3s were sold in North America?"
# "How many BMW M3s were in North America were automatics?"
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.
# pip install pandas
# pip install kagglehub
# pip install kagglehub[pandas-datasets]
# pip install matplotlib
# pip freeze > requirements.txt
#https://github.com/Kaggle/kagglehub
#https://docs.python.org/3/library/pathlib.html

#Import needed packages
import pandas as pd
import kagglehub
from pathlib import Path
import shutil
import os
import matplotlib.pyplot as plt

#Initialize variables
bmw_sales_data = ['Models','Colors','Transmissions']

#Initialize project root and data and charts output directories
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

    #print(df.info())
    #print(df.describe())

    #Create dataset from csv file
    df = pd.read_csv(str(file_path / file.name))

    models = df[["Model"]].value_counts()
    #print(models)
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

    #Plot model data to a graph
    plt.barh(["3 series", " 5 series", "7 series", "i3", "i8", "x1", "x3", "x5", "x6", "m3", "m5"],[three_series, five_series, seven_series, i3, i8, x1, x3, x5, x6, m3, m5], color= ['r','m','b','r','m','b','r','m','b','r','m'])
    #Add title to chart
    plt.title("BMW Models")
    #Add label to X axis
    plt.xlabel('Count')
    #Add label to Y axis
    plt.ylabel('Models')
    plt.tight_layout()

    #Save chart
    file_name = bmw_sales_data[0]
    outfile = output_directory / f"{file_name}.png"
    plt.savefig(outfile)

    plt.show()

    years = df[["Year"]].value_counts()
    colors = df[["Color"]].value_counts()
    regions = df[["Region"]].value_counts()
    transmissions = df[["Transmission"]].value_counts()

    #print(df.head(5))
    #print(df.info())
    #print(df.describe())

    #How many BMW M3s were sold in North America?
    #How many BMW M3s were automatics?
    #print(models["M3"])
