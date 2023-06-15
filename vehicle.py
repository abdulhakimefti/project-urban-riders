from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    speed ={
        'car':30,
        'bike':50,
        'cng':15
    }
    def __init__(self,license_plate, vehicle_type,rate,driver):
        self.license_plate = license_plate
        self.vehicle_type= vehicle_type
        self.status= 'available'
        self.rate = rate
        self.driver=driver
        self.speed = self.speed[vehicle_type]
    
    @abstractclassmethod
    def start_driving(self):
        pass
    @abstractclassmethod
    def trip_finish(self):
        pass


class Car(Vehicle):
    def __init__(self,license_plate,vehicle_type,rate,driver):
        super().__init__(license_plate,vehicle_type,rate,driver)
    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.licese_plate,'started')
    
    def trip_finish(self):
        print(self.vehicle_type,self.licese_plate,'finished')
        self.status= 'available'


class Bike(Vehicle):
    def __init__(self,license_plate,vehicle_type,rate,driver):
        super().__init__(license_plate,vehicle_type,rate,driver)
    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.licese_plate,'started')
    
    def trip_finish(self):
        print(self.vehicle_type,self.licese_plate,'finished')
        self.status= 'available'


class Cng(Vehicle):
    def __init__(self,license_plate,vehicle_type,rate,driver):
        super().__init__(license_plate,vehicle_type,rate,driver)
    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.licese_plate,'started')
    
    def trip_finish(self):
        print(self.vehicle_type,self.licese_plate,'finished')
        self.status= 'available'
