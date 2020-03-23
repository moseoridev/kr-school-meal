import re
import datetime

import requests
from bs4 import BeautifulSoup


def get_text(code, gyc, kind, date):
    gyc_url = {
        '서울': 'stu.sen.go.kr',
        '인천': 'stu.ice.go.kr',
        '부산': 'stu.pen.go.kr',
        '광주': 'stu.gen.go.kr',
        '대전': 'stu.dje.go.kr',
        '대구': 'stu.dge.go.kr',
        '세종': 'stu.sje.go.kr',
        '울산': 'stu.use.go.kr',
        '경기': 'stu.goe.go.kr',
        '강원': 'stu.kwe.go.kr',
        '충북': 'stu.cbe.go.kr',
        '충남': 'stu.cne.go.kr',
        '경북': 'stu.gbe.go.kr',
        '경남': 'stu.gne.go.kr',
        '전북': 'stu.jbe.go.kr',
        '전남': 'stu.jne.go.kr',
        '제주': 'stu.jje.go.kr'
    }
    params = {'schulCode': code, 'schulCrseScCode': kind[-1:],
              'schulKndScCode': kind, 'schYm': date.strftime('%Y%m')}
    url = f'https://{gyc_url[gyc]}/sts_sci_md00_001.do?'
    r = requests.get(url, params)

    return r.text


def menu_list(lt):
    souped_html = BeautifulSoup(lt, 'html.parser')
    raw_menu_list = souped_html.find(
        'table', {'class': 'tbl_type3 tbl_calendar'}).find_all('div')

    return raw_menu_list


def today_meal(ml, today):
    for i in ml:
        d = re.findall(r'\d+', str(i))
        if len(d) > 0:
            if d[0] == str(today):
                return str(i)


def get_meal(code, gyc, kind, date=datetime.datetime.now()):
    lt = get_text(code, gyc, kind, date)
    ml = menu_list(lt)
    tm = today_meal(ml, date.day)

    target = ('.', '\'', '`', ',', '*', '#', '<div>', '</div>',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    for c in target:
        tm = tm.replace(c, '')
    tm = tm.replace('<br/>', '\n')
    tm = [line for line in tm.split('\n') if line.strip() != '']

    if tm == []:
        return False

    return tm


# get_meal('J100005882', '경기', '04', datetime.datetime(2019, 10, 10))
