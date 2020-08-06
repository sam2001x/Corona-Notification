from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "A:\\projects\\project_7\\icon.ico",
        timeout = 6
    )

def getdata(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyme("saket","lets stop the spread of this virus")    
    myhtmldata = getdata('https://www.mohfw.gov.in/')
    
    soup = BeautifulSoup(myhtmldata, 'html.parser')
    # print(soup.prettify())
    mydatastr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        mydatastr += tr.get_text()

    states = ['Rajasthan']
    mydatastr = mydatastr[1:]    
    itemlist = mydatastr.split("\n\n")
    for item in itemlist[0:30]:
        datalist = item.split("\n")
        if datalist[1] in states:
            print(datalist)
            ntitle = "Cases of covid-19 "
            ntext = f"{datalist[1]}\ncured: {datalist[3]}\ndeaths: {datalist[4]}"
            notifyme(ntitle, ntext)
            time.sleep(2)
    
