
# By MOHAMMED ADEL
# Twitter : @moh_security

import requests # pip install requests 
import re # pip install re
import argparse # pip install argparse 
from bs4 import BeautifulSoup, SoupStrainer # pip install BeautifulSoup | pip install SoupStrainer


def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))


prRed (
    '''
****************************************
                  :                        
                  :                      
       ,,         :         ,,               
       ::         :         ::             
,,     ::         :         ::     ,,      
::     ::         :         ::     ::      
 '::.   '::.      :      .::'   .::'          
    '::.  '::.  _/~\_  .::'  .::'       
      '::.  :::/     \:::  .::'        
        ':::::(       ):::::'         
               \ ___ /                  
         .:::::/`   `\:::::.           
       .::'   .:\o o/:.   '::.        
     .::'   .::  :":  ::.   '::.            
   .::'    ::'   ' '   '::    '::.      
  ::      ::             ::      ::    
  ^^      ::             ::      ^^   
          ::             ::             
          ^^             ^^      
    '''
)


parser = argparse.ArgumentParser(description="[+] XSPID3R is a tool that uses DNSDUMPSTER To Scan specific TARGETS.[+]")
parser.add_argument("-s", "--search", type=str, help="-s example.com OR --search example.com")
parser.add_argument("-b", "--backup", type=str, help="-b example.com OR --backup example.com")
parser.add_argument("-a", "--author", type=str, help="-a show OR --author show")
args = parser.parse_args()


client = requests.session()
GET_URL_VCOMM = args.search
GET_BACKUO_URL = args.backup

if args.search:
    URL_TARGET = GET_URL_VCOMM
    URL = 'https://dnsdumpster.com/'
    client.get(URL) 
    csrftoken = client.cookies['csrftoken']
    payload = {
    'targetip':URL_TARGET,
    'csrfmiddlewaretoken':csrftoken
    }
    DNS_FILE = open('DNS_RESP.txt','w')


    r = client.post(URL, data=payload, headers=dict(Referer=URL))

    DNS_FILE.write(r.text)
    DNS_FILE.close()

    DNS_LINKS = open('DNS_LINKS.txt', 'w')


    scan1 =  open('DNS_RESP.txt', 'r')
    soup = BeautifulSoup(scan1, "lxml")
    for link1 in soup.findAll('a', attrs={'href': re.compile('((http|https)s?://.*?)')}):
        DNS_LINKS.write(link1.get('href'))
        DNS_LINKS.write("\n")


    DNS_LINKS.close()

    FIND_RE_URLS = open('DNS_LINKS.txt', 'r')

    ReadDATA = FIND_RE_URLS.readlines()


    FIND_RE_URLS.close()


    DNS_FILTER_LINKS = open('DNS_LINKS.txt', 'r')
    DNS_FFR_LINKS = open('DNS_FFR.txt', 'w')

    FilterDATA = DNS_FILTER_LINKS.readlines()

    for line in FilterDATA:
        DNS_FFR_LINKS.write(line.rpartition('?q=')[2])

    DNS_FFR_LINKS.close()
    DNS_FILTER_LINKS.close()


    DNS_PRINT_OUT = open('DNS_FFR.txt', 'r+b')

    Final_Result = DNS_PRINT_OUT.readlines()
    
    prCyan("[+] TARGET : "+URL_TARGET)
    prCyan("[+] CSRF TOKEN : "+csrftoken)


    for line in Final_Result:
        if "https://dnsdumpster.com/static/xls/" in line:
            S_REPORT = line 
            prCyan("[+] Scan Report : "+S_REPORT)


    Choice_TO_SRESULT = raw_input("[**] Show RESULT ? (y/n) #> ")
    PRINT_FINAL_URLSS = open('FINAL_RESULT.txt', 'a')
    PRINT_FINAL_URLSS.write("[+] TARGET : "+URL_TARGET)
    PRINT_FINAL_URLSS.write("\n")
    PRINT_FINAL_URLSS.write("[+] CSRF TOKEN : "+csrftoken)
    PRINT_FINAL_URLSS.write("\n")
    PRINT_FINAL_URLSS.write("[+] Scan Report : "+S_REPORT)
    PRINT_FINAL_URLSS.write("\n")

    if Choice_TO_SRESULT == "y" or Choice_TO_SRESULT == "Y":
        for line in Final_Result:
            if URL_TARGET in line:
                print "\n"
                prGreen("[+] "+line)
                PRINT_FINAL_URLSS.write(line)

    elif Choice_TO_SRESULT == "n" or Choice_TO_SRESULT == "N":
        print "\n"
        for line in Final_Result:
            if URL_TARGET in line:
                PRINT_FINAL_URLSS.write(line)

        prGreen("[INFO] DATA SAVED IN FILE [FINAL_RESULT.txt] \n")
        prGreen("[INFO] To Search Backup Data Use The Commands Below : \n")
        prGreen("[INFO] python XSPID3R.py --backup examples.com \n")
        print "\n"

elif args.backup:
    Search_FILE = open('FINAL_RESULT.txt', 'r')
    FILE_DATA = Search_FILE.readlines()

    for line in FILE_DATA:
        if GET_BACKUO_URL in line:
            prGreen(line)
 
elif args.author:
    prPurple("[+] Author : MOHAMMED ADEL\n")
    prPurple("[+] Twitter : @moh_security\n")
    prPurple("[+] Github : github.com/inurlx\n")
    exit()

