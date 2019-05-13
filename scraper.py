import os
import requests

from BeautifulSoup import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
sch = BlockingScheduler()

def main(): 
    url = 'https://www.indeed.com/jobs?q=web%20developer&l=Denver%2C%20CO&vjk=0c0f7c56b3d79b4c'
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    matches = soup.findAll(name='div', attrs={'class': 'title'})

    for jobTitle in matches:
        if "Junior" in jobTitle.text: 
            os.system("osascript sendMessage.scpt YOUR_NUMBER_HERE 'Just one' ")
            break
        elif "Jr" in jobTitle.text: 
            os.system("osascript sendMessage.scpt YOUR_NUMBER_HERE 'how many' ")
            break  
    return;

sch.add_job(main, 'interval', seconds=2)
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
    sch.start()
except (KeyboardInterrupt, SystemExit):
    pass
