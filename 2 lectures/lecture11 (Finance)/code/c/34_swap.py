i = 10
j = 24

# TODO: swap these two values without additional storage, and without
# the syntax `i, j = j, i`.

i = j - i  # 14
j = j - i  # 10
i = i + j  # 24
print(i, j)

