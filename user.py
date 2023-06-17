import hashlib
from random import randint,choice
from brta import BRTA
from vehicle import Car, Bike, Cng
from ride_manager import uber
license_authority = BRTA()
import threading

class UserAlreadyExists(Exception):
    def __init__(self,email,*args: object) -> None:
        print(f'{email} already exits')
        super().__init__(*args)


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('./users.txt','r') as file:
            if email in file.read():
                pass
                # print(f'{email} already exits')
                # raise UserAlreadyExists(email)
            else:
                with open('./users.txt', 'a') as file:
                    file.writelines(f'{email} {pwd_encrypted} ')
        file.close()

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = list(str(file.readlines()).split(' '))

            # print(lines)

            for key, line in enumerate(lines):
                if email in line:
                    stored_password = lines[key+1]
        file.close()
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        if hashed_pass == stored_password:
            print('logged in\n')
            return True
        else:
            return False


class Rider(User):
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.balance = balance
        self.__trip_history= []
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_destination(self, destination):
        self.destination = destination

    def request_trip(self):
        pass

    def start_trip(self, fare,trip_info):
        print(f'trip started for {self.name}')
        self.balance -= fare
        self.__trip_history.append(trip_info)
    def get_trip_history(self):
        return self.__trip_history


class Driver(User):
    def __init__(self, name, email, password, location, licenses) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.licenses = licenses
        self.earning = 0
        self.__trip_history = []
        self.valid_driver = license_authority.validate_license(email, licenses)
        self.vehicle = None

    def taking_driver_test(self):
        result = license_authority.driving_test(self.email)
        if result == False:
            # print('Youre failed,try again')
            self.licenses = None
        else:
            self.licenses = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
          
            if vehicle_type == 'car':
                self.vehicle = Car(
                    license_plate, vehicle_type, rate, self)
                uber.add_a_vehicle(self.vehicle,vehicle_type)
                # print('vehicle created')
            elif vehicle_type == 'bike':
                self.vehicle = Bike(
                    license_plate, vehicle_type, rate, self)
                uber.add_a_vehicle(self.vehicle,vehicle_type)
                # print('vehicle created')
            elif vehicle_type == 'cng':
                self.vehicle = Cng(
                    license_plate, vehicle_type, rate, self)
                uber.add_a_vehicle(self.vehicle,vehicle_type)
                # print('vehicle created')

        else:
            self.valid_driver= False

    def set_a_trip(self, fare,start, destination,trip_info):
        self.earning += fare
        self.location = destination

        # start a thread
        tripThread = threading.Thread(target=self.vehicle.start_driving, args=(start,destination,))
        tripThread.start()
        # self.vehicle.start_driving(start,destination)
        self.__trip_history.append(trip_info)
      
    
    def get_trip_history(self):
        return self.__trip_history


rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1',
               randint(1, 200), randint(3000,5000))
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2',
               randint(1, 200), randint(3000,5000))
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3',
               randint(1, 200), randint(3000,5000))
rider4 = Rider('rider4', 'rider4@gmail.com', 'rider4',
               randint(1, 200), randint(3000,5000))




for i in range(0,200):
    driver = Driver(f'driver{i}', f'driver{i}@gmail.com',
                 f'driver{i}', randint(1, 200), None)
    driver.taking_driver_test()
    driver.register_a_vehicle(choice(['car','cng','bike']),randint(3234, 32578839),20)

print(len(uber.available_vehicle()))


uber.find_a_vehicle(rider1,'car',randint(0,400))
uber.find_a_vehicle(rider2,'car',randint(0,400))
uber.find_a_vehicle(rider3,'cng',randint(0,400))
uber.find_a_vehicle(rider1,'car',randint(0,400))
uber.find_a_vehicle(rider2,'bike',randint(0,400))
uber.find_a_vehicle(rider4,'car',randint(0,400))

print(rider1.get_trip_history())


print(len(uber.available_vehicle()))
print(uber.total_income())
