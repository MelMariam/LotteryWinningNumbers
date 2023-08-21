# whatIsThis
The goal of this project was to analyze and plot lottery winning numbers from csv file

This code defines a PowerballAnalyzer class that has 
methods for loading and processing data from a CSV file, 
saving the processed data to a SQLite3 database, 
and displaying the results in a chart using the matplotlib library.

The __init__ method is the constructor for the class, 
and it initializes the data_file and df instance variables. 
The data_file variable stores the path to the CSV file, and
 the df variable will store the data from the CSV file as a
 Pandas DataFrame once it is loaded.

The load_data method reads the data from the CSV file into
 a Pandas DataFrame and stores it in the df instance variable.

The process_data method converts the 'Date' column to datetime
 objects and adds a 'Month' column that stores the month of each date.
 It also converts the 'Winning Number' column to integers.

The save_to_database method saves the processed data to a SQLite3 
database using the to_sql method of the Pandas DataFrame.

The display_results method calculates the number of times each
 winning number was drawn in each month, and displays the results
 in a bar chart using the plot method of the Pandas DataFrame.

The run method ties everything together by calling the other methods
 in the correct order and handling any exceptions that may occur.

Finally, the code creates an instance of the PowerballAnalyzer class 
and calls the run method to execute the data analysis.
