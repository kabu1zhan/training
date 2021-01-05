import math
def initSpher(a, f):
  b = a * (1. - f)
  c = a / (1. - f)
  e2 = f * (2. - f)
  e12 = e2 / (1. - e2)
  return (b, c, e2, e12)

def func(x,y,z,a,f):
  b,c,e2,e12 = initSpher(a,f)
  p = math.hypot(x,y)
  if p == 0.:
    lat = math.copysign(math.pi / 2., z)
    lon = 0.
    h = math.fabs(z) - b
  else:
    t = z/p * (1. + e12 * b / math.hypot(p,z))
    for i in range(2):
      t = t * (1. - f)
      lat = math.atan(t)
      cos_lat = math.cos(lat)
      sin_lat = math.sin(lat)
      t = (z + e12 * b * sin_lat ** 3) / (p - e2 * a * cos_lat ** 3)
    lon = math.atan2(y,x)
    lat = math.atan(t)
    cos_lat = math.cos(lat)
    n = c /math.sqrt(1. + e12 * cos_lat ** 2)
    if math.fabs(t) <= 1.:
      h = p / cos_lat - n
    else:
      h = z / math.sin(lat) - n * (1. - e2)
  return (lat, lon, h)

a = func(2861932, 2195185, 5242900, 6378245, 1/298.3)

print(a)
