import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
import schedule
import time

def scrape_and_write_to_csv():
    url = 'https://www.sharesansar.com/live-trading'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    rows = table.find_all('tr')
    i = 1
    for row in rows[1:]:
        first_row = rows[i]
        data0 = [cell.text.strip().replace(',', '').replace('"', '').replace('/', '') for cell in
                 first_row.find_all('td')]
        data = [cell.text.strip().replace(',', '').replace('"', '') for cell in first_row.find_all('td')[2:]]

        current_date = datetime.now().strftime('%Y-%m-%d')
        data.insert(0, current_date)
        csv_filename = data0[1] + '.csv'

        if not os.path.exists(csv_filename):
            with open(csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
                print(f"CSV file '{csv_filename}' created and data appended.")
        else:
            with open(csv_filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
                print(f"Data appended to existing CSV file '{csv_filename}'...")
        i += 1

scrape_and_write_to_csv()
# schedule.every().sunday.at("15:30").do(scrape_and_write_to_csv)
# schedule.every().monday.at("15:30").do(scrape_and_write_to_csv)
# schedule.every().tuesday.at("15:30").do(scrape_and_write_to_csv)
# schedule.every().wednesday.at("15:30").do(scrape_and_write_to_csv)
# schedule.every().thursday.at("15:30").do(scrape_and_write_to_csv)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)