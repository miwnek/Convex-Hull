from convexhulls import *

# MIEJSCE DO TESTOWANIA FUNKCJI

points = genUniformRectangle(-10, 10, -20, 30, 100)
# points2 = genUniformCircle(10, 10, 10, 100)
# points3 = genUniformOnRectangle(-10, 10, 20, 30, 100)
# points4 = genUniformOnSquare(10, 25, 25)

saveList(points, "points1")
points1 = readList("points1")
# plotPoints(points)

hullScenes = divideconquerVis(points)
plot = Plot(scenes = hullScenes)
print(hullScenes)
plot.draw()


# -- Benchmarking --
# sizes = [100, 1000, 10000, 100000, 1000000]
# functions = [chan]

# for f in functions:
#    for s in sizes:
#        benchmark(f, 5, genUniformOnSquare, 10, int(s//4), int(s//4))
