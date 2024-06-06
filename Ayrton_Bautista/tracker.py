import time

class time_sheet:
    def __init__(self, name, total_balance):
        self.name = name
        self.time = [0] * 7 # initialize to be zero
        self.total_balance = total_balance
    
    def summary_week(self):
        time = 0
        balance = 0
        free_day = True

        for i in self.time:
            time = self.time[i]

            if self.time[i] < 60*60:
                if free_day == True:
                    free_day = False
                else:
                    balance += 20

        self.total_balance += balance

def fetch_user(self):
    username = input("Input Username: ")



username = input("Input Username: ")

user = fetch_user(username)