import csv
import pandas as pd
from datetime import date
from colorama import Fore

class Discount:

    def __init__(self):

        #TODO: create csv on first use
        df = pd.read_csv("/Users/ligula/Documents/projects/discount/words.csv")
        lenf = len(df.index)

        self.current_words = df["current_words"][lenf-1]
        self.daily_goal = df["daily_goal"] [lenf-1]
        self.weekly_goal = df["weekly_goal"][lenf-1]
        self.total_words = df["total_words"][lenf-1]
        self.due_date = df["due_date"] [lenf-1]
        self.curr_date = df["curr_date"][lenf-1]

    def main(self):

        while True:
            today = date.today()
            print("\nCurrent word count: " + Fore.RED, self.current_words, "" + Fore.WHITE)

            new_count = int(input("New word count: "))
            new_words  = new_count-self.current_words
            self.weekly_goal -= new_words
            
            

            if self.curr_date == str(today):
                self.daily_goal = self.daily_goal-new_words
            else:
                self.daily_goal = 500-new_words
            self.curr_date = str(today)
            days_left = self.curr_date-self.due_date
            
            print("\nYou have written" + Fore.GREEN, new_words, "new words" + Fore.WHITE + " you have" + Fore.GREEN, self.daily_goal, Fore.WHITE + "many words left for the week!")
            # print("You need to write", self.weekly_goal )
            print("Percentage complete: ", (self.current_words/self.total_words)*100, "% towards completing your diss!")
            print("There are ", days_left)
            # print("Days left: you have ", date(int(self.curr_date))-today, " days till assignment is due")
            self.current_words = new_count
            row = [self.current_words, self.daily_goal, self.weekly_goal, self.total_words, self.due_date, self.curr_date]
            self.write_csv(row)

    def write_csv(self, row):
        with open('/Users/ligula/Documents/projects/discount/words.csv', mode='a+') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)

    # def strip_latex():


if __name__ == "__main__":
    Discount().main()











