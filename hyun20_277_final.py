#-------------------------------------------------------------------------------
# Name: Henry Yun
# Final Exam
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
def highest_grade(gradebook, major, level):
    p = 0
    for i in gradebook:
        elm = set(gradebook.get(i))
        for j in elm:
            if j[:2] == major and int(j[2:3]) == level:
                t = gradebook[i][j]
                if t >= p:
                    p = t
                    result = (i,j,p)
            elif level != int(j[2:3]) and p == 0:
                result = False
    return result


def create_graph(xs):
    t = []
    for i in range(len(xs)):
        g = []
        for j in range(xs[i]):
            g.append(0)
        t.append(g)
    return t


def unique_nums(filename):
    s = []
    file = open(filename)
    for line in file:
        line = line.replace('\n','')
        if int(line) in s:
            continue
        else:
            s.append(int(line))
    file.close()
    return s


def prolific_author(books):
    elm = []
    dup = []
    final = []
    for i in books.values():
        if i in elm:
            dup.append(i)
        else:
            elm.append(i)
    for j in range(len(dup)):
        for i in books.keys():
            if books.get(i) == dup[j]:
                final.append(i)
        return final
    
    
def sum_items(xs):
    add = 0
    for i in range(len(xs)):
        for j in range(len(xs[i])):
            if i != 0 and i != len(xs)-1:
                if j != 0 and j != len(xs[i]) - 1 :
                    if xs[i][j] % 2 != 0:
                        add += xs[i][j]
    return add


def fail_class(quizzes, midterm_exam, final_exam):
    if final_exam >= 60:
        return False
    if final_exam < 60:
        if quizzes > midterm_exam or quizzes > final_exam:
            if (((final_exam * 2) + midterm_exam)/300) > 0.65:
                return False
        else:
            return True
        

def plot(filename,xs):
    g = xs[0]
    for i in range(1,len(xs)):
        if xs[i] > g:
            g = xs[i]
    file = open(filename,'w')
    for i in range(g):
        if i >0:
            file.write('\n')
        for j in range(len(xs)):
            if xs[j] > 0:
                file.write('X')
                xs[j] = xs[j] - 1
            elif xs[j] == 0:
                file.write(' ')
