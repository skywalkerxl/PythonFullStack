import requests
import json
from bs4 import BeautifulSoup

for i in range(53,153):


    print("第%s章"%(i-53))

    response = requests.get(
        url='http://yun.mmd6666.com/article/reader?aid=12588&cid=18498' + str(i),
        headers={
            'Referer': 'http://yun.mmd6666.com/login',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        },
        cookies={
            "PHPSESSIDTUIKE": "d8b55c3c0003fb3cc0a9870f3798edda",
            "jieqiUserInfoTk": "jieqiUserId%3D1468%2CjieqiUserUname%3D15555511181%2CjieqiUserUname_un%3D15555511181%2CjieqiUserLogin%3D1521725222",
            "jieqiVisitInfoTk": "jieqiUserLogin%3D1521725222%2CjieqiUserId%3D1468"
        }
    )

    # print(response.text)
    html_doc = response.text
    soup = BeautifulSoup(html_doc)
    print()
    aArr = soup.find(id="mainCont").find_all("p")
    for key in aArr:
        print(key.get_text())

