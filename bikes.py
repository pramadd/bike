class Bike(object):
    def __init__(self,price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "Total Price is", self.price
        print "Total speed is", self.max_speed
        print "Total miles are",self.miles
        return self
    def ride(self):
        self.miles +=10
        print "riding",self.miles,"miles"
        return self
    def reverse(self):
        if self.miles > 5:
            self.miles -= 5
            print "reversing" ,self.miles ,"miles"
        return self
bike1 = Bike("3000$","56",500)
bike1.ride().ride().ride().reverse().displayInfo()
bike2 =Bike("6000$","80",182)
bike2.ride().ride().reverse().reverse().displayInfo()
bike3 =Bike("7000$","100",890)
bike3.reverse().reverse().reverse().displayInfo()
#bike1.ride()
#bike1.ride()
#bike1.ride()
#bike1.reverse()
#bike1.displayInfo()


#bike2 =Bike("6000$","80",182)
#bike2.ride()
#bike2.ride()
#bike2.reverse()
#bike2.reverse()
#bike2.displayInfo()
#
#
#
#bike3 =Bike("7000$","100",890)
#bike3.reverse()
#bike3.reverse()
#bike3.reverse()
#bike3.displayInfo()



#What would you do to prevent the instance from having negative miles?
# if miles>= 5

#Which methods can return self in order to allow chaining methods?
