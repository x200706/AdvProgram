def find_final_point(x1, y1, x2, y2, x3, y3):
    # D = A + C - B B->x2, y3
    return x1 + x3 - x2, y1 + y3 - y2

while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
        public_x, public_y = 0, 0
        #找出公共頂點
        if x1 == x2 and y1 == y2:
            px, py = find_final_point(x3, y3, x1, y1, x4, y4)
        elif x1 == x3 and y1 == y3:
            px, py = find_final_point(x2, y2, x1, y1, x4, y4)
        elif x1 == x4 and y1 == y4:
            px, py = find_final_point(x2, y2, x1, y1, x3, y3)
        elif x2 == x3 and y2 == y3:
            px, py = find_final_point(x1, y1, x2, y2, x4, y4)
        elif x2 == x4 and y2 == y4:
            px, py = find_final_point(x1, y1, x2, y2, x3, y3)
        elif x3 == x4 and y3 == y4:
            px, py = find_final_point(x1, y1, x3, y3, x2, y2)

        print(f"{px:.3f} {py:.3f}")
    except EOFError:
        break