class Lava():
    def __init__(self, input_file):
        self.num_dict = dict()
        self.cost_dict = dict()
        self.lows = 0
        self.low_points = set()  # list of (i,j)
        self.nums = []
        self.dict_basins = dict()  # {(0, 1): {(0, 1), (1, 2) ...)}}
        self.checked_points = set()
        cnt = 0
        with open(input_file) as f:
            for line in f:
                cnt +=1
                line = line.rstrip()
                self.nums.append([int(x) for x in line])
        self.num_rows = len(self.nums)
        self.num_cols = len(self.nums[0])
    
    def is_smaller_than_all(self, i, j):
        if self.is_lower_than_up(i, j) and self.is_lower_than_down(i, j) and self.is_lower_than_left(i, j) and self.is_lower_than_right(i, j):
            return True
        else:
            return False
        
    def part1(self):
        for i in range(self.num_rows):  # row
            for j in range(self.num_cols):
                if not self.is_smaller_than_all(i, j):
                    continue
                # print('{} -------------- '.format(self.nums[i][j]))
                self.low_points.add((i, j))
                self.lows += 1
                self.lows += self.nums[i][j]
        # print(self.low_points)
        print(self.lows)

    def part2(self):
        for l in self.low_points:
            self.dict_basins[l] = set()
            self.dict_basins[l].add(l)

            # print('low : ---------- {}'.format(l))
            self.checked_points.add(l)
            self.count_left(l, l)
            self.count_down(l, l)
            self.count_up(l, l)
            self.count_right(l, l)

        # print(self.dict_basins)   
        
        sizes = []
        for k, v in self.dict_basins.items():
            # print('basins: {}->{}'.format(k, self.nums[k[0]][k[1]]))
            # print(v)
            # print(len(v))
            sizes.append(len(v))
        
        sizes.sort(reverse=True)
        print(sizes)
        print(sizes[0] * sizes[1] * sizes[2])
            
    # parent lowest point, plus current point       
    def count_up(self, lp, l):
        self.dict_basins[lp].add(l)
        self.checked_points.add(l)
        i = l[0]
        j = l[1]
        ii = i - 1
        while ii > 0 or ii == 0:
            # print('Up to ({},{}) -> {}'.format(ii, j, self.nums[ii][j]))
            if self.nums[ii][j] == 9 or (ii, j) in self.dict_basins[lp]:
                break
            else:
                # if self.is_lower_than_up(ii, j):
                p = (ii, j)
                # print('Add({},{}) -> {}'.format(ii, j, self.nums[ii][j]))
                self.dict_basins[lp].add(p)  
                self.checked_points.add(p)
                self.count_right(lp, p)
                self.count_left(lp, p)

            ii -= 1
    
    def count_down(self, lp, l):
        self.dict_basins[lp].add(l)
        self.checked_points.add(l)
        i = l[0]
        j = l[1]
        ii = i + 1
        while ii < self.num_rows:
            # print('Down to ({},{}) -> {}'.format(ii, j, self.nums[ii][j]))
            if self.nums[ii][j] == 9 or (ii, j) in self.dict_basins[lp]:
                break
            else:
                # if self.is_lower_than_down(ii, j):
                p = (ii, j)
                # print('add ({},{}) -> {}'.format(ii, j, self.nums[ii][j]))
                self.dict_basins[lp].add(p)
                self.checked_points.add(p)
                self.count_right(lp, p)
                self.count_left(lp, p)

            ii += 1
        
    def count_left(self, lp, l):
        self.dict_basins[lp].add(l)
        self.checked_points.add(l)
        i = l[0]
        j = l[1]
        jj = j - 1
        while jj > 0 or jj == 0:
            # print('Left to ({}, {})->{}'.format(i, jj, self.nums[i][jj]))
            if self.nums[i][jj] == 9 or (i, jj) in self.dict_basins[lp]:
                break
            else:
                p = (i, jj)
                # print('Add ({}, {})->{}'.format(i, jj, self.nums[i][jj]))
                self.dict_basins[lp].add(p)
                self.checked_points.add(p)
                self.count_down(lp, p)
                self.count_up(lp, p)
            jj -= 1
        
    def count_right(self, lp, l):
        self.dict_basins[lp].add(l)
        self.checked_points.add(l)
        i = l[0]
        j = l[1]
        jj = j + 1
        while jj < self.num_cols:
            # print('Right to ({}, {})->{}'.format(i, jj, self.nums[i][jj]))
            if self.nums[i][jj] == 9 or (i, jj) in self.dict_basins[lp]:
                break
            else:
                if self.is_lower_than_right(i, jj):
                    p = (i, jj)
                    # print('add to ({}, {})->{}'.format(i, jj, self.nums[i][jj]))
                    self.dict_basins[lp].add(p)
                    self.checked_points.add(p)
                    self.count_down(lp, p)
                    self.count_up(lp, p)
                else:
                    break
            jj += 1
        
    def is_lower_than_left(self, i, j):
        l = self.nums[i][j]
        left = j - 1
        if left > 0 or left == 0:
            if l > self.nums[i][left] or l == self.nums[i][left]:
                return False
        return True

    def is_lower_than_right(self, i, j):
        l = self.nums[i][j]
        right = j + 1
        if right < self.num_cols - 1 or right == self.num_cols - 1:
            if l > self.nums[i][right] or l == self.nums[i][right]:
                return False
        return True
    
    def is_lower_than_up(self, i, j):
        l = self.nums[i][j]
        up = i - 1
        if up > 0 or up == 0:  # has up neibour
            if l > self.nums[up][j] or l == self.nums[up][j]:
                return False
        return True
    
    def is_lower_than_down(self, i, j):
        l = self.nums[i][j]
        down = i + 1
        if down < self.num_rows - 1 or down == self.num_rows - 1:
            if l > self.nums[down][j] or l == self.nums[down][j]:
                return False
        return True


lava = Lava('d9.txt')     
lava.part1()
lava.part2()
