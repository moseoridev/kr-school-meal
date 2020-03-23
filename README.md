# Korea School Meal

대한민국 학교들의 급식 정보를 알려줍니다. 모든 정보는 [NEIS](https://www.neis.go.kr/)에서 얻어옵니다.

# How To Use

```
> pip install kr_school_meal
> from kr_school_meal import meal, neis_code
```

- `neis_code.py` - 각 학교의 NEIS 코드를 가져옵니다.

```
> neis_code.get_code('이의고등학교')
> {'이의고등학교': {'코드': 'J100006813', '교육청': '경기', '종류': '04'}}
```

- `meal.py` - 지정일의 급식을 가져옵니다.

```
> meal.get_meal('J100005882', '경기', '04', datetime.datetime(2019, 10, 10))
> ['[중식]', '우유', '차조밥', '오징어찌개', '새송이버섯불고기', '녹두빈대떡', '열무김치', '머루포도']
```

# Troubleshooting

문제가 있다면 issue를 남겨주세요.

# Links

[GitHub](https://github.com/moseoridev/kr-school-meal)<br>
[PyPI](https://pypi.org/project/kr-school-meal/)

---

made by [moseoridev](https://github.com/moseoridev/) with <3
