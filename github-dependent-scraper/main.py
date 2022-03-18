###Code is from Bertrand Martel and oneturkman for this script https://stackoverflow.com/questions/58734176/how-to-use-github-api-to-get-a-repositorys-dependents-information-in-github

import requests
from bs4 import BeautifulSoup

repo = "expressjs/express"
page_num = 100
url = 'https://github.com/RIAEvangelist/node-ipc/network/dependents'.format(repo) ### edit this link to the github dependent repo you want to scrape!

for i in range(page_num):
    print("GET " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    data = [
        "{}/{}".format(
            t.find('a', {"data-repository-hovercards-enabled":""}).text,
            t.find('a', {"data-hovercard-type":"repository"}).text
        )
        for t in soup.findAll("div", {"class": "Box-row"})
    ]

    print(data)
    print(len(data))
    paginationContainer = soup.find("div", {"class":"paginate-container"}).find_all('a')
    if len(paginationContainer) > 1:
        paginationContainer = paginationContainer[1]
    else:
        paginationContainer = paginationContainer[0]
    if paginationContainer:
        url = paginationContainer["href"]
    else:
        break


