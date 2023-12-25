from itertools import combinations

import numpy as np
import numpy.linalg

lines = open("inputs/24.txt").read().split("\n")
points = []
vectors = []

for line in lines:
    p, v = line.split("@")
    points.append(np.array([int(x) for x in p.split(",")]))
    vectors.append(np.array([int(x) for x in v.split(",")]))

points = np.array(points)
vectors = np.array(vectors)


def will_intersect(minimum, maximum, p1, v1, p2, v2):
    # solving p1 + t*v1 = p2 + s*v2
    A = np.vstack([v1, -v2]).T
    B = p2 - p1
    try:
        t, s = np.matmul(np.linalg.inv(A), B)
        x, y = p1 + t * v1
        return s > 0 and t > 0 and minimum <= x <= maximum and minimum <= y <= maximum
    except np.linalg.LinAlgError:
        return False


print(sum(will_intersect(200000000000000, 400000000000000, p1, v1, p2, v2) for (p1, v1), (p2, v2) in
          combinations(zip(points[:, :2], vectors[:, :2]), 2)))


# p0 - pi = t(vi-v0)
# co-linearity -> cross product is zero: (p0 - pi) x (vi - v0) = 0; ->
# (x0 - xi, y0 - yi, z0 - zi) x (vi_x - v0_x, vi_y - v0_y, vi_z - v0_z)
# cross product: u x v = (u2 * v3 - u3 * v2, u3 * v1 - u1 * v3, u1 * v2 - u2 * v1)
# a = x0, b = y0, c = z0, d = v0_x, e = v0_y, f = v0_z
# (b - y1) * (v1_z - f) - (c - z1) * (v1_y - e) = (b - y2) * (v2_z - f) - (c - z2) * (v2_y - e)
# (c - z1) * (v1_x - d) - (a - x1) * (v1_z - f) = (c - z2) * (v2_x - d) - (a - x2) * (v2_z - f)
# (a - x1) * (v1_y - e) - (b - y1) * (v1_x - d) = (a - x2) * (v2_y - e) - (b - y2) * (v2_x - d)
# and
# (b - y1) * (v1_z - f) - (c - z1) * (v1_y - e) = (b - y3) * (v3_z - f) - (c - z3) * (v3_y - e)
# (c - z1) * (v1_x - d) - (a - x1) * (v1_z - f) = (c - z3) * (v3_x - d) - (a - x3) * (v3_z - f)
# (a - x1) * (v1_y - e) - (b - y1) * (v1_x - d) = (a - x3) * (v3_y - e) - (b - y3) * (v3_x - d)
# expressing first three
# a*0 + b(v1_z - v2_z) + c(v2_y - v1_y) + d*0 + e(z1 - z2) + f(y2 - y1) = z2*v2_y - y2*v2_z + y1*v1_z - z1*v1_y
# and so on


def make_equations(p1, v1, p2, v2):
    x1, y1, z1 = p1[0], p1[1], p1[2]
    x2, y2, z2 = p2[0], p2[1], p2[2]
    v1_x, v1_y, v1_z = v1[0], v1[1], v1[2]
    v2_x, v2_y, v2_z = v2[0], v2[1], v2[2]

    A = np.array([
        [0, v1_z - v2_z, v2_y - v1_y, 0, z1 - z2, y2 - y1],
        [v2_z - v1_z, 0, v1_x - v2_x, z2 - z1, 0, x1 - x2],
        [v1_y - v2_y, v2_x - v1_x, 0, y1 - y2, x2 - x1, 0],
    ])

    B = np.array([
        z2 * v2_y - y2 * v2_z + y1 * v1_z - z1 * v1_y,
        x2 * v2_z - z2 * v2_x + z1 * v1_x - x1 * v1_z,
        y2 * v2_x - x2 * v2_y + x1 * v1_y - y1 * v1_x
    ])

    return A, B


def solve_system():
    A1, B1 = make_equations(points[0], vectors[0], points[1], vectors[1])
    A2, B2 = make_equations(points[0], vectors[0], points[2], vectors[2])
    A = np.vstack([A1, A2])
    B = np.concatenate([B1, B2])

    return np.round(np.sum(np.matmul(np.linalg.inv(A), B)[:3]))


print(f"{solve_system():.0f}")
