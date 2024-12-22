from typing import DefaultDict
import numpy as np
import matplotlib.pyplot as plt

INT_MAX = 2147483647

# def findMinRoute(tsp):
#     total_distance = 0
#     counter = 0
#     j = 0
#     i = 0
#     min_distance = INT_MAX
#     visitedRouteList = DefaultDict(int)

#     visitedRouteList[0] = 1
#     route = [0] * len(tsp)

#     # Danh sách lưu các thành phố đã đi qua
#     cities_visited = [0]  # Bắt đầu từ thành phố 0

#     while i < len(tsp) and j < len(tsp[i]):
#         if counter >= len(tsp[i]) - 1:
#             break
#         if j != i and (visitedRouteList[j] == 0):
#             if tsp[i][j] < min_distance:
#                 min_distance = tsp[i][j]
#                 route[counter] = j + 1
#         j += 1
#         if j == len(tsp[i]):
#             total_distance += min_distance
#             min_distance = INT_MAX
#             visitedRouteList[route[counter] - 1] = 1
#             cities_visited.append(route[counter] - 1)  # Lưu thành phố đã đi qua
#             j = 0
#             i = route[counter] - 1
#             counter += 1

#     i = route[counter - 1] - 1

#     for j in range(len(tsp)):
#         if (i != j) and tsp[i][j] < min_distance:
#             min_distance = tsp[i][j]
#             route[counter] = j + 1

#     total_distance += min_distance
#     cities_visited.append(route[counter] - 1)  # Lưu thành phố cuối cùng

#     # In kết quả
#     print("Minimum Cost is:", total_distance)
#     print("Route taken by the truck:", " -> ".join(map(str, cities_visited)))

#     return cities_visited


def findMinRoute(tsp):
    total_distance = 0
    counter = 0
    j = 0
    i = 0
    min_distance = INT_MAX
    visitedRouteList = DefaultDict(int)

    visitedRouteList[0] = 1  # Đánh dấu thành phố đầu tiên đã được ghé thăm
    route = [0] * len(tsp)

    # Danh sách lưu các thành phố đã đi qua
    cities_visited = [0]  # Bắt đầu từ thành phố 0

    while counter < len(tsp) - 1:
        min_distance = INT_MAX
        next_city = -1

        # Tìm thành phố gần nhất chưa được ghé thăm
        for j in range(len(tsp)):
            if j != i and visitedRouteList[j] == 0 and tsp[i][j] < min_distance:
                min_distance = tsp[i][j]
                next_city = j

        # Cập nhật thông tin
        if next_city != -1:
            visitedRouteList[next_city] = 1  # Đánh dấu thành phố đã ghé thăm
            cities_visited.append(next_city)  # Lưu thành phố vào lộ trình
            total_distance += min_distance  # Cộng khoảng cách
            i = next_city  # Chuyển sang thành phố tiếp theo
            counter += 1

    # Quay về thành phố đầu tiên
    total_distance += tsp[i][0]
    cities_visited.append(0)  # Quay lại thành phố đầu tiên

    # In kết quả
    print("Minimum Cost is:", total_distance)
    print("Route taken by the truck:", " -> ".join(map(str, cities_visited)))

    return cities_visited


# def load_data():
#     file_path = "D:\\Tran Hoang Vu\\Semester 5\\Artificical intelligence\\final assigment\\tsp_greedy\data\\42.txt"
#     data = np.loadtxt(file_path, dtype=int)
#     N = len(data)
#     dist_matrix = np.zeros((N, N), dtype=int)
#     for i in range(N):
#         for j in range(N):
#             if i != j:
#                 dist_matrix[i][j] = np.sqrt((data[i, 1] - data[j, 1]) ** 2 + (data[i, 2] - data[j, 2]) ** 2)

#     return dist_matrix


def plot_route(data, route):
    plt.figure(figsize=(10, 8))
    
    # Vẽ các điểm thành phố và ghi số thứ tự
    for city in range(len(data)):
        plt.scatter(data[city, 1], data[city, 2], c='blue', label='City' if city == 0 else "")
        plt.text(data[city, 1], data[city, 2], str(city), fontsize=15, color='green')

    # Vẽ đường đi giữa các thành phố
    for i in range(len(route) -1):
        city1 = route[i]
        city2 = route[i+1]
        plt.plot(
            [data[city1, 1], data[city2, 1]],
            [data[city1, 2], data[city2, 2]],
            c='red', linewidth=1.5
        )
	
  
    city_last = route[-1]
    city_start = route[0]
    plt.plot(
        [data[city_last, 1], data[city_start, 1]],
        [data[city_last, 2], data[city_start, 2]],
        c='red', linewidth=1.5,label='Truck route'
    )

    # Thiết lập tiêu đề và chú thích
    plt.title("Traveling Salesperson Problem - Route")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid()
    plt.show()





# Driver Code
# def main():
# 	tsp = load_data()
# 	findMinRoute(tsp)
# main()
def main():
    file_path = "D:\\Tran Hoang Vu\\Semester 5\\Artificical intelligence\\final assigment\\tsp_greedy\\data\\26.txt"
    data = np.loadtxt(file_path, dtype=int)

    tsp = np.zeros((len(data), len(data)), dtype=int)
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                tsp[i][j] = np.sqrt((data[i, 1] - data[j, 1]) ** 2 + (data[i, 2] - data[j, 2]) ** 2)

    cities_visited = findMinRoute(tsp)
    # Vẽ sơ đồ
    plot_route(data, cities_visited)

main()
