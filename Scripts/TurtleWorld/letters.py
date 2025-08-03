from swampy.TurtleWorld import *
from mypoligon import arc, circle
import math

def draw_a(t, height):
  """Draw the letter A with the given height.
  moves to the next letter position
  """
  radians = math.radians(15)
  width =  (height * math.tan(radians)) * 2
  bar_width = (height /2 * math.tan(radians)) *2
  side = height / math.cos(radians)

  t.lt(75)
  t.fd(side)
  t.rt(150)
  t.fd(side)
  t.bk(side/2)
  t.rt(105)
  t.fd(bar_width)
  t.pu()
  t.lt(75)
  t.fd(side/2)
  t.lt(105)
  t.fd(2*width+10)

def draw_b(t,height):
  """Draw the letter B with the given height.
  Moves to the next letter position
  """
  radians = math.radians(15)
  width =  (height * math.tan(radians)) * 2

  t.pd()
  t.lt(90)
  t.fd(height)
  t.rt(90)
  arc(t, height/4, 180, False)
  t.lt(180)
  arc(t, height / 4, 180, False)
  t.pu()
  t.lt(180)
  t.fd(2*width+10)

def draw_c(t, height):
  """Draw the letter C with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width =  (height * math.tan(radians)) * 2


  t.fd(width/2)
  t.pd()
  t.lt(180)
  arc(t, height/2, 180, False)
  t.pu()
  t.rt(90)
  t.fd(height)
  t.lt(90)
  t.fd((2*width+10) - width/2)

def draw_d(t, height):
  """Draw the letter D with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width =  (height * math.tan(radians)) * 2

  t.lt(90)
  t.pd()
  t.fd(height)
  t.rt(90)
  arc(t, height/2, 180, False)
  t.pu()
  t.lt(180)
  t.fd(2*width+10)

def draw_e(t, height):
  """Draw the letter E with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.lt(90)
  t.pd()
  t.fd(height)
  t.rt(90)
  t.fd(2*width/3)
  t.pu()
  t.rt(90)
  t.fd(height/2)
  t.rt(90)
  t.pd()
  t.fd(2*width/3)
  t.lt(90)
  t.fd(height/2)
  t.lt(90)
  t.fd(2*width/3)
  t.pu()
  t.fd((2*width+10)-(2*width/3))

def draw_f(t, height):
  """Draw the letter F with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.pd()
  t.lt(90)
  t.fd(height)
  t.rt(90)
  t.fd(2*width/3)
  t.pu()
  t.rt(90)
  t.fd(height/2)
  t.pd()
  t.rt(90)
  t.fd(2*width/3)
  t.pu()
  t.lt(90)
  t.fd(height/2)
  t.lt(90)
  t.fd(2*width+10)

def draw_g(t, height):
  """Draw the letter G with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.fd(width/2)
  t.lt(90)
  t.fd(height/2-5)
  t.pd()
  t.fd(5)
  t.rt(90)
  t.fd(width/2)
  t.rt(90)
  arc(t, height/2, 300, False)
  t.pu()
  arc(t, height/2, 150, False)
  t.rt(180)
  t.fd((2*width+10)-width/2)

def draw_h(t, height):
  """Draw the letter H with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.lt(90)
  t.pd()
  t.fd(height)
  t.bk(height/2)
  t.rt(90)
  t.fd(width)
  t.lt(90)
  t.fd(height/2)
  t.bk(height)
  t.pu()
  t.rt(90)
  t.fd(width + 10)

def draw_i(t, height):
  """Draw the letter I with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.pd()
  t.fd(width/2)
  t.lt(90)
  t.fd(height)
  t.lt(90)
  t.fd(width/2)
  t.bk(width)
  t.fd(width/2)
  t.lt(90)
  t.fd(height)
  t.lt(90)
  t.fd(width/2)
  t.pu()
  t.fd(width+10)

def draw_j(t, height):
  """Draw the letter J with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.lt(90)
  t.fd(width/2)
  t.lt(180)
  t.pd()
  arc(t, width/2, 180, True)
  t.fd(height-width/2)
  t.pu()
  t.bk(height)
  t.rt(90)
  t.fd(width+10)

