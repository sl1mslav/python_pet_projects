import itertools

start = (0, 2)  # координаты почтового отделения
coords = [(2, 5), (5, 2), (6, 6), (8, 3)]  # координаты остальных точек


# функция, считающая дистанцию от одной точки до другой
def calcDist(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


# функция, считающая общую дистанцию маршрута используя порядок и координаты точек в кортеже
def calcTotalDist(route):
    totalDist = calcDist(start, route[0]) + calcDist(route[-1], start)
    for i in range(len(coords) - 1):
        totalDist += calcDist(route[i], route[i + 1])
    return totalDist


allRoutes = list(itertools.permutations(coords))  # список всех возможных перестановок по n точек
shortestDist = calcTotalDist(allRoutes[0])
# алгоритм, выбирающий оптимальный путь
for route in allRoutes[1:]:
    if calcTotalDist(route) < shortestDist:
        shortestDist = calcTotalDist(route)
        neededRoute = list(route)
# алгоритм, выводящий результат в консоль по заранее выбранному списку
output = f"{start}"
neededRoute.insert(0, start)
neededRoute.append(start)
totalDist = 0
for i in range(1, len(neededRoute)):
    totalDist += calcDist(neededRoute[i - 1], neededRoute[i])
    output += f" -> {neededRoute[i]}[{totalDist}]"
print(f"{output} = {totalDist}")
