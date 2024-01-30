
import json
import matplotlib.pyplot as plt
import numpy as np
import math

class Point:
  x = 0.0
  y = 0.0
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

def BézierCurves3Point(points):
  t_points = list()
  x, y = list(map(lambda p: p.x, points)), list(map(lambda p: p.y, points))
  for t in np.linspace(0, 1, num=10):
    xt = BézierCurvesNPointFn(t, x)
    yt = BézierCurvesNPointFn(t, y)
    t_points.append(Point(xt, yt))
    # print(f"{t} => [{xt}, {yt}]")
  return t_points

def BézierCurves3PointFn(t: float, a) -> float:
  return ((1.0-t)**2)*a[0] + 2*(1.0-t)*t*a[1] + t*t*a[2]

def BézierCurves4PointFn(t: float, a) -> float:
  return ((1.0-t)**3)*a[0] + 3*((1.0-t)**2)*t*a[1] + 3*(1.0-t)*(t**2)*a[2] + (t**3)*a[3]

def BézierCurvesNPointFn(t: float, a) -> float:
  s = 0
  n = len(a)
  i = 0
  for ai in a:
    st = math.comb(n, i) * ((1-t)**(n-i)) * (t**(i)) * ai
    print(f"{st}")
    s +=st
    i+=1
  return s


def main():
  f = open('v.json')
  points = list()
  data = json.load(f)
  for i in data:
    points.append(Point(float(i[0]), float(i[1])))
  f.close()
  t_points = BézierCurves3Point(points)
  x, y = list(map(lambda p: p.x, points)), list(map(lambda p: p.y, points))
  xt, yt = list(map(lambda p: p.x, t_points)), list(map(lambda p: p.y, t_points))
  # print(x, y)
  plt.plot(x, y, label = "Anchor")
  plt.plot(xt, yt, label = "Corve") 
  plt.legend() 
  plt.show()


if __name__ == "__main__":
  main()