class Stack():

    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else :
            self.items = ls

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def move(n,from_rod, to_rod, aux_rod):
    if n == 1:
        print("move 1 from ",from_rod,"to",to_rod)
        change_pos(from_rod, to_rod)
        return
    move(n-1, from_rod, aux_rod, to_rod)
    print("move",n,"from ",from_rod,"to",to_rod)
    change_pos(from_rod, to_rod)
    move(n-1, aux_rod, to_rod, from_rod)

def Display(n, lstA, lstB, lstC) :
    temp = [[i for i in lstA.items],[i for i in lstB.items],[i for i in lstC.items]]
    for i in range(len(temp)) :
        for j in range(n+1) :
            if len(temp[i]) != n+1 : 
                temp[i].append("|")
    for i in reversed(range(n+1)) :
        print(temp[0][i], "", temp[1][i], "", temp[2][i])

def change_pos(form, des) :
    if form == 'A' : form = listA
    if form == 'B' : form = listB
    if form == 'C' : form = listC
    if des == 'A' : des = listA
    if des == 'B' : des = listB
    if des == 'C' : des = listC
    des.push(form.pop())
    Display(n, listA, listB, listC)



listA = Stack()
listB = Stack()
listC = Stack()

n = int(input("Enter Input : "))

for i in reversed(range(n+1)) : # initial rod
    if i != 0 : listA.push(i) 

Display(n, listA, listB, listC)
move(n, 'A', 'C', 'B');