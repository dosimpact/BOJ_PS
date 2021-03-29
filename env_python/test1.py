x, x_span = 0, 9
y, y_span = 0, 9


for i in range(x, x + x_span, x_span // 3):
    for j in range(y, y + y_span, y_span // 3):
        print(i, j)
