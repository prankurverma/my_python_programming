class Robot():
    def __init__(self, currpos, head, inst):
        self.currpos = currpos
        self. head = head
        self.inst = inst
        
    def direction(self, inst, head):
        dirset = ['N','E','S','W']
        i = dirset.index(head)
        if inst == 'L':
            i = i-1
            #print(i)
        if inst == 'R':
            i = i+1
        return dirset[(4+i)%4]

    def move(self, pos, head):
        if head == 'N':
            pos[1] +=1
        if head == 'E':
            pos[0] +=1
        if head == 'W':
            pos[0] -=1
        if head == 'S':
            pos[1] -=1
        return pos


    def position(self):
        newpos = []
        newhead = ''
        for i in self.inst:
            if i == 'L' or 'R':
                newhead =  self.direction(i, self.head)
                self.head = newhead
            if i == 'M':
                newpos = self.move(self.currpos, self.head)
                self.currpos = newpos
                newhead = self.head
        print(newhead)
        print(newpos)   

currpos = [3,3]
head = 'E'
inst = ['M','M','R','M','M','R','M','R','R','M']
p1 = Robot(currpos, head, inst)
p1.position()
