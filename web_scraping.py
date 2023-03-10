import requests
from bs4 import BeautifulSoup
from db_oper import open_db, fill_db


def web_sc():
    last_nr = input('Paskutinio tiražo numeris : ')
    start_nr = input('Pradinio tiražo numeris : ')

    adr = f'https://loto.lt/lt/statistic/eurojackpot?tab=%23archive&Filter%5BdrawFrom%5D={start_nr}&Filter%5BdrawTo%5D={last_nr}'
    r = requests.get(adr)
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)
    elements = soup.find_all(class_='lead')
    elements2 = soup.select('.number ')
    tir: list[int] = []
    for element in elements:
        temp = element.get_text()
        # print(temp)
        temp2 = ''
        for x in temp:
            if x.isdigit():
                temp2 += x
        # print(temp2)
        tir.append(int(temp2))
    # print(tir)

    dig = []
    dig_tmp = []
    counter = 0
    cnt_tir = 0
    for el in elements2:
        if counter == 0:
            dig_tmp.append(tir[cnt_tir])
            cnt_tir += 1
        temp = int(el.get_text())
        dig_tmp.append(temp)
        counter += 1
        # print(counter, temp)
        if counter > 6:
            dig.append(dig_tmp)
            dig_tmp = []
            counter = 0

    cont = len(dig)
    # print(dig)
    # print(cont)

    open_db()
    fill_db(dig, cont)
