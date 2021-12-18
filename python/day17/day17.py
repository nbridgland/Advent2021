X_MIN = 150
X_MAX = 193
Y_MIN = -136
Y_MAX = -86


def should_continue_simulation(x, y, x_min=X_MIN, y_min=Y_MIN, x_max=X_MAX, y_max=Y_MAX):
    if x_min > 0:
        if x > x_max:
            return False, False
    else:
        if x < x_min:
            return False, False
    if y < y_min:
        return False, False

    if x_min <= x <= x_max and y_min <= y <= y_max:
        return False, True

    return True, False

def simulate_path(x_vel, y_vel, x_min=X_MIN, y_min=Y_MIN, x_max=X_MAX, y_max=Y_MAX):
    x, y = (0, 0)
    y_max = 0
    while should_continue_simulation(x, y)[0]:
        x += x_vel
        y += y_vel
        y_vel -= 1
        if x_vel > 0:
            x_vel -= 1
        if x_vel < 0:
            x_vel += 1
        if y > y_max:
            y_max = y
    if should_continue_simulation(x, y)[1]:
        return y_max
    else:
        return None

def contains_triangle_number(x_min, x_max):
    k = 0
    triangle_number = 0
    while triangle_number < x_max:
        if triangle_number > x_min:
            return triangle_number, k
        k += 1
        triangle_number += k
    return False


#trajectory:
#[(velocity + velocity - 1 + ... + velocity - velocity)] + [-1 - 2 - 3 - .. - velocity]

#Max velocity = -(y_min + 1) as long as that provides space for x to show up

x_coord = contains_triangle_number(X_MIN, X_MAX)[1]


print("Part 1: ", simulate_path(x_coord, -(Y_MIN+1)))


count_options = 0
for y_vel in range(Y_MIN, -Y_MIN):
    for x_vel in range(contains_triangle_number(X_MIN, X_MAX)[1], X_MAX+1):
        if simulate_path(x_vel, y_vel) is not None:
            count_options += 1

print("Part 2: ", count_options)