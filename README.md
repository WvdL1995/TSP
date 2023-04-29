# TSP
In data:
- An ordered list of 'cities' (citynames.txt) faculties of the tudelft
- A matrix of distance between all 'cities' (data_challenge.csv) use this file for the challenge!
- A second distance matrix as example (exampledata.csv). Thisone can be overwritten with the gen_data() function

In functions:
- totaltime(): calculates the total time given a route
- tran_time(): calculates/ selects traveltime between citystart and cityend
- gen_data(): generates a random distance matrix of given size
- load_data(): loads the csv data file
- save_solution(): saves the solution to a txt file

Additional files:
- example.py: a code example, check it out to see how the given functions can be used.
- solution.txt an example solution in the correct format. You can use this to benchmark your own method!
