import pandas as pd

f = open("weight.csv", 'r')

weight_capacity_list = []
trips_list = []

next(f)

for line in f:
  
    x = line.index(',')
    weight_capacity = float(line[0:x])  
    trips = int(line[(x + 1):-1]) 
    weight_capacity_list.append(weight_capacity)
    trips_list.append(trips)

f.close()

data = [weight_capacity_list, trips_list]
df = pd.DataFrame(data).T 

df.columns = ['weights', 'trips']

df['total_weight'] = df['weights'] * df['trips']

df.to_csv('auto.csv', index=False)

print(df)