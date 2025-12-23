import random

print("Random no. from 0 to 1 : ", random.random())                # Random no. from 0 to 1 : 0.5474005703828818

print("Random no. :", random.randint(1, 95))                       # Random no. : 42

num_list = [1, 6, 9, 20, 19]
print("Random no. from the list : ", random.choice(num_list))      # Random no. from the list :  9

random.shuffle(num_list)
print("Shuffled order : ", num_list)                               # Shuffled order :  [19, 1, 6, 9, 20]

print("Random Choice from the list: ", random.sample(num_list, 2)) # Random Choice from the list:  [6, 19]

print("Random range : ",random.randrange(1, 10))                   # Random range :  7
