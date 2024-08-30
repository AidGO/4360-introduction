import sys

info_command = ["/fact", "/what", "/name", "/why"]

def isPresent():
    if sys.argv[1].lower() in info_command:
        return True
    else:
        print("Command not found. Can only get info using '/fact', '/what', 'why', and '/name' after file name")
        return False
        

def printInfo(info):
    if info == False:
        print("No info recieved")
    else:
        if sys.argv[1].lower() == "/fact":
            print("I lived on a farm for most of my life and had 7 fully grown dogs at some point.")
        elif sys.argv[1].lower() == "/what":
            print("I want to make cool stuff using the knowledge I gained in computer science")
        elif sys.argv[1].lower() == "/name":
            print("My name is Aiden Olsen and this is my third year at BSU!")
        elif sys.argv[1].lower() == "/why":
            print("I find it crazy that computers even work at all and how fast they evolve. Thats why I am interested in computer science.")

if __name__ == "__main__":
    info = isPresent()
    printInfo(info)  