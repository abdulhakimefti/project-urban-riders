class RideManager:
    def __init__(self):
        print('Ride manager activated')
        self.__availableCar = []
        self.__availableBike = []
        self.__availableCng = []
    
    def match_a_vahicle(self):
        pass

    def add_a_vehicle(self,vehicle,vehicle_type):
        if vehicle_type == 'car':
            self.__availableCar.append(vehicle)
        elif vehicle_type== 'bike':
            self.__availableBike.append(vehicle)
        elif vehicle_type=='cng':
            self.__availableCng.append(vehicle)
    def available_vehicle(self):
        return self.__availableCar
    
    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type=='car':
            if len(self.__availableCar)==0:
                print('sry no cars availble')
                return False
            for car in self.__availableCar :
                 if abs(rider.location-car.driver.location) < 30:
                   print('find a match for you')
                   return True
uber = RideManager()
    