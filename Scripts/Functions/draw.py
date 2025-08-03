from swampy.TurtleWorld import *

def draw(t, length, n):
  if n == 0:
    return
  angle = 50
  fd(t, length*n)
  lt(t, angle)
  draw(t, length, n-1)
  rt(t, 2*angle)
  draw(t, length, n-1)
  lt(t, angle)
  bk(t, length*n)

if __name__ == '__main__':

  world=TurtleWorld()
  bob=Turtle()
  bob.delay = 0.001
  bob.rt(90)
  bob.pu()
  bob.fd(100)
  bob.pd()

  draw(bob, 10, 6)

  wait_for_user()