class RideManager:
    def __init__(self):
        print('Ride manager activated')
        self.__tripHistory = []
        self.__availableCar = []
        self.__availableBike = []
        self.__availableCng = []
        self.__privateIncome = 0
    
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
    

    def total_income(self):
        return self.__privateIncome
    
    def trip_history(self):
        return self.__tripHistory

    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type=='car':
            vehicles = self.__availableCar
        elif vehicle_type=='bike':
            vehicles = self.__availableBike
        elif vehicle_type == 'cng':
            vehicles = self.__availableCng
        if len(vehicles)==0:
            print('sry no cars availble')
            return False
        fare = 0
        for vehi in vehicles :
                if abs(rider.location-vehi.driver.location) < 50:
                    distance = abs(rider.location - destination)
                    fare = vehi.rate * distance
                if fare > rider.balance :
                    print('You have not sufficent money')
                    return False
                if vehi.status == 'available':
                    vehi.status = 'unavailable'
                    trip_info = f'match for {vehicle_type} {rider.name} for fare {fare} and balace of rider {rider.balance} with driver {vehi.driver.name} and earning {vehi.driver.earning} started: {rider.location} to {destination}'
                    vehicles.remove(vehi)
                    
                    rider.start_trip(fare,trip_info)
                    vehi.driver.set_a_trip(fare*0.8,rider.location,destination,trip_info)
                    self.__privateIncome+=fare*0.2
                    self.__tripHistory.append(trip_info)
                    return True
uber = RideManager()
    