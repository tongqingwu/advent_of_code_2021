import re
import collections
from collections import Counter


def get_all_points(lines):
    points = []
    for line in lines:
        points += get_points_by_line(line)
    c = Counter(points)
    print(c)
    
    p = 0
    for k, v in c.items():
        print('k: {}, v: {}'.format(k, v))
        if v > 1:
            p += 1
    print(p)


def get_points_by_line(t):
    points = []
    print('-------------new line: {}'.format(t))
    x1 = n_x = t[0][0]
    y1 = n_y = t[0][1]
    x2 = t[1][0]
    y2 = t[1][1]

    if x1 == x2:  # vertical line
        points = [(x1, y1)]
        if y1 < y2:
            while n_y < y2:
                n_y += 1
                points.append((x1, n_y))
        else:
            while n_y > y2:
                n_y -= 1
                points.append((x1, n_y))
        
        print('v line {}'.format(points))
    elif y1 == y2:
        points = [(x1, y1)]
        if x1 < x2:
            while n_x < x2:
                n_x += 1
                points.append((n_x, y1))
        else:
            while n_x > x2:
                n_x -= 1
                points.append((n_x, y1))
        print('h line {}'.format(points))
    else:
        x_diff = abs(x2 - x1)
        y_diff = abs(y2 - y1)
        if x_diff == y_diff: 
            points = [(x1, y1)]
            if x1 < x2 and y1 < y2:
                while n_x < x2 and n_y < y2:
                    n_x += 1
                    n_y += 1
                    points.append((n_x, n_y))
            elif x1 < x2 and y1 > y2:
                while n_x < x2 and n_y > y2:
                    n_x += 1
                    n_y -= 1
                    points.append((n_x, n_y))
            elif x1 > x2 and y1 > y2:
                while n_x > x2 and n_y > y2:
                    n_x -= 1
                    n_y -= 1
                    points.append((n_x, n_y))
            elif x1 > x2 and y1 < y2:
                while n_x > x2 and n_y < y2:
                    n_x -= 1
                    n_y += 1
                    points.append((n_x, n_y))
        print('d line {}'.format(points))

    return points


def main():
    lines = []   # two dimension arrays.
    with open('d5.txt') as f:
        for line in f:
            line = line.rstrip()
            row = re.search(r'(\d+),(\d+) -> (\d+),(\d+)', line)
            if row:
                x1 = int(row.group(1))
                y1 = int(row.group(2))
                x2 = int(row.group(3))
                y2 = int(row.group(4))

                tmp = ((x1, y1), (x2, y2))
                # print(tmp)
                lines.append(tmp)
#        print(lines)

        get_all_points(lines)
          

if __name__ == '__main__':
    main()
