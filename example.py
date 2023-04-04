# You can use the provided functions
# These can be used to generate additional data
# As well as testing the file for hand in, as shown below

from TSPfunctions.functions import *

# Load in the data, from a csv file
# if no argument is given, the load_data function automatically opens
# the challenge dataset
data = load_data()

# the final ordered list should contain the names of the cities/ locations
# use the following line to load the faculty names 
citynames = [line.strip() for line in open('data/citynames.txt','r')]

# using the "totaltime" functions we can calculat the total time of our solution
order=citynames.copy()
order.append(citynames[0]) #remember that the starting city should be the final city as well!
print("The solution has a total travel time of %d!" % totaltime(order))

# with the tran_time function the distance between two cities can be calculated
startcity=np.random.choice(citynames)
endcity=np.random.choice(citynames)
print("The distance between %s and %s is %d!" % (startcity,endcity,tran_time(startcity,endcity)))

# example implementation
# This example is based brute force random search which is a terrible idea and will not win you anything xD

best_order = order #as calculated before
best_sol = totaltime(order) # to initialize
ordered = citynames[1:].copy()

for i in range(100):
    # Create random order
    np.random.shuffle(ordered)
    
    # Add start and endlocation
    order=[]
    order.append(citynames[0])
    order.extend(ordered[:])
    order.append(citynames[0])
    sol_val = totaltime(order)
    if sol_val < best_sol:
        print("New best solution found: %d" % sol_val)
        best_sol=sol_val
        best_order = order.copy()

print("The solution has a total travel time of %d!" % totaltime(best_order))

# Don't forget to save your solution
save_solution(best_order)

# to evaluate your score we will use the following approach
# please ensure this works for your solution file (the name of the final is not important)
solution = [line.strip() for line in open('solution.txt','r')]
print("This solution has an optimal value of %d!" % totaltime(solution))