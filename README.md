### INF601 - Advanced Programming in Python
### Jeff Johnson
### Mini Project 1
 
 
## Mini Project 1
 
Mini Project 1 queries last 10 days of stock information for Apple, Draft King, Microsoft, Rubrik, and Tesla. It then creates graphs for each stock, plots the 10 stock prices over each day, and saves the charts to a folder called 'charts'.
 
## Description
 
The program pulls financial data from the yfinance API, processes arrays using NumPy, and plots charts with matplotlib. Each stock closing price for Apple, DraftKings, Microsoft, Rubrik, and Tesla are collected and scaled based on minimum and maximum values and plotted on a graph with X and Y axis labels and a title. The program ensures that a charts directory exists before saving the charts as .png files.
 
## Getting Started
 
### Dependencies
 
- Python 3.13.7
- Operating System: 
    - Windows
    - macOS
    - Linux
- Required libraries (install with pip):
```
pip install numpy
pip install matplotlib
pip install yfinance
```

## Installing
 
1. Clone or download this project to your local machine.
2. Ensure you have the required dependencies listed above installed.
3. Running main.py will automatically create the charts folder if it doesn’t already exist.
 
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
- [yfinance Documentation](https://ranaroussi.github.io/yfinance/)
- [shutil Documentation](https://docs.python.org/3/library/shutil.html)
