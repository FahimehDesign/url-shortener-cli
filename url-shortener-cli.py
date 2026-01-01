import random
import string
import json

class Link:
    def __init__(self, file_name = "myfile.json"):
        self.links = {}
        self.file_name = file_name
        self.load_from_file()
        

    def show_menu(self):
        print("What do you want?")
        print("1. Shorten a URL")
        print("2. Get original URL from short code")
        print("3. Exit")

    def gettin_number(self,number):
        if number == 1:
            url = input("Enter the long url: ")

            length = 5
            character = string.ascii_letters + string.digits
            new_url = ''.join(random.choice(character) for _ in range(length))

            #avoide duplicates
            while new_url in self.links:
                new_url = ''.join(random.choice(character) for _ in range(length))
                
            self.links[new_url] = url
            self.save_to_file() #save after update

            print("this is the short URL: ", new_url)
            
        elif number == 2:
            short_url = input("give me your short url...")

            if short_url in self.links:
                print("You're welcome.")
                print("Original URL:",self.links[short_url])
            else:
                print("We don't have it  SORRY!")
        
        elif number == 3:
            print("OK BYE. Have fun.")
            exit()
    
    #save dictionary to JSON file
    def save_to_file(self):
        with open (self.file_name , 'w') as file:
            json.dump(self.links, file)
            print("Saved!")
    
    #load links from JSON
    def load_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                self.links = json.load(file)
        except FileNotFoundError:
            self.links = {}


#------------------Main Program-----------------------#
my_link =Link()
while True:
    my_link.show_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter 1, 2 or 3!")
        continue
    my_link.gettin_number(choice)