from typing import DefaultDict
import numpy as np
INT_MAX = 2147483647

def findMinRoute(tsp):
	sum = 0
	counter = 0
	j = 0
	i = 0
	min = INT_MAX
	visitedRouteList = DefaultDict(int)

	visitedRouteList[0] = 1
	route = [0] * len(tsp)


	while i < len(tsp) and j < len(tsp[i]):
		if counter >= len(tsp[i]) - 1:
			break
		if j != i and (visitedRouteList[j] == 0):
			if tsp[i][j] < min:
				min = tsp[i][j]
				route[counter] = j + 1
		j += 1
		if j == len(tsp[i]):
			sum += min
			min = INT_MAX
			visitedRouteList[route[counter] - 1] = 1
			j = 0
			i = route[counter] - 1
			counter += 1

	i = route[counter - 1] - 1

	for j in range(len(tsp)):

		if (i != j) and tsp[i][j] < min:
			min = tsp[i][j]
			route[counter] = j + 1

	sum += min

	print("Minimum Cost is :", sum)

def load_data():
    file_path = "D:\\greedy_tsp\\data.txt"
    data = np.loadtxt(file_path, dtype=int)
    N = len(data)
    dist_matrix = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            if i != j:
                dist_matrix[i][j] = np.sqrt((data[i, 1] - data[j, 1]) ** 2 + (data[i, 2] - data[j, 2]) ** 2)

    return dist_matrix


# Driver Code
def main():
	tsp = load_data()
	findMinRoute(tsp)
main()
