import csv
import os 
import pandas as pd
from datetime import date
from dateutil.parser import parse
from colorama import Fore

class Discount:

    def __init__(self):

        #TODO: Check if file exists for initial word count
        try:
            df = pd.read_csv("words.csv")
        except:
            self.make_csv()
            df = pd.read_csv("words.csv")

        lenf = len(df.index)

        self.current_words = df["current_words"][lenf-1]
        self.daily_goal = df["daily_goal"] [lenf-1]
        self.weekly_goal = df["weekly_goal"][lenf-1]
        self.total_words = df["total_words"][lenf-1]
        self.due_date = df["due_date"][lenf-1]
        self.curr_date = df["curr_date"][lenf-1]
        self.days_left = df["days_left"][lenf-1]

    def main(self):
        self.menu()

    def menu(self):
        choice = ''
        while choice != "4":
            os.system("clear")
            print( Fore.CYAN + 
            """       
 ___    ____ _____ _____        __   ___   __ __  ____   ______ 
|   \  |    / ___// ___/       /  ] /   \ |  |  ||    \ |      |
|    \  |  (   \_(   \_       /  / |     ||  |  ||  _  ||      |
|  D  | |  |\__  |\__  |     /  /  |  O  ||  |  ||  |  ||_|  |_|
|     | |  |/  \ |/  \ |    /   \_ |     ||  :  ||  |  |  |  |  
|     | |  |\    |\    |    \     ||     ||     ||  |  |  |  |  
|_____||____|\___| \___|     \____| \___/  \__,_||__|__|  |__| 
            """ + Fore.WHITE 
            
            )

            choice = input("\n1) Update\n2) Statistics\n3) Remove Entry\n4) Exit\n> ")
            if choice == "1":
                self.update()
            elif choice == "2":
                self.statistics()
        
        exit()

    def update(self):
        today = date.today()
        print("\nCurrent word count: " + Fore.RED, self.current_words, "" + Fore.WHITE)

        new_count = int(input("New word count: "))
        new_words  = new_count-self.current_words
        self.weekly_goal -= new_words
        
        if str(self.curr_date) == str(today):
            self.daily_goal = self.daily_goal-new_words
        else:
            self.daily_goal = 500-new_words

        self.curr_date = today
        d1 = parse(self.due_date)
        self.days_left = d1.date() - self.curr_date
        self.days_left = self.days_left.days
        self.current_words = new_count
        
        print("\nYou have written" + Fore.GREEN, new_words, "new words" + Fore.WHITE + " you have" + Fore.GREEN, self.daily_goal, Fore.WHITE + "words left for the day!")
        # print("You need to write", self.weekly_goal )
        print("You are" + Fore.GREEN, (self.current_words/self.total_words)*100, "%" + Fore.WHITE + " towards completing your assignment!")
        print("There are" + Fore.RED, self.days_left, Fore.WHITE + "days till your deadline!")
        # print("Days left: you have ", date(int(self.curr_date))-today, " days till assignment is due")
        print("You must write at least" + Fore.GREEN, int((self.total_words-self.current_words)/self.days_left-2), Fore.WHITE + "to complete your assignment by the due date!")

        
        row = [self.current_words, self.daily_goal, self.weekly_goal, self.total_words, self.due_date, self.curr_date, self.days_left]
        self.write_csv(row)

        input("\nPress any key to return to menu\n> ")
    
    def statistics(self):
        print("\npercentage: {}%".format(int((self.current_words/self.total_words)*100)))
        print("minimum words per day: {}".format(int((self.total_words-self.current_words)/self.days_left-2)))
        print("days till deadline: {}".format(self.days_left))
        #TODO: Implement daily average / predicted completion 
        # print("daily average")
        # print("predicted completion: {}")
        print("words done today: {}".format(500-self.daily_goal))


        input()

    def remove_entry(self):
        

    def make_csv(self):
        with open('words.csv', mode='a+') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["current_words", "daily_goal", "weekly_goal", "total_words" , "due_date", "curr_date", "days_left"])

            current_words = input("\nHow many words are you currently on: ")
            daily_goal = input("What is your daily word goal: ")
            weekly_goal = input("What is your weekly word goal: ")
            total_words = input("What is the total word goal: ")
            due_date = parse(input("When is your assignment due (i.e 21 March, 2020): "))
            days_left = due_date.date() - date.today()
            writer.writerow([current_words,daily_goal,weekly_goal,total_words,due_date.date(),date.today(),days_left.days])
        
    def write_csv(self, row):
        with open('/Users/ligula/Documents/projects/discount/words.csv', mode='a+') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)

    # def strip_latex():


if __name__ == "__main__":
    Discount().main()











