
'''
The Python class is similar to Javascript class,
The structure of Python class like:
'''
class Cars:
    def __init__(self,color,seat): # "self" as the first attribute is needed.
        self.color = color
        self.seat = seat
    
    def drive(self): # "self" as the first attribute is needed.
        print(f"My car is {self.color} and {self.seat} seats.")

'''
In Javascript, the class is like:

class Cars {
    consturctor(color,seat){
        this.color = color
        this.seat =seat
    }
    drive(){
        console.log(`My car is ${this.color} and ${this.seat} seats.`)
    }
}

The "self" attribute is similar to Javascript's "this" keyword, but the usecases is different.
In python, the constructor and all the method behide the class should have "self" keyword as the first attribute.
Then in Javascript, it should't.

'''

toyota = Cars("Red",4)

toyota.drive()