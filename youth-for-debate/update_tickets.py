import pandas as pd

def update_tickets():
    # read in csv
    df = pd.read_csv('ticket_tracker.csv')

    # update total tickets
    df['tickets'] = df.drop(columns=['tickets', "student"]).sum(axis=1)

    # display + save
    df.to_csv('ticket_tracker.csv', index=False)
    print(df)

if __name__ == '__main__':
    update_tickets()