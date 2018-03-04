import requests
import json
from bs4 import BeautifulSoup

response = requests.get(
    url='https://zhihu.com',
    headers={
        'Referer': 'https://www.google.com.sg/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    },
    cookies={
        "d_c0": "AEBCSgCuwQuPTsubeQMLJe8FL5gz4wXYsXM=|1494756185",
        "_zap": "e6df398a-eb7b-4bfa-9575-62c48a53909c",
        "q_c1": "dd9243a129544ff7a5bbc8141bd5fd5c|1506381951000|1503628661000",
        "z_c0": "2|1:0|10:1510965947|4:z_c0|92:Mi4xcm1SQ0FnQUFBQUFBUUVKS0FLN0JDeVlBQUFCZ0FsVk51OUQ4V2dCZXNqQkRZMllGWnVIYUU1Y293X3h3R0w5UXJR|900b5754c0bdaa76afabee064b55691f8e607c19a307bb37fbe6e06ac1bd2749",
        "__utmv": "51854390.100-1|2=registration_date=20151105=1^3=entry_date=20151105=1",
        "q_c1": "dd9243a129544ff7a5bbc8141bd5fd5c|1517276258000|1503628661000",
        "_ga": "GA1.2.562875993.1508210234",
        "__utma": "51854390.562875993.1508210234.1513684089.1518097927.5",
        "__utmz": "51854390.1518097927.5.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/47114001",
        "aliyungf_tc": "AQAAANDKWkqRegAAdqAccOh3TidP8KE0",
        "_xsrf": "6ec90f49-5dac-448a-8163-e93f9e408432"
    }
)

print(response.text)
