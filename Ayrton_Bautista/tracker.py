import time
import json
import os
import datetime

def weekday_to_index (date):
    day_index = date.weekday()
    if day_index == 6:
        return 0
    else:
        return day_index + 1

def sec_to_HMS (sec):
    hours = int(sec // 3600)
    minutes = int((sec % 3600) // 60)
    sec = int(sec % 60)
    return f"{hours:02d}:{minutes:02d}:{sec:02d}"

class time_sheet:
    def __init__(self, ref):
        self.name = ref["name"]
        self.time = ref["time"]
        self.week_balance = ref["week_balance"]
        self.prev_balance = ref["prev_balance"]
    
    def summary_week(self):
        
        balance = 0
        free_day = True

        for i in self.time:
            
            if i < 60*60:
                if free_day == True:
                    free_day = False
                else:
                    balance += 20

        self.week_balance = balance

def menu (user):
    print("What do you want to do?\n(1) Start Learning Session\n(2) Balance Check\n(3) Summary\n(E) Edit Specific Field\n(Q) Quit")
    user_choice = input("\nUser Choice: ")
    
    # Quiting the menu
    if user_choice.lower() == "q":
        return True
    
    # Learning Session including updating the time in the JSON File
    elif user_choice == "1":
        while True:
            os.system("cls")

            # user input to start the timer
            # if user input "N", the program will loop back and ask again
            user_start = input("Start Timer? (Y/N) ")

            # to lower() will ensure that answers are not case sensitive
            if user_start.lower() == "y":

                # this stores the actual start time of the session
                start_time = time.time()

                #string version of the start time in HH:MM:SS
                str_start_time = time.strftime("%H:%M:%S", time.localtime(start_time))
                print(f"Start Time: {str_start_time}")

                # listens if the user wants to stop the timer
                while True:
                    user_stop = input("\nStop Timer? (Y/N)")
                    if user_stop.lower() == "y":

                        # record the stop time of the session
                        stop_time = time.time()
                        print(f"Total duration for this session is: {sec_to_HMS(stop_time - start_time)}"
                              )
                        time.sleep(1)
                        print("\nReturning to Menu in...")
                        user.time[weekday_to_index(datetime.datetime.today())] += time.time() - start_time
                        user.summary_week()

                        for i in range(3):
                            time.sleep(1)
                            print(f"{3-i}")
                        time.sleep(1)    
                        break
                    print(f"Elapse Time: {sec_to_HMS(time.time() - start_time)}")
                    
                break   
            else:
                print("Input a valid response.\n")


    elif user_choice == "2":
        os.system("cls")
        user.summary_week()
        
        print(f"This Week's Balance is: Php {user.week_balance}")
        print(f"Previous Week's Balance is: Php {user.prev_balance}\n")
        print(f"Total Balance is: Php {user.week_balance + user.prev_balance}\n\nReturning to Menu in...\n")
        for i in range(3):
            time.sleep(1)
            print(f"{3-i}")
        time.sleep(1)

def open_JSON_File(filename, folder_path):

    user_data_path = os.path.join(folder_path, filename)
    
    try:
        with open(user_data_path) as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: File '{user_data_path}' not found.")

    except json.JSONDecodeError:
        print(f"Error: '{user_data_path}' is not a valid JSON file.")
    

if __name__ == "__main__":
    
    # accessing the user_data file
    user_data = open_JSON_File("user_data.json","user_data")

    # Access the JSON File and check if username exist
    while True:
        # Ask the user for their username
        os.system("cls")
        username = input("Input Github Username or Quit(Q): ")
        if username.lower() == "q":
            break
        else:   
            if username in user_data:
                os.system("cls")
                user_name = user_data[username]["name"].upper()
                print(f"*** WELCOME ***\n{user_name}")
                user = time_sheet(user_data[username])        
                time.sleep(2)

                while True:
                    os.system("cls")
                    if menu(user):
                        break
                    
                    # Updating the JSON File
                    user_data[username]["time"] = user.time
                    user_data[username]["week_balance"] = user.week_balance 
                    with open(user_data_path,'w') as file:
                        json.dump(user_data, file, indent=4)
            else:
                print("User not found. Please enter a valid username.")
                time.sleep(2)



