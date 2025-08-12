import json
import os
class Vault:
    def __init__(self):
        self.user_id=None
        self.password=None
        self.pass_key=None
        
    def main(self):
        while True:
            
            
            choise=input("""select valid action
                     1. Save Password
                     2. Show Password
                     3. Edit Password or User name
                     4. Delete Password
                     5. Exit """)
            if choise=="1":
                self.save_pass()
            elif choise=="2":
                self.show_passwords()
            elif choise=="3":
                self.edit_password()
            elif choise=="4":
                print("we are still working on it")
            elif choise=="5":
                break
            else:
                print("select valid action :")
        
    def save_pass(self):
        self.user_id=input("enter user name or email id : ")
        self.password=input("enter password : ")
        self.display()
        self.encrypt_and_save()
        
    
    def display(self):
        print("user_id:{}, password:{}".format(self.user_id,self.password))
        
    
    def encrypt(self,password):
        encrypted=''
        for i in range (len(password)):
            encrypted+= chr(ord(password[i])+i)
        return encrypted
            
        
        
    
    def encrypt_and_save(self):
          
        self.password=self.encrypt(self.password)
        
        dict={"name":self.user_id,"password":self.password}
        if os.path.exists('locker.json'):
            with open('locker.json','r') as f:
                try:
                    data=json.load(f)
                except json.JSONDecodeError:
                    data=[]
        else:
            data=[]        
        data.append(dict)
        
        with open('locker.json','w') as f:
            json.dump(data,f)
    def show_passwords(self):
        with open('locker.json','r') as f:
            data=json.load(f)
            for entry in data:
                Password=entry["password"]
                unercryped=self.decrypt(Password)
                print("user_id:{}, password:{}".format(entry["name"],unercryped))
    def decrypt(self,password):
        decrypted=""
        for i in range (len(password)):
            decrypted+=chr(ord(password[i])-i)
        return decrypted
            
    
    def edit_password(self):
            with open('locker.json','r') as f:
                data=json.load(f)
            edit=input("enter user corresponding user name to edit password : ")
            for entry in data:
                if edit==entry["name"]:
                    entry["password"]=self.encrypt(input("enter new password"))
            with open('locker.json','w') as f:
                json.dump(data,f)
            print ("password edited successfully")
                
            
p1=Vault()
p1.save_pass()
p1.show_passwords()
            
            
        
        