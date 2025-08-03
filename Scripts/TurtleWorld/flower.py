from swampy.TurtleWorld import *
from mypoligon import arc


def petal (t, r, angle):
  """Draws a petal using two arcs.
  t: turtle
  r: radius of the arcs
  angle: angle (degrees) that subtends the arcs

  """
  for i in range(2):
    arc(t, r, angle, o=True)
    lt(t, 180 - angle)

def flower(t, n, r, angle):
  """Draws a flower with n petals
  t: turtle
  n: number of petals
  r: radius of the arcs
  angle: angle (degrees) that subtends the arcs
  """
  for i in range(n):
    petal(t, r, angle)
    lt(t, 360.0 / n)

def move(t, length):
  """Move Turtle(t) forward (length) units without leaving trail
  Leaves the pen down
  """
  t.pu()
  t.fd(length)
  t.pd()

if __name__ == '__main__':

  world=TurtleWorld()
  bob = Turtle()
  print(bob)
  bob.delay = 0.01

  move(bob, -100)
  flower(bob, 7, 60.0, 60.0)

  move(bob, 100)
  flower(bob, 10, 40.0, 80.0)

  move(bob, 100)
  flower(bob, 20, 140.0, 20.0)

  wait_for_user()

