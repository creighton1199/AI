import math

class Geometry:
    
    numGeometry=0;
    #global variable to get all of type Geometry
    
    def __init__(self, name = "Shape", points = None):
        self.name = name
        # name is string that is a name of geometry
        self.points = points
        # points are a list of tuple points = [(x0, y0), (x1, y1), ...]
        Geometry.numGeometry+=1
		#will add one to global variable numGeomtry when new instance is created
        
    def calculate_area(self):
        pass
    
    def get_name(self):
        return self.name

    @classmethod
    def count_number_of_geometry(cls):
        # TODO: Your task is to implement the class method
        # to get the number of instances that have already created
        return (cls.numGeometry)
        
c=Geometry()

#print(c.__dict__)
    
class Triangle(Geometry):
    
    def __init__(self, a, b, c):
        super(Triangle, self).__init__("Triangle",[a,b,c])
    
    def calculate_area(self):
        
        side1=self.getSideLength(self.points[0],self.points[1])  #gets side length from a-b
        
        side2=self.getSideLength(self.points[1],self.points[2])  #gets side length from b-c
        
        side3=self.getSideLength(self.points[0],self.points[2])  #gets side legnth from a-c
        
        semiPerimeter=(side1+side2+side3)/2
        
        return math.sqrt(semiPerimeter*(semiPerimeter-side1)*(semiPerimeter-side2)*(semiPerimeter-side3)) #gets area using heron theorem
        
    
    def getSideLength(self,point1,point2): #will pass in a,b,c to get a side length
        
        #print(((point2[0]+point1[0])**2)) //What i used to test if my distance formula was working
        #print((point2[1]-point1[1])**2)
        #print (math.sqrt(((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2)))
        
        return math.sqrt(((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2))
    
    
class Rectangle(Geometry):
    
    def __init__(self, a, b):
        super(Rectangle, self).__init__("Rectangle",[a,b])
        
        
    def calculate_area(self):
    
        side1=abs(self.points[0][0]-self.points[1][0])
        #print(side1)
        side2=abs(self.points[0][1]-self.points[1][1])
        #print(side2)
        return side2*side1

class Square(Rectangle):
    
    def __init__(self, a, length):     # a is a tuple that represent a top vertex of a square # length is the side length of a square 
        super(Square, self).__init__(a,[a[0]+length,a[0]+length])
        self.name="Square"

    def calculate_area(self):
        
        side1=abs(self.points[0][0]-self.points[1][0])
        return side1**2

class Circle(Geometry):
    
    def __init__(self, o, r):
        super(Circle, self).__init__("Circle",[o,[o[0]+r,o[0]+r]])
        
    def calculate_area(self):
        return math.pi*((self.points[1][0]-self.points[0][0])**2)

class Polygon(Geometry):
    def __init__(self, points):
        super(Polygon, self).__init__("Polygon",points)
        
    def calculate_area(self):  #my attempt at the shoelace formula I couldnt seem to ever get it to work even though I thought I did it right
        length=len(self.points)
        print (length)
        total=0
        for x in range(length-1):
            total+=self.points[x][0]*self.points[x+1][1]
        total+=self.points[length-1][0]*self.points[0][1]
        
        for x in range(length-1):
            total-=self.points[x][1]*self.points[x+1][0]
        total-=self.points[length-1][1]*self.points[0][0]
        abs(total)
        total/=2
        return total
        

#testing for triangle
tri=Triangle([4.5,5.33],[7,1],[2,1]) #points that can make an equilateral triangle
#print(tri.calculate_area())


#testing for rectangle
rec=Rectangle([0,0],[4,2])
print(rec.__dict__)
#print(rec.calculate_area())

sq=Square([0,0],4)
#print(sq.__dict__)
#print(sq.calculate_area())

cr=Circle([0,0],1)
#print(cr.__dict__)
#print(cr.calculate_area())

po=Polygon([[0,0],[4,4],[0,4],[4,0]])
#print(po.__dict__)
#print(po.calculate_area())   


    


    
    
    
    
    
        