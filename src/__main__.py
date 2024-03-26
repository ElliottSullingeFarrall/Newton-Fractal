from parallel import parallel_map

from numpy import prod, linspace, meshgrid, vectorize
import matplotlib.pyplot as plt

MAX_ITER = 10
TOL = 1e-6

roots = [-1, 1+1j, +1]
p0 = lambda z: prod([(z - root) for root in roots])
p1 = lambda z: sum([prod([(z - root) for root in roots if root != r]) for r in roots])

def newton_raphson(z0):
    z = z0
    for _ in range(MAX_ITER):
        z_new = z - p0(z) / p1(z)

        if abs(z_new - z) < TOL:
            return z_new
        else:
            z = z_new
    return 0

def fractal(z):
    errors = [abs(newton_raphson(z) - root) for root in roots]
    root = errors.index(min(errors))
    return root
        


GRID_SIZE = 1000

X, Y = meshgrid(linspace(-5, +5, GRID_SIZE), linspace(-5, +5, GRID_SIZE))
Z = parallel_map(vectorize(fractal), X + 1j*Y)

fig, ax = plt.subplots()
ax.imshow(Z)
fig.savefig('newton.png')