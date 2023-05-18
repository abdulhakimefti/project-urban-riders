import hashlib
class User :
    def __init__(self,name,email,password)->None:
        self.name = name;
        self.email = email;
        self.password = password
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('./users.txt','w') as file :
            file.write(f'{email} {pwd_encrypted}')
        file.close()

    @staticmethod 
    def log_in(email,password):
        stored_password=''
        with open('users.txt','r') as file:
            lines = file.readlines()
            for line in lines :
                if email in line :
                   stored_password = line.split(' ')[1]
        file.close()
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        if hashed_pass == stored_password :
            return True
        else :
            return False

efti = User('Abdul Hakim','abdulhakimefti@gmail.com','checkpass')
print(User.log_in('abdulhakimefti@gmail.com','checkpass'))



