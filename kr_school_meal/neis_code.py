import requests


def get_code(school_name):
    result = {}

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    data = {
        'HG_CD': '',
        'SEARCH_KIND': '',
        'HG_JONGRYU_GB': '',
        'GS_HANGMOK_CD': '',
        'GS_HANGMOK_NM': '',
        'GU_GUN_CODE': '',
        'SIDO_CODE': '',
        'GUGUN_CODE': '',
        'SRC_HG_NM': school_name
    }

    response = requests.post('https://www.schoolinfo.go.kr/ei/ss/Pneiss_a01_l0.do',
                             headers=headers, data=data).json()

    for i in response:
        sch = response[i]
        if sch:
            for c in sch:
                code = c['SCHUL_CODE']
                gyc = c['LCTN_NM']
                kind = c['SCHUL_KND_SC_CODE']
                name = c['SCHUL_NM']
                result[name] = {'코드': code, '교육청': gyc, '종류': kind}

    if result:
        return result
    else:
        return False


# get_code('이의')
