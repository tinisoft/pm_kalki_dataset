html_list = [
    "pmuni0169_00.html",
    "pmuni0169_01_01.html",
    "pmuni0169_01_02.html",
    "pmuni0169_01_03.html",
    "pmuni0169_01_04.html",
    "pmuni0169_01_05.html",
    "pmuni0169_01_06.html",
    "pmuni0169_02_01.html",
    "pmuni0169_02_02.html",
    "pmuni0169_02_03.html",
    "pmuni0169_02_04.html",
    "pmuni0169_02_05.html",
    "pmuni0169_02_06.html",
    "pmuni0169_03_01.html",
    "pmuni0169_03_02.html",
    "pmuni0169_03_03.html",
    "pmuni0169_03_04.html",
    "pmuni0169_03_05.html",
    "pmuni0169_04_01.html",
    "pmuni0169_04_02.html",
    "pmuni0169_04_03.html",
    "pmuni0169_04_04.html",
    "pmuni0169_04_05.html",
    "pmuni0169_05_01.html",
    "pmuni0169_05_02.html",
    "pmuni0169_05_03.html",
    "pmuni0169_05_04.html",
    "pmuni0169_05_05.html",
    "pmuni0169_05_06.html",
    "pmuni0169_05_07.html",
    "pmuni0169_05_08.html",
    "pmuni0169_05_09.html",
    "pmuni0169_06.html",
    "pmuni0193.html",
    "pmuni0194.html",
    "pmuni0195.html",
    "pmuni0205.html",
    "pmuni0206.html",
    "pmuni0210.html",
    "pmuni0214.html",
    "pmuni0223_01.html",
    "pmuni0223_02.html",
    "pmuni0228.html",
    "pmuni0376.html",
    "pmuni0384.html",
    "pmuni0385_01.html",
    "pmuni0385_02.html",
    "pmuni0443_01.html",
    "pmuni0443_02.html",
    "pmuni0636.html",
    "pmuni0637.html",
    "pmuni0637.html",
    "pmuni0638.html",
    "pmuni0639.html",
    "pmuni0640.html"
]

import requests
import time

base_url = "https://www.projectmadurai.org/pm_etexts/utf8/{}"

for book in html_list:
    url = base_url.format(book)
    print("fetching {}".format(url))
    
    r = requests.get(url, allow_redirects=True)
    open(book, 'wb').write(r.content)
    time.sleep(5)
