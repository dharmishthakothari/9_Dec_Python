class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x}:{self.y}"

    def __add__(self, other):
        # self.x=self.x+other.x
        # self.y=self.y+other.y
        # return Point(self.x,self.y)
        p=Point(0,0)
        p.x=self.x+other.x
        p.y=self.y+other.y
        return p
    def __gt__(self, other):
        if self.x>other.x:
            return Point(self.x,self.y)
        else:
            return Point(other.x,other.y)
    def __mul__(self, other):
        self.x=self.x*other.x
        self.y=self.y*other.y
        return Point(self.x,self.y)

p1=Point(222,22)
p2=Point(111,11)
p3=Point(0,0)
# p3=p1+p2
# print(p3)
# p3=p1*p2
# print(p3)
p3=p1>p2
print(f"Greater {p3}")

