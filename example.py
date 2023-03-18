from TSPfunctions.functions import *
# data = np.tril(np.random.randint(low=10,high=100,size=[10,10]),-1)
# data = data+np.transpose(data)
# print(data)

data = load_data()
citynames = [line.strip() for line in open('data/citynames.txt','r')]
order=citynames
order.append(citynames[0])
print(order)
#print(cities)
print(totaltime(order))


print(gen_data(len(citynames)))

print(load_data())

save_solution(order)

solution = [line.strip() for line in open('solution.txt','r')]
print(totaltime(solution))