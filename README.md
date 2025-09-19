### INF601 - Advanced Programming in Python
### Jeff Johnson
### Mini Project 2
 
 
## Mini Project 2
 
Mini Project 2 downloads a BMW sales dataset via KaggleHub, then loads each CSV into a Pandas DataFrame.
The script aggregates counts for models, colors, and transmissions and plots them using Matplotlib.
 
## Description
 
The program downloads BMW sales data with KaggleHub, refreshes its local data/ and charts/ folders, and loads each CSV into a DataFrame. It totals models, colors, and transmissions, then creates clear bar charts (horizontal for models/transmissions, vertical for colors) and saves them as PNGs in charts folder.

## Getting Started
 
### Dependencies
 
- Python 3.13.7
- Operating System: 
    - Windows
    - macOS
    - Linux
- Required libraries (install with pip):
```
pip install pandas
pip install kagglehub
pip install kagglehub[pandas-datasets]
pip install matplotlib
```

## Installing
 
1. Clone or download this project to your local machine.
2. Ensure you have the required dependencies listed above installed.
3. Running main.py will automatically create the charts and data folders if they don’t already exist.
 
## Executing program
 
1. Navigate to the project directory.
2. Run the Python script:
```
python main.py
```
 
## Help
 
If you encounter issues with missing modules, re-run pip installs:
```
pip install -r requirements.txt
```
 
## Authors
 
Jeff Johnson
 
## Version History
 
- 0.1
  - Initial Release
 
## License
 
This project is licensed under the MIT License - see the LICENSE.md file for details
 
## Acknowledgments
 
Inspiration, code snippets, etc.
- [Matplotlib Documentation](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html)
- [kagglehub Documentation](https://github.com/Kaggle/kagglehub/tree/main)
- [kagglehub cache Documentation](https://github.com/Kaggle/kagglehub#change-the-default-cache-folder)
- [shutil Documentation](https://docs.python.org/3/library/shutil.html)
- [pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [os Documentation](https://docs.python.org/3/library/os.html)
