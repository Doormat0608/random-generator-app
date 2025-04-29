import numpy as np

def sample_linear(a, b, size, xmin, xmax):
    Z = a/2 * (xmax**2 - xmin**2) + b * (xmax - xmin)
    u = np.random.rand(size)
    if abs(a) < 1e-8:
        return xmin + (xmax - xmin) * u
    A = a/2
    B = b
    C = -u * Z - b * xmin + a/2 * xmin**2
    disc = B**2 - 4 * A * C
    x = (-B + np.sqrt(disc)) / (2 * A)
    return x

def generate_mixed_distribution(a1, b1, a2, b2, xmin, xmax, w, N):
    u_mix = np.random.rand(N)
    n1 = np.sum(u_mix < w)
    s1 = sample_linear(a1, b1, n1, xmin, xmax)
    s2 = sample_linear(a2, b2, N - n1, xmin, xmax)
    samples = np.concatenate([s1, s2])
    np.random.shuffle(samples)
    return samples
