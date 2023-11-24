import random


def random_ch_pull(population_size):
    ch_pull = []
    cities = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for ch in range(population_size):
        city = cities.copy()
        random.shuffle(city)
        city.insert(0, 1)
        city.append(1)
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
        # print("Total cost:", cost)
        ch_pull_sum.append(cost)
    ch_min = min(ch_pull_sum)
    print("Ch pull sum list {0}\nCh min: {1}".format(ch_pull_sum, ch_min))
    return ch_min


def orderly_crossing(ch_pull):
    mating_pull = ch_pull.copy()
    random.shuffle(mating_pull)
    print("\nMating pull", mating_pull)

    ch_pull.clear()

    for mate in range(0, len(mating_pull), 2):
        p_1 = random.randrange(2, 6)
        p_2 = random.randrange(6, 10)
        # print("p_1: {0}, p_2: {1}".format(p_1, p_2))

        mid_genes_1 = mating_pull[mate+1][p_1:p_2]
        mid_genes_2 = mating_pull[mate][p_1:p_2]
        # print("Mid genes", mid_genes_1, mid_genes_2)

        new_genes_1_right = mating_pull[mate][p_2:10]
        new_genes_1_left = mating_pull[mate][:p_1]
        new_genes_1_left.remove(1)

        new_genes_2_right = mating_pull[mate+1][p_2:10]
        new_genes_2_left = mating_pull[mate+1][:p_1]
        new_genes_2_left.remove(1)
        # print("New genes {0} {1}".format(new_genes_1_right, new_genes_1_left))

        child_1 = [1]
        # print("\nChild 1", child_1)
        # print("New genes 1 {0} {1}".format(new_genes_1_right, new_genes_1_left))
        for gene in new_genes_1_right:
            if gene in mid_genes_1:
                pass
            else:
                child_1.append(gene)

        # print("Child 1 + new_genes_1_right", child_1)
        # print("Mid genes 1", mid_genes_1)
        child_1.extend(mid_genes_1)
        # print("Child 1 + mid_genes_1", child_1)

        for gene in new_genes_1_left:
            if gene in mid_genes_1:
                pass
            else:
                child_1.append(gene)

        # print("Child 1 + new_genes_1_left", child_1)

        for gene in range(2, 11):
            if gene not in new_genes_1_right and gene not in new_genes_1_left and gene not in mid_genes_1:
                child_1.append(gene)

        child_1.append(1)
        ch_pull.append(child_1)
        print("Result Child 1", child_1)

        child_2 = [1]
        # print("\nChild 2", child_2)
        # print("New genes 2 {0} {1}".format(new_genes_2_right, new_genes_2_left))
        for gene in new_genes_2_right:
            if gene in mid_genes_2:
                pass
            else:
                child_2.append(gene)

        # print("Child 2 + new_genes_2_right", child_2)
        # print("Mid genes 2", mid_genes_2)
        child_2.extend(mid_genes_2)
        # print("Childs 2 + mid_genes_2", child_2)

        for gene in new_genes_2_left:
            if gene in mid_genes_2:
                pass
            else:
                child_2.append(gene)

        # print("Child 2 + new_genes_2_left", child_2)

        for gene in range(2, 11):
            if gene not in new_genes_2_right and gene not in new_genes_2_left and gene not in mid_genes_2:
                child_2.append(gene)

        child_2.append(1)
        ch_pull.append(child_2)
        print("Result Child 2", child_2)

    print("New ch pull", ch_pull)
    return ch_pull


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


population_size = int(input("Enter population size: "))

ch_pull = random_ch_pull(population_size)
epoch = 1
best_epoch = epoch
min_cost = fitness(ch_pull, M1)
number_not_better = 0


while number_not_better < 20:
    ch_pull = orderly_crossing(ch_pull)
    cost = fitness(ch_pull, M1)
    if cost <= min_cost:
        min_cost = cost
        best_epoch = epoch
        number_not_better = 0
        best_ch_pull = ch_pull.copy()
    else:
        number_not_better += 1
    print("Epoch:", epoch)
    print("Min cost:", min_cost)
    print("Number not better", number_not_better)
    epoch += 1
    print("\n---------------------------------------------------------------------------------------------------------")

if number_not_better == 20:
    print("Min cost: {0} \nBest population {1}\nBest epoch: {2}".format(min_cost, best_ch_pull, best_epoch))
