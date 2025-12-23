import random

print("Random no. from 0 to 1 : ", random.random())

print()

print("Random no. :", random.randint(1, 95))

print()

num_list = [1, 6, 9, 20, 19]
print("Random no. from the list : ", random.choice(num_list))

print()

random.shuffle(num_list)
print("Shuffled order : ", num_list)

print()

print("Random Choice from the list: ", random.sample(num_list, 2))

print()

print("Random range : ",random.randrange(1, 10))
