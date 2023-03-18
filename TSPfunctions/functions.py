# functions
import numpy as np

def totaltime(order,data=None,citynames=None):
    """Calculates time the total travelling time.
    Takes three arguments;
      order, a list with your solution 
      data (Optioneel), the dataframe
      citynames (Optional)
      """
    if data==None:
        data = load_data()
    if citynames==None:
        citynames = [line.strip() for line in open('data/citynames.txt','r')]
    
    assert len(order)==len(data)+1, f"solution has {len(order)} entries but should have {len(data)+1}!"
    assert order[0]==citynames[0], f"route should start at {citynames[0]}!"
    assert order[0]==order[-1], f"route should start at {citynames[0]} and end at {citynames[0]}!"

    time = 0
    for i in range(1,len(order)):
        time += data[citynames.index(order[i-1]),citynames.index(order[i])]
    return time

def tran_time(citystart,cityend,data=None,citynames=None):
    """Calculates/ reads, the distance between two locations"""
    if data==None:
        data = load_data()
    if citynames==None:
        citynames = [line.strip() for line in open('data/citynames.txt','r')]
    return data[citynames.index(citystart),citynames.index(cityend)]

def gen_data(citynumber):
    """Generate distancematrix based on the number of locations to visit
    Takes one argument;
        citynumber, the number of locations to visit"""
    data = np.tril(np.random.randint(low=10,high=100,size=[citynumber,citynumber]),-1)
    data = data+np.transpose(data)
    np.savetxt("data/exampledata.csv",data,fmt='%s',delimiter=",")
    return data

def load_data(file="data/data_challenge.csv"):
    """Load the datafile
    Takes one argument;
        file (Optional), the path to the csv file with the data
        if no file is specified it will open the challenge data"""
    return np.genfromtxt(file, delimiter=",",dtype=int)

def save_solution(order):
    """Saves the solution to solution.txt
    Takes 1 argument
    order, a list of names"""
    f = open('solution.txt','w')
    f.writelines('\n'.join(order) + '\n')

