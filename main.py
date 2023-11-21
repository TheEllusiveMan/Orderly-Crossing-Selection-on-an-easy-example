import random
# import numpy as np


def random_ch_pull(population_size):
    ch_pull = []
    cities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for ch in range(population_size):
        city = cities.copy()
        random.shuffle(city)
        city.append(city[0])
        ch_pull.append(city)
    print("Ch pull", ch_pull)
    return ch_pull


def fitness(ch_pull, M1):
    ch_pull_sum = []
    print("Cur ch pull", ch_pull)
    for ch in ch_pull:
        cost = 0
        for j in range(len(ch)-1):
            city_out = ch[j]
            city_in = ch[j+1]
            cost += M1[city_out][city_in]
            # print("Cost", cost)
        # print("Ch", ch)
        # print("Total cost:", cost)
        ch_pull_sum.append(cost)
    ch_min = min(ch_pull_sum)
    print("Ch pull sum list {0}\nCh min: {1}".format(ch_pull_sum, ch_min))
    return ch_pull_sum


def orderly_crossing(ch_pull):
    mating_pull = ch_pull.copy()
    random.shuffle(mating_pull)


M1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 3, 5, 7, 1, 4, 6, 9, 2, 5],
      [0, 3, 0, 3, 5, 7, 3, 2, 1, 5, 7],
      [0, 5, 3, 0, 4, 5, 7, 4, 1, 2, 6],
      [0, 7, 5, 4, 0, 5, 7, 2, 4, 3, 9],
      [0, 1, 7, 5, 5, 0, 7, 2, 2, 1, 8],
      [0, 4, 3, 7, 7, 7, 0, 1, 6, 9, 3],
      [0, 6, 2, 4, 2, 2, 1, 0, 5, 2, 1],
      [0, 9, 1, 1, 4, 2, 6, 5, 0, 5, 2],
      [0, 2, 5, 2, 3, 1, 9, 2, 5, 0, 4],
      [0, 5, 7, 6, 9, 8, 3, 1, 2, 4, 0]]

# M1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 3, 5, 7, 1, 4, 6, 9, 2, 5],
#                [0, 3, 0, 3, 5, 7, 3, 2, 1, 5, 7],
#                [0, 5, 3, 0, 4, 5, 7, 4, 1, 2, 6],
#                [0, 7, 5, 4, 0, 5, 7, 2, 4, 3, 9],
#                [0, 1, 7, 5, 5, 0, 7, 2, 2, 1, 8],
#                [0, 4, 3, 7, 7, 7, 0, 1, 6, 9, 3],
#                [0, 6, 2, 4, 2, 2, 1, 0, 5, 2, 1],
#                [0, 9, 1, 1, 4, 2, 6, 5, 0, 5, 2],
#                [0, 2, 5, 2, 3, 1, 9, 2, 5, 0, 4],
#                [0, 5, 7, 6, 9, 8, 3, 1, 2, 4, 0]])


population_size = int(input("Enter population size: "))
ch_pull = random_ch_pull(population_size)
costs = fitness(ch_pull, M1)
