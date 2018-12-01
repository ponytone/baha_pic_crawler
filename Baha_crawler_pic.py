import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def baha_picture(url, page_number, gp_number):
    # load
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'lxml')
    # Find page
    di = soup.find('div', id="BH-master")
    s = di.find_all(href=re.compile("page="))
    l = []
    for i in s:
        try:
            l.append(int(i.contents[0]))
        except ValueError:
            continue
    page = max(l)
    if page_number > page:
        page_number = page
    # Get all pages of url
    pageList = []
    if len(url.split('page')) == 1:
        url = url.split("php?")[0] + "php?" + "page=1&" + url.split("php?")[1]
    for i in range(1, page + 1):
        pageList.append(url.split("page=")[0] + "page=" + str(i) + "&bsn" + url.split("&bsn")[1])

    # Get gp / bp / floor / picture
    gp = []
    bp = []
    a_list = []
    pic_list = []
    floor_list = []
    n = 0
    for page in pageList[:page_number]:
        url = page
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'lxml')
        floor = soup.find_all('a', class_="count tippy-gpbp-list")
        # gp
        for i in floor[::2]:
            if i.contents[0] == '爆':
                gp.append(1000)
            else:
                gp.append(int(i.contents[0]))
                # bp
        for i in floor[1::2]:
            if i.contents[0] == 'X':
                bp.append(1000)
            elif i.contents[0] == '-':
                bp.append(0)
            else:
                bp.append(int(i.contents[0]))
        # floor
        alive = soup.find_all('a', class_="floor")
        for i in alive:
            a_list.append(i.contents[0])
        # picture
        picture = soup.find_all('div', class_="c-section__main c-post ")
        for i in range(len(picture)):
            pic_list.append([])
            try:
                # pic_list[i].append(picture[i].find('a',class_="floor").contents[0])
                [pic_list[n + i].append(j['href']) for j in
                 picture[i].find_all('a', href=re.compile("\/truth.bahamut.com.tw\/"))]
            except IndexError:
                continue
        n += len(picture)
    # Prepare for Dataframe
    a_list = np.array(a_list).reshape(-1, 1)
    bp = np.array(bp).reshape(-1, 1)
    gp = np.array(gp).reshape(-1, 1)
    diff = gp - bp
    floor_list = np.array(floor_list).reshape(-1, 1)
    pic_list = np.array(pic_list).reshape(-1, 1)

    # Turn into Dataframe
    dataf = np.concatenate((bp, diff), axis=1)
    dataf = np.concatenate((gp, dataf), axis=1)
    dataf = np.concatenate((a_list, dataf), axis=1)
    dataf1 = np.concatenate((dataf, pic_list), axis=1)
    Liketable = pd.DataFrame(dataf1, columns=("樓層", "推", "噓", "差", "網址"))
    Liketable_simple = pd.DataFrame(dataf, columns=("樓層", "推", "噓", "差"))
    pd.set_option('max_colwidth', 200)

    # Turn into int
    Liketable["推"] = pd.to_numeric(Liketable["推"])
    Liketable["噓"] = pd.to_numeric(Liketable["噓"])
    Liketable["差"] = pd.to_numeric(Liketable["差"])
    Liketable_simple["推"] = pd.to_numeric(Liketable_simple["推"])
    Liketable_simple["噓"] = pd.to_numeric(Liketable_simple["噓"])
    Liketable_simple["差"] = pd.to_numeric(Liketable_simple["差"])

    # Filter
    filter1 = (Liketable_simple['差'] >= gp_number)
    print(Liketable_simple[filter1])

    filter1 = (Liketable['差'] >= gp_number)
    for i in Liketable[filter1]["樓層"]:
        fliter = (Liketable['樓層'] == i)
        print(i)
        for x in Liketable[fliter]["網址"]:
            if x == []:
                print("\t沒圖啦")
            else:
                [print(z) for z in x]