def draw_k(t, height):
  """Draw the letter K with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  joint = height * 2 / 3
  angle_upper = math.degrees(math.atan(width/(height-joint)))
  angle_lower = math.degrees(math.atan(width / joint))
  upper_leg = math.hypot(width, (height-joint))
  lower_leg = math.hypot(width, joint)

  t.lt(90)
  t.pd()
  t.fd(height)
  t.bk(height-joint)
  t.rt(angle_upper)
  t.fd(upper_leg)
  t.bk(upper_leg)
  t.lt(angle_upper +180)
  t.lt(angle_lower)
  t.fd(lower_leg)
  t.bk(lower_leg)
  t.rt(angle_lower)
  t.fd(joint)
  t.pu()
  t.lt(90)
  t.fd(2*width+10)

def draw_l(t, height):
  """Draw the letter L with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.lt(90)
  t.pd()
  t.fd(height)
  t.bk(height)
  t.rt(90)
  t.fd(width)
  t.pu()
  t.fd(width+10)

def draw_m(t, height):
  """Draw the letter M with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  side = height / math.cos(radians)

  t.lt(90)
  t.pd()
  t.fd(height)
  t.rt(165)
  t.fd(side)
  t.lt(150)
  t.fd(side)
  t.rt(165)
  t.fd(height)
  t.pu()
  t.lt(90)
  t.fd(width+10)

def draw_n(t, height):
  """Draw the letter N with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  def get_angle_from_opposite_and_adjacent(width, height):
    angle_rad = math.atan(width/height)
    angle_deg = math.degrees(angle_rad)
    return angle_deg

  def get_hypotenuse(width, height):
    return math.sqrt(width**2+height**2)

  t.lt(90)
  t.pd()
  t.fd(height)
  t.rt(180-get_angle_from_opposite_and_adjacent(width, height))
  t.fd(get_hypotenuse(width, height))
  t.lt(180-get_angle_from_opposite_and_adjacent(width, height))
  t.fd(height)
  t.bk(height)
  t.rt(90)
  t.pu()
  t.fd(width+10)
  t.bk(14*(2*width+10))
  t.rt(90)
  t.fd(2*width+10)
  t.lt(90)

def draw_o(t, height):
  """Draw the letter O with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.fd(width/2)
  t.pd()
  arc(t, height/2, 360, True)
  t.pu()
  t.fd((2*width+10)-width/2)

def draw_p(t, height):
  """Draw the letter P with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.lt(90)
  t.pd()
  t.fd(height)
  t.rt(90)
  arc(t, height/4, 180, False)
  t.lt(90)
  t.pu()
  t.fd(height/2)
  t.lt(90)
  t.fd(2*width+10)

def draw_q(t, height):
  """Draw the letter Q with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.fd(width/2)
  t.pd()
  arc(t, height/2, 420, True)
  t.lt(90)
  t.fd(width/2)
  t.bk(width)
  t.fd(width/2)
  t.lt(90)
  t.pu()
  arc(t, height/2, 60, False)
  t.rt(180)
  t.fd((2*width+10)-width/2)

def draw_r(t, height):
  """Draw the letter R with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  angle = math.degrees(math.atan(width/height))
  leg = math.hypot(width/2, height/2)

  t.lt(90)
  t.pd()
  t.fd(height)
  t.rt(90)
  arc(t, height/4, 180, False)
  t.rt(180)
  t.rt(90-angle)
  t.fd(leg)
  t.lt(90-angle)
  t.pu()
  t.fd((2*width+10)-width/2)

def draw_s(t, height):
  """Draw the letter S with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  offset = (height/4) * math.sin(math.radians(30))

  t.fd(height/4)
  t.lt(180)
  arc(t, height/4, 60, False)
  t.rt(180)
  t.pd()
  arc(t, height/4, 240, True)
  arc(t, height/4, 240, False)
  t.rt(30)
  t.pu()
  t.fd(height-offset)
  t.lt(90)
  t.fd((2*width+10)-height/2)

def draw_t(t, height):
  """Draw the letter T with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.fd(width/2)
  t.lt(90)
  t.pd()
  t.fd(height)
  t.rt(90)
  t.fd(width/2)
  t.bk(width)
  t.fd(width/2)
  t.rt(90)
  t.fd(height)
  t.lt(90)
  t.pu()
  t.fd((2*width+10)-width/2)

