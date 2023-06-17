import random
class BRTA:
    def __init__(self) -> None:
        self.__licensed = {}
    def driving_test(self,email):
        score = random.randint(0,100)

        if score>=33:
            license_number = random.randint(9999,39393)
            self.__licensed[email]= license_number
            return license_number
        else:
            # print('Sorry you failed')
            return False
    
    def validate_license(self,email,licenses):
        # print(self.__licensed,email,licenses)
        for key,value in self.__licensed.items():
            if key==email and value == licenses:
                return True
        return False
    

