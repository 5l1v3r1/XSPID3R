# XSPID3R

XSPID3R is a tool that uses DNSDUMPSTER.com To Scan either a specific target or list of targets .

# XSPID3R SCREENSHOT :

![Alt text](https://preview.ibb.co/hgqqJS/XSPID3R.png "XSPID3R ScreenShoot")

# How to install XSPID3R ? 

Include the files below in one folder : 

* DNS_FFR.txt	
* DNS_LINKS.txt
* DNS_RESP.txt
* FINAL_RESULT.txt
* LIST.txt
* XSPID3R.py

Make Sure The Modules Below Are Installed If NOT > use this command to install one : pip install [module name] 

* requests
* re
* argparse
* BeautifulSoup
* SoupStrainer

# XSPID3R USAGE : 

* python XSPID3R.py --search example.com > Look for example.com in Dnsdumpster .

* python XSPID3R.py --search_list LIST.txt > Scan sites in the file 'LIST.txt' using  Dnsdumpster.

* python XSPID3R.py --backup example.com > Look for example.com in the backup file .

* python XSPID3R.py --author show > shows the author information 

# Contact : 

Twitter.com/moh_security 

