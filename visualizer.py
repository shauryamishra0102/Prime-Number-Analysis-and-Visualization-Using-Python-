# visualizer.py

import matplotlib.pyplot as plt
from primes import generate_primes
import numpy as np



def visualize_prime_scatter(n):
    primes = generate_primes(n)
    x = range(len(primes))
    y = primes

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, s=155)
    plt.title(f"Prime Numbers up to {n}")
    plt.xlabel("Index")
    plt.ylabel("Prime Value")
    plt.grid(True)

    save_path = "assets/saved_plots/prime_scatter.png"
    plt.savefig(save_path)
    print(f"Saved scatter plot to: {save_path}")

    plt.show()


def visualize_ulam_spiral(n):
    primes = set(generate_primes(n))

    size = int(np.ceil(np.sqrt(n)))
    grid = np.zeros((size, size))

    x = y = size // 2
    dx, dy = 0, -1

    for val in range(1, size * size + 1):
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = 1 if val in primes else 0

        if x == y or (x < y and x + y == size - 1) or (x > y and x + y == size):
            dx, dy = -dy, dx

        x += dx
        y += dy

    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap="viridis")
    plt.title("Ulam Prime Spiral")
    plt.axis("off")

    save_path = "assets/saved_plots/ulam_spiral.png"
    plt.savefig(save_path)
    print(f"Saved Ulam Spiral to: {save_path}")

    plt.show()
