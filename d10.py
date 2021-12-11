db = {'<' : '>', '{' : '}', '(' : ')', '[' : ']'}

scores = {')' : 3, ']' : 57, '}': 1197, '>': 25137}
s2 = {')' : 1, ']' : 2, '}': 3, '>': 4}


def replace_line(line):
    ss = {(k + v) for k, v in db.items()} 
    while any(x in line for x in ss):
        for x in ss:
            line = line.replace(x, '')
    return line


def get_new_score(score, value):
    return score * 5 + value

    
class Syntax():
    def __init__(self, input_file):
        self.scores = 0
        self.list_scores = []  # part2
        with open(input_file) as f:
            for line in f:
                line = line.rstrip()
                
                self.check_line(line)

        print('Part 1: {}'.format(self.scores))
        # print('p2')
        #print(self.list_scores)
        self.list_scores.sort()
        # print(self.list_scores)
        m =  (len(self.list_scores) - 1)/2
        # print(m)
        print('Part 2: {}'.format(self.list_scores[int(m)]))
        
    def check_line(self, line):
        line = replace_line(line)
        # print(line)
        
        for l in line:
            if l in db.keys():
                la = l
            else:
                # print('find {}'.format(la))
                self.scores += scores[l]
                return 
            
        rs = line[::-1]
        score = 0
        for r in rs:
            score = get_new_score(score, s2[db[r]])
            
        # print(score)
        self.list_scores.append(score)
                   
s = Syntax('d10.txt')
