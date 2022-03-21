import collections
import random

import networkx as nx
import numpy as np


# Test_1   O(log(N))

def test_2(n_people: int, k_syllable: int):

    count = [i for i in range(1, n_people + 1)]
    print(count)
    stop = False
    first_out = 0

    while not stop:
        if len(count) == 1:
            stop = True
            print(f'Winner: {count[0]}')
        else:
            if k_syllable > n_people:
                del_n_people = k_syllable - n_people - 1 + first_out
                if del_n_people >= len(count):
                    while del_n_people >= len(count):
                        del_n_people = del_n_people - len(count)
            else:
                del_n_people = k_syllable - 1 + first_out
                while len(count) <= del_n_people:
                    del_n_people = del_n_people - len(count)
            del count[del_n_people]
            first_out = del_n_people
            if first_out > len(count):
                first_out = first_out - len(count) - 1
            print(count)


def test_3(graph, start_node):

    all_visits = []
    visited = []
    queue = []
    connection_rate = 0
    queue.append(start_node)

    while all_visits != graph.nodes:
        queue.append(start_node)
        for node in queue:
            d = graph.adj[node]
            visited.append(node)
            for k in d:
                if k in visited or k in queue:
                    pass
                else:
                    queue.append(k)

        all_visits.extend(visited)
        temp_lst = list(set(graph.nodes) - set(all_visits))
        connection_rate += 1
        if len(temp_lst) == 0:
            return connection_rate
        start_node = temp_lst[0]


def test_5(word):
    word_1 = []
    word_2 = []
    v = {}
    s = ''
    for w in range(len(word_1)):
        word_2.append(word[w][word])
        v = collections.Counter(word_2)
    for i, j in iter(v.items()):
        if j == max(v.values()):
            s = i
    return s


def test_6(list_order: list, new_list: list):
    rocket = True
    for first_rocket in list_order:
        start_time = first_rocket[0]
        finish_time = first_rocket[1]
        time = range(start_time, finish_time)
        for second_rocket in list_order:
            if first_rocket == second_rocket or second_rocket in new_list:
                pass
            else:
                if second_rocket[0] == start_time:
                    rocket = False
                if second_rocket[1] in time:
                    rocket = False
                if second_rocket[0] in time:
                    rocket = False
                if start_time in range(second_rocket[0], second_rocket[1] + 1):
                    rocket = False
        new_list.append(first_rocket)

        if rocket:
            print('Enough first rocket')
        else:
            print('Do not enough first rocket')


def test_7(a: int, b: int):

    array = list([x + a for x in (range(b - a))]) * 2
    random.shuffle(array)
    print(array)

    numbers = np.full(b - a, 0)
    for x in array:
        numbers[x - a] += 1
    result = np.array([], dtype=int)
    for i in range(b - a):
        result = np.concatenate((result, np.full(numbers[i], a + i, dtype=int)))
    print(np.array(result))


def test_4(cost: list):
    coords = [(0, 0)]

    for j in range(1, len(cost[0])):
        cost[0][j] += cost[0][j - 1]

    for i in range(1, len(cost)):
        cost[i][0] += cost[i-1][0]

    for i in range(1, len(cost)):
        for j in range(1, len(cost[0])):
            cost[i][j] += min(cost[i][j-1], cost[i-1][j])
            if cost[i][j - 1] <= cost[i - 1][j] and (i, j-1) != coords[-1]:
                coords.append((i, j-1))
            else:
                if (i - 1, j) != coords[-1]:
                    coords.append((i - 1, j))
    coords.append((len(cost) - 1, len(cost) - 1))

    print(cost[-1][-1])
    print(coords)


if __name__ == '__main__':
    test_2(5, 2)

    g = nx.Graph()
    g.add_nodes_from("ABCDEFG")
    g.add_edges_from(
        [
            ("A", "B"),
            ("B", "C"),
            ("B", "D"),
            ("C", "D"),
            ("G", "F")
        ]
    )
    print("Компонент связанности графа: ", test_3(g, "F"))

    price = [
        [2, 5, 6],
        [7, 1, 9],
        [6, 4, 2]
    ]
    test_4(price)

    test = [['A', 'T', 'T', 'A'],
            ['A', 'C', 'T', 'A'],
            ['A', 'G', 'C', 'A'],
            ['A', 'C', 'A', 'A']]

    test_5(test)

    orders_received = [(4, 3), (7, 9), (5, 2), (9, 11)]
    list_ = []
    test_6(orders_received, list_)

    test_a = 15
    test_b = 25
    test_7(test_a, test_b)
