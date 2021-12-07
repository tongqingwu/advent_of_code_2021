import collections


def print_school(school):
    print(school)
    line = ''
    for n in range(9):
        if school[n] != -1:
            line += (str(n) + ',') * school[n]
     
    print(line)
 
           
class Fish():
    def __init__(self, input_file, days):
        self.nums = []
        self.days = days
        self.school = [-1] * 9

        self.cnt = 0
        with open(input_file) as f:
            for line in f:
                self.cnt += 1
                line = line.rstrip()
                self.nums = [int(x) for x in line.split(',')]
        # print(self.nums)
        c = collections.Counter(self.nums)
        for k, v in c.items():
            self.school[k] = v
       
        # print(self.school)
   
    def get_new_school(self):
        new_school = self.school.copy()
        for n in range(1, 9):
            new_school[n - 1] = self.school[n] if self.school[n] != -1 else -1

        if new_school[6] != -1:
            if self.school[0] != -1:
                new_school[6] += self.school[0]
        else:
            new_school[6] = self.school[0]
        new_school[8] = self.school[0]

        # print_school(new_school)
        return new_school

    def get_fish_by_days(self):
        day = 0
        while (day < self.days):
            day += 1
            # print('day ---- {}'.format(day))
            self.school = self.get_new_school()
           
        print(sum(self.school))
           
           
fish = Fish('d6.txt', 80)
fish.get_fish_by_days()
fish = Fish('d6.txt', 256)
fish.get_fish_by_days()
