import requests
import sys
import io
import re
import json


cookie_str = r'''s_fid=308606A89767EE44-049182C0C6CF190B; s_vi=[CS]v1|2B1314DF851D1A76-4000015160324A26[CE]; AMCV_327761B652606ED30A490D4C%40AdobeOrg=793872103%7CMCAAMB-1465438727%7CNRX38WO0n5BH8Th-nqAG_A%7CMCAAMLH-1464929700%7C11%7CMCAID%7C2B1314DF851D1A76-4000015160324A26%7CMCIDTS%7C16955%7CMCMID%7C29129975055344574525935256751111319268; _ga=GA1.2.1362505539.1445341633; pgv_pvi=1546051584; GerritAccount=aOYDprq8yKLOzpK1UYN7FJTvtHqQ99N7rW'''
xauth = 'aOYDprrREZk.Ir1Kn3nTSHEQRK4eBMXq4q'
inputfile = 'giturl'
outputfile = 'cl'

cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

requesthead = {
'Host': 'git.htc.com:8081',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'X-Gerrit-Auth': xauth,
'Referer': 'http://git.htc.com:8081/',
'Connection': 'keep-alive'
}


cllist = []
with open(inputfile, "r") as f:
  for line in f:
    #form url
    if len(line) < 24:
      break
    if line[-1] == "\n":
      line = line[:-1]
    line = line.replace(r'#/c/', "")
    line = line[:24] + "changes/" + line[24:]
    if line[-1] == r'/':
      line = line[:-1]
    line = line + "/detail"
    #it should be like:  http://git.htc.com:8081/changes/1009763/detail
    print(line)
    
    #get git info
    response = requests.get(line, headers = requesthead, cookies = cookies)

    # to handle hit git response abnormal
    clid = 0
    if response.text.find("Not") != -1:
      clid = 0
    else:
      # error char )]}'\n ahead of json data
      jstring = response.text[5:]
      # store cl
      js = json.loads(jstring)
      clid = js['clid']

    cllist.append(clid)
f.close()

print(cllist)

with open(outputfile, "w") as f:
  for index in range(len(cllist)):
    f.write(str(cllist[index]))
    f.write('\n')
f.close()
