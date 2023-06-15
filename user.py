import hashlib
from random import randint
from brta import BRTA
from vehicle import Car, Bike, Cng
from ride_manager import uber
license_authority = BRTA()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('./users.txt', 'a') as file:
            file.writelines(f'{email} {pwd_encrypted} ')
        file.close()

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = list(str(file.readlines()).split(' '))

            print(lines)

            for key, line in enumerate(lines):
                if email in line:
                    stored_password = lines[key+1]
        file.close()
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        if hashed_pass == stored_password:

            return True
        else:

            return False


class Rider(User):
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.balance = balance

        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_destination(self, destination):
        self.destination = destination

    def request_trip(self):
        pass

    def start_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, licenses) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.licenses = licenses
        self.earning = 0
        self.valid_driver = license_authority.validate_license(email, licenses)

    def taking_driver_test(self):
        result = license_authority.driving_test(self.email)
        if result == False:
            print('Youre failed,try again')
        else:
            self.licenses = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            new_vehicle = None
            if vehicle_type == 'car':
                new_vehicle = Car(
                    license_plate, vehicle_type, rate, self)
                uber.add_a_vehicle(new_vehicle,vehicle_type)
                # print('vehicle created')
            elif vehicle_type == 'bike':
                new_vehicle = Bike(
                    license_plate, vehicle_type, rate, self)
                uber.add_a_vehicle(new_vehicle,vehicle_type)
                # print('vehicle created')
            elif vehicle_type == 'cng':
                new_vehicle = Cng(
                    license_plate, vehicle_type, rate, self)
                uber.add_a_vehicle(new_vehicle,vehicle_type)
                # print('vehicle created')

        else:
            print('You are not a valid driver')

    def set_a_trip(self, fare, destination):
        self.earning += fare
        self.location = destination


rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1',
               randint(1, 100), randint(5000, 333333))
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2',
               randint(1, 100), randint(5000, 333333))
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3',
               randint(1, 100), randint(5000, 333333))
# print(dir(rider1))
# rider1.log_in('rider1@gmail.com', 'rider1')

driver1 = Driver('driver1', 'driver1@gmail.com',
                 'driver1', randint(1, 100), None)
driver1.taking_driver_test()
driver1.register_a_vehicle('car',randint(3234, 32578839),40)
driver2 = Driver('driver2', 'driver2@gmail.com',
                 'driver2', randint(1, 100), None)
driver2.taking_driver_test()
driver2.register_a_vehicle('car',randint(3234, 32578839),40)
driver3 = Driver('driver3', 'driver3@gmail.com',
                 'driver3', randint(1, 100), None)
driver3.taking_driver_test()
driver3.register_a_vehicle('car',randint(3234, 32578839),40)
print(uber.available_vehicle())


uber.find_a_vehicle(rider1,'car',90)