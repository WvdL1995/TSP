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
