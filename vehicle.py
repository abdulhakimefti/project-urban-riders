from abc import ABC, abstractclassmethod
from time import sleep
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
    def start_driving(self,start,destination):
        pass
    @abstractclassmethod
    def trip_finish(self):
        pass


class Car(Vehicle):
    def __init__(self,license_plate,vehicle_type,rate,driver):
        super().__init__(license_plate,vehicle_type,rate,driver)
    def start_driving(self,start,destination):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate,'started car')
        distance = abs(start-destination)
        for i in range(0,distance):
            sleep(0.01)
            print(f'driving: {self.license_plate} currentPosition: {i} of {distance}')
        self.trip_finish()
    
    def trip_finish(self):
        print(self.vehicle_type,self.license_plate,'finished')
        self.status= 'available'


class Bike(Vehicle):
    def __init__(self,license_plate,vehicle_type,rate,driver):
        super().__init__(license_plate,vehicle_type,rate,driver)
    def start_driving(self,start,destination):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate,'started bike')
        distance = abs(start-destination)
        for i in range(0,distance):
            sleep(0.01)
            print(f'driving: {self.license_plate} currentPosition: {i} of {distance}')
        self.trip_finish()
    
    def trip_finish(self):
        print(self.vehicle_type,self.license_plate,'finished')
        self.status= 'available'


class Cng(Vehicle):
    def __init__(self,license_plate,vehicle_type,rate,driver):
        super().__init__(license_plate,vehicle_type,rate,driver)
    def start_driving(self,start,destination):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate,'started cng')
        distance = abs(start-destination)
        for i in range(0,distance):
            sleep(0.01)
            print(f'driving: {self.license_plate} currentPosition: {i} of {distance}')
        self.trip_finish()
    
    def trip_finish(self):
        print(self.vehicle_type,self.license_plate,'finished')
        self.status= 'available'
