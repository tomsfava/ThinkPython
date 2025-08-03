from swampy.TurtleWorld import *
import math

def polyline(t, n, length, angle, o=True):
  for i in range(n):
    fd(t, length)
    if o:
      lt(t, angle)
    else:
      rt(t, angle)

def poligon(t, length, n, o):
  angle = 360.00/n
  polyline(t, n, length, angle, o)

def arc(t, r, angle, o):
  arc_length = 2*math.pi*r*angle/360
  n = int(arc_length/3) + 1
  step_length = arc_length/n
  step_angle = float(angle)/n
  polyline(t, n, step_length, step_angle, o)

def circle(t, r, o):
  arc(t, r, 360, o)

if __name__ == '__main__':

  world = TurtleWorld()
  bob = Turtle()
  bob.delay = 0.01

  circle(bob, 20, False)




  wait_for_user()