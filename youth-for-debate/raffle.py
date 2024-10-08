import pandas as pd
from update_tickets import update_tickets
import random

def main():

    # update the csv
    update_tickets()

    # read in csv
    df = pd.read_csv("ticket_tracker.csv")

    # drop all columns except for tickets and student
    new_df = df[['tickets', 'student']]


    # create list
    students_list = []
    for _, row in new_df.iterrows():
        students_list.extend([row['student']] * row['tickets'])

    # randomly select a winner
    winner = random.choice(students_list)
    print(f"The winner of the raffle is: {winner}")


if __name__ == '__main__':
    main()