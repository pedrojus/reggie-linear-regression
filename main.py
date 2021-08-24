# The function get_y returns the result of the following formula y = m*x+b
def get_y(m, b, x):
    return m * x + b


# Print statements to test functionality of get_y function
# print(get_y(1, 0, 7) == 7)
# print(get_y(5, 10, 3) == 25)

# This function calculates the error between a point and a line
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    result = get_y(m, b, x_point)
    diff = result - y_point
    return abs(diff)


# This is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
# print(calculate_error(1, 0, (3, 3)))
# The point (3, 4) should be 1 unit away from the line y = x:
# print(calculate_error(1, 0, (3, 4)))
# The point (3, 3) should be 1 unit away from the line y = x - 1:
# print(calculate_error(1, -1, (3, 3)))
# The point (3, 3) should be 5 units away from the line y = -x + 1:
# print(calculate_error(-1, 1, (3, 3)))
