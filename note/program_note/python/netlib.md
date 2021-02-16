# python网页下载

<pre>
"""
Created on Tue Nov 20 09:50:26 2018
@author: weiyx15
Automated downloading all data links from 
http://nemweb.com.au/Reports/Current/Next_Day_Offer_Energy/
"""
import urllib.request# url request
import re            # regular expression
import os            # dirs
 
# parent url
url = 'http://nemweb.com.au/Reports/Current/Next_Day_Offer_Energy/'
 
# regular expression
pattern = '(PUBLIC_NEXT_DAY_OFFER_ENERGY_(\d*)_(\d*).zip)'
 
# pull request
headers = {'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
content = opener.open(url).read().decode('utf8')
 
# match regex and drop repetition
raw_hrefs = re.findall(pattern, content, 0)
hset = set(raw_hrefs)
 
# make directory
if not os.path.exists('./auto_download'):
    os.makedirs('auto_download')
 
# download links
for href in hset:
    link = url + href[0]
    print(link)
    urllib.request.urlretrieve(link, os.path.join('./auto_download', href[0]))

</pre>