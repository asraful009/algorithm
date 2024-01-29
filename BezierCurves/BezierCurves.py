
import json
import matplotlib.pyplot as plt
import numpy as np

class Point:
  x = 0.0
  y = 0.0
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

def BézierCurves3Point(points):
  t_points = list()
  x, y = list(map(lambda p: p.x, points)), list(map(lambda p: p.y, points))
  for t in range(x[0], x[len(x)]: 0.1):
    print(t)

def main():
  f = open('v.json')
  points = list()
  data = json.load(f)
  for i in data:
    points.append(Point(float(i[0]), float(i[1])))
  f.close()
  # x, y = list(map(lambda p: p.x, points)), list(map(lambda p: p.y, points))
  BézierCurves3Point(points)
  # print(x, y)
  # plt.plot(x, y)
  # plt.show()


if __name__ == "__main__":
  main()