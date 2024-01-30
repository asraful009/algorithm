# Bézier Curves N Point

https://en.wikipedia.org/wiki/B%C3%A9zier_curve

core function for Bézier Curves N Point
```python3
def BézierCurvesNPointFn(t: float, a) -> float:
  s = 0
  n = len(a)-1
  i = 0
  for ai in a:
    s+= math.comb(n, i) * ((1-t)**(n-i)) * (t**(i)) * ai
    i+=1
  return s
```


```python3
def BézierCurves3Point(points):
  t_points = list()
  x, y = list(map(lambda p: p.x, points)), list(map(lambda p: p.y, points))
  for t in np.linspace(0, 1, num=100):
    xt = BézierCurvesNPointFn(t, x)
    yt = BézierCurvesNPointFn(t, y)
    t_points.append(Point(xt, yt))
  return t_points
```
