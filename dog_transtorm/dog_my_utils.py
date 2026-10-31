import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

INF = 600
LEN = 100


def draw_axis(ax):
  ax.axhline(0, color='black', alpha=0.3)
  ax.axvline(0, color='black', alpha=0.3)
  ax.set_xlim(-INF, INF)
  ax.set_ylim(-INF, INF)
  ax.set_aspect('equal')


def draw_rectangle(ax, p1, p2, p3, p4):
  my_polygon = Polygon([p1, p2, p3, p4])
  ax.add_patch(my_polygon)


def translate(p, dx, dy):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[1.0, 0.0, dx], [0.0, 1.0, dy], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


def rotate(p, theta):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[np.cos(theta), -np.sin(theta), 0.0], [np.sin(theta), np.cos(theta), 0.0], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


def scale(p, sx, sy):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[sx, 0.0, 0.0], [0.0, sy, 0.0], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


def shear_x(p, sx):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[1.0, sx, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


def shear_y(p, sy):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[1.0, 0.0, 0.0], [sy, 1.0, 0.0], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


def reflect_x(p):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


def reflect_y(p):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


def reflect_origin(p):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


def reflect_yx(p):
  hp = np.array([p[0], p[1], 1.0])
  m = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
  q = np.dot(m, hp)
  q = np.array([q[0], q[1]])
  return q


# 검은색 사각형 그리기 (draw_rectangle 과 같은데 색만 검정)

def draw_black_rectangle(ax, p1, p2, p3, p4):
  ax.add_patch(Polygon([p1, p2, p3, p4], facecolor='black', edgecolor='black'))


def draw_piece(ax, x, y, angle, w, h):
  p1 = np.array([0, 0])
  p2 = np.array([LEN, 0])
  p3 = np.array([LEN, LEN])
  p4 = np.array([0, LEN])
  q1 = translate(p1, -LEN/2, -LEN/2)
  q2 = translate(p2, -LEN/2, -LEN/2)
  q3 = translate(p3, -LEN/2, -LEN/2)
  q4 = translate(p4, -LEN/2, -LEN/2)
  q1 = scale(q1, w/LEN, h/LEN)
  q2 = scale(q2, w/LEN, h/LEN)
  q3 = scale(q3, w/LEN, h/LEN)
  q4 = scale(q4, w/LEN, h/LEN)
  q1 = rotate(q1, angle)
  q2 = rotate(q2, angle)
  q3 = rotate(q3, angle)
  q4 = rotate(q4, angle)
  q1 = translate(q1, x, y)
  q2 = translate(q2, x, y)
  q3 = translate(q3, x, y)
  q4 = translate(q4, x, y)

  draw_black_rectangle(ax, q1, q2, q3, q4)



def draw_object(ax):
  face = [(-265, -5, -1.61, 94), (-254, -114, -1.36, 126), (-202, -224, -0.90, 125),
          (-107, -287, -0.25, 114), (26, -300, 0.02, 156), (156, -283, 0.30, 109),
          (234, -218, 1.08, 110), (266, -117, 1.45, 105), (268, -14, 1.67, 102)]
  top  = [(-75, 268, 0.35, 104), (13, 286, 0.00, 78), (89, 268, -0.44, 82)]
  lear = [(-198, 252, 3.11, 111), (-292, 218, -2.40, 106), (-344, 140, -1.87, 88),
          (-332, 79, -0.61, 63), (-266, 71, 0.24, 80), (-211, 94, 0.70, 42)]
  rear = [(182, 260, 0.11, 118), (283, 228, -0.75, 115), (339, 150, -1.22, 83),
          (336, 78, -2.07, 74), (286, 44, -3.08, 65), (228, 56, 2.63, 58)]
  mouth = [(-34, -254, -0.07, 36), (-10, -247, 0.98, 19),
           (12, -249, -0.52, 39), (34, -254, 0.72, 14)]
  for (x, y, a, w) in face + top + lear + rear:
    draw_piece(ax, x, y, a, w + 14, 14)
  for (x, y, a, w) in mouth:
    draw_piece(ax, x, y, a, w + 9, 9)
  for ex in (-139, 139):
    draw_piece(ax, ex, 56, 0, 40, 40)
    draw_piece(ax, ex, 56, np.pi/4, 40, 40)
  draw_piece(ax, -3, -204, 0, 14, 14)


def main():
  fig, ax = plt.subplots(figsize=(7, 7))
  draw_axis(ax)
  draw_object(ax)
  plt.show()
