from swampy.TurtleWorld import *
from flower import move
from mypoligon import *

def isosceles(t, r, angle):
  """Draws an isosceles triangle.
  The turtle starts and ends at the peak, facing the middle of the base.

  t: Turtle
  r: length of the equal legs
  angle: half peak angle in degrees
  """
  y = r * math.sin(angle * math.pi / 180)
  t.rt(angle)
  t.fd(r)
  t.lt(90+angle)
  t.fd(2*y)
  t.lt(90+angle)
  t.fd(r)
  t.lt(180-angle)

def polypie(t, n, r):
  """Draws a pie divided into radial segments.

  t: Turtle
  n: number of radial segments
  r: length of the radial spokes
  """
  angle = 360.0/n
  for i in range(n):
    isosceles(t, r, angle/2)
    t.lt(angle)

def draw_pie(t, n, r):
  """Draws a pie, then moves into position to the right.

  t: Turtle
  n: number of radial segments
  r: length of the radial spokes
  """
  polypie(t, n, r)
  t.pu()
  t.fd(r*2 + 10)
  t.pd()

if __name__ == '__main__':

  world = TurtleWorld()
  bob = Turtle()


  bob.pu()
  bob.bk(130)
  bob.pd()

  size = 40

  draw_pie(bob, 5, size)
  draw_pie(bob, 6, size)
  draw_pie(bob, 7, size)
  draw_pie(bob, 8, size)


  wait_for_user()