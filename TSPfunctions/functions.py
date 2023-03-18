# functions
def totaltime(order,data):
    """Calculates time the total travelling time.
    Takes two arguments, order, a list with your solution and data, the dataframe"""
    
    citynames = [line.strip() for line in open('data/citynames.txt','r')]
    
    assert len(order)==len(data)+1, f"solution has {len(order)} entries but should have {len(data)+1}!"
    assert order[0]==citynames[0], f"route should start at {citynames[0]}!"
    assert order[0]==order[-1], f"route should start at {citynames[0]} and end at {citynames[0]}!"

    time = 0
    for i in range(1,len(order)):
        time += data[citynames.index(order[i-1]),citynames.index(order[i])]
    return time

def tran_time(citystart,cityend,data):
    citynames = [line.strip() for line in open('data/citynames.txt','r')]
    return data[citynames.index(citystart),citynames.index(cityend)]

#def gen_data(citynumber):