def draw_u(t, height):
  """Draw the letter U with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2

  t.lt(90)
  t.fd(height/4)
  t.pd()
  t.fd(3*height/4)
  t.bk(3*height/4)
  t.lt(180)
  arc(t, height/4, 180, True)
  t.fd(3*height/4)
  t.bk(3*height/4)
  t.pu()
  t.bk(height/4)
  t.rt(90)
  t.fd((2*width+10)-height/2)

def draw_v(t, height):
  """Draw the letter V with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  side = height / math.cos(radians)

  t.fd(width/2)
  t.lt(105)
  t.pd()
  t.fd(side)
  t.bk(side)
  t.rt(30)
  t.fd(side)
  t.bk(side)
  t.rt(75)
  t.pu()
  t.fd((2*width+10)-width/2)

def draw_w(t, height):
  """Draw the letter W with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  tan_15 = math.tan(radians)
  target_tan = tan_15/2
  angle = math.degrees(math.atan(target_tan))
  side = math.hypot(height, width/4)


  t.lt(90)
  t.fd(height)
  t.rt(180-angle)
  t.pd()
  t.fd(side)
  t.lt(180-2*angle)
  t.fd(side)
  t.rt(180-2*angle)
  t.fd(side)
  t.lt(180-2*angle)
  t.fd(side)
  t.rt(180-angle)
  t.pu()
  t.fd(height)
  t.lt(90)
  t.fd(width+10)

def draw_x(t, height):
  """Draw the letter X with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  angle = math.degrees(math.atan(width/height))
  leg = math.hypot(width, height)

  t.lt(90-angle)
  t.pd()
  t.fd(leg)
  t.pu()
  t.bk(leg/2)
  t.lt(2*angle)
  t.pd()
  t.fd(leg/2)
  t.pu()
  t.bk(leg/2)
  t.pd()
  t.bk(leg/2)
  t.rt(90+angle)
  t.pu()
  t.fd(width+10)

def draw_y(t, height):
  """Draw the letter Y with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  angle = math.degrees(math.atan(width/height))
  leg = math.hypot(width/2, height/2)

  t.fd(width/2)
  t.lt(90)
  t.pd()
  t.fd(height/2)
  t.lt(angle)
  t.fd(leg)
  t.pu()
  t.bk(leg)
  t.rt(2*angle)
  t.pd()
  t.fd(leg)
  t.pu()
  t.bk(leg)
  t.lt(angle)
  t.bk(height/2)
  t.rt(90)
  t.fd((2*width+10)-width/2)

def draw_z(t, height):
  """Draw the letter Z with the given height.
  Moves to the next letter position"""

  radians = math.radians(15)
  width = (height * math.tan(radians)) * 2
  angle = math.degrees(math.atan(width/height))
  leg = math.hypot(width, height)

  t.lt(90)
  t.fd(height)
  t.rt(90)
  t.pd()
  t.fd(width)
  t.rt(90+angle)
  t.fd(leg)
  t.lt(90+angle)
  t.fd(width)




if __name__ == '__main__':
  world = TurtleWorld()
  bob = Turtle()
  bob.delay = 0.01

  bob.pu()
  bob.bk(160)
  bob.pd()

  height = 80

  draw_a(bob, height)
  draw_b(bob, height)
  draw_c(bob, height)
  draw_d(bob, height)
  draw_e(bob, height)
  draw_f(bob, height)
  draw_g(bob, height)
  draw_h(bob, height)
  draw_i(bob, height)
  draw_j(bob, height)
  draw_k(bob, height)
  draw_l(bob, height)
  draw_m(bob, height)
  draw_n(bob, height)
  draw_o(bob, height)
  draw_p(bob, height)
  draw_q(bob, height)
  draw_r(bob, height)
  draw_s(bob, height)
  draw_t(bob, height)
  draw_u(bob, height)
  draw_v(bob, height)
  draw_w(bob, height)
  draw_x(bob, height)
  draw_y(bob, height)
  draw_z(bob, height)



  wait_for_user()
