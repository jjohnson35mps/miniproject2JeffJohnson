# INF601 - Advanced Programming in Python
# Jeff Johnson
# Mini Project 1

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

#Import needed packages
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
from pathlib import Path
import shutil

#Initialize project root and charts output directory
project_root = Path().resolve()
output_directory = project_root / "charts"

if not output_directory.exists():
    #Create output directory
    output_directory.mkdir(parents=True, exist_ok=True)
else:
    #Remove output directory
    shutil.rmtree(output_directory)
    #Create output directory
    output_directory.mkdir(parents=True, exist_ok=True)

#Download latest dataset version
file_path = Path(kagglehub.dataset_download("eshummalik/bmw-sales-dataset", force_download=True))

#print("Path to dataset files:", file_path)

for file in file_path.rglob("*.csv"):
    print("Filename:", file.name)

    #Load a DataFrame with a specific version of a CSV
    df = kagglehub.dataset_load(
      KaggleDatasetAdapter.PANDAS,
      "eshummalik/bmw-sales-dataset",
      str(file.name),
    )

    #print(df.head(5))
    #print(df.info())
    #print(df.describe())
    #How many BMW M3s were sold in North America?
    #How many BMW M3s were automatics?
    print("Count:", df.groupby(['Model','Region']).count())
    print("Count:", df.groupby(['Model','Transmission']).count())
