# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.

T = lambda n: n * (n + 1) // 2
P = lambda n: n * (3 * n - 1) // 2
H = lambda n: n * (2 * n - 1)

t_index, p_index, h_index = 286, 0, 0
t_value, p_value, h_value = T(t_index), 0, 0

while True:
    if t_value == p_value == h_value:
        print(t_index, t_value)
        print(p_index, p_value)
        print(h_index, h_value)
        break

    smallest = min(t_value, p_value, h_value)
    if t_value == smallest:
        t_index += 1
        t_value = T(t_index)

    if p_value == smallest:
        p_index += 1
        p_value = P(p_index)

    if h_value == smallest:
        h_index += 1
        h_value = H(h_index)
