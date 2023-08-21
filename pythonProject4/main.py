import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

class PowerballAnalyzer:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.data_file)

    def process_data(self):
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Winning Number'] = self.df['Winning Number'].astype(int)

    def save_to_database(self, database_file):
        conn = sqlite3.connect(database_file)
        self.df.to_sql('powerball_winning_numbers', conn, if_exists='replace')
        conn.close()

    def display_results(self):
        winning_numbers_by_month = self.df.groupby(['Month', 'Winning Number'])['Winning Number'].count().reset_index()
        winning_numbers_by_month = winning_numbers_by_month.sort_values(by=['Month', 'Winning Number'], ascending=[True, False])
        winning_numbers_by_month.plot(x='Month', y='Winning Number', kind='bar', title='Winning Numbers by Month')
        plt.show()

    def run(self):
        try:
            self.load_data()
            self.process_data()
            self.save_to_database('powerball_winning_numbers.db')
            self.display_results()
        except Exception as e:
            print(f'An error occurred while processing the data: {e}')

analyzer = PowerballAnalyzer('LotteryPowerballWinningNumbers.csv')
analyzer.run()