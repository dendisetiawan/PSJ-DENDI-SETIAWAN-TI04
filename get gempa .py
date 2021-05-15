import  requests
from bs4 Beautifulsoup4
from bs4 import  beautifulsoup
url="https://www.bmkg.go.id/gempabumi/gempabumi-terkini.bmkg
web = request.get(url)
data= web.text
bs = beautifulsoup(data,"html.parser)
bs.tbody
bs.tbody.tr
for tr in bs.tbody:
 print(tr)
                   
