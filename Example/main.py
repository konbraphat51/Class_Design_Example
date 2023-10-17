'''
Interface script
'''

from Manager import Manager

manager = Manager()

manager.load_data('data.json')

#repeat for ever
while True:
    #take command
    print("Give your command:")
    command = input()
    
    #respond to command
    match command:
        
        #users list
        case "l":
            print(manager.show_users_list())
            
        #user detail
        case "d":
            #ask user id
            print("input id:")
            id = int(input())
            
            #show
            print(manager.show_user_detail(id))
            
        #income calculation
        case "i":
            print(manager.calculate_income())
            