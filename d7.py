import collections
 

def get_sum(steps):
    sum = 0
    for i in range(steps):
        sum += i + 1
       
    return sum


class Crab():
    def __init__(self, input_file):
        self.num_dict = dict()
        self.cost_dict = dict()
        self.keys = []
        self.far = 0
        nums = []
        cnt = 0
        with open(input_file) as f:
            for line in f:
                cnt +=1
                line = line.rstrip()
                if cnt == 1:
                    nums = [int(x) for x in line.split(',')]
                    break
        # print(nums)
        c = collections.Counter(nums)
        self.num_dict = {k: v for k, v in sorted(c.items(), key=lambda item: item[1], reverse=True)}
       
        # print(self.num_dict)
        self.keys = list(self.num_dict.keys())
        self.far = sorted(self.keys, reverse=True)[0]
        # print(self.far)
       
    def get_all_cost_dict(self):  
        for k in self.num_dict.keys():
            ky, cost = self.get_cost(k, part2=False)
            self.cost_dict[ky] = cost
        self.show_cost()
     
    def get_all_cost_dict2(self):  
        for k in list(range(0, self.far + 1)):
            ky, cost = self.get_cost(k)
            self.cost_dict[ky] = cost
        self.show_cost()
       
    def show_cost(self):
        print(self.cost_dict)
        s = {k: v for k, v in sorted(self.cost_dict.items(), key=lambda item: item[1], reverse=False)}
        f = list(s.values())
        # print(f)
        f = sorted(f)
        print(f[0])
       
    def get_cost(self, key, part2=True):  
        cost = 0
        for k in self.keys:
            if part2:
                cost += get_sum(abs(k - key)) * self.num_dict[k]
            else:
                cost += abs(k - key) * self.num_dict[k]
        return key, cost
           

# s = get_sum(2)    
# print(s)
crab = Crab('d7.txt')
crab.get_all_cost_dict()
crab.get_all_cost_dict2()
