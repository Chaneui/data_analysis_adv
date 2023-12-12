import seaborn as sns

df = sns.load_dataset('penguins')
df.head()

# query 메서드를 이용한 부등호 필터링
df.query('bill_length_mm > 55')

# 위 코드와 동일한 결과를 얻음
df[df['bill_length_mm'] > 55]

# 위 코드와 동일한 결과를 얻음
df.loc[df['bill_length_mm'] > 55]

# query 메서드를 이용한 and 조건문 연결
df.query('bill_length_mm > 55 and species == "Gentoo"')

# query 메서드 조건문의 외부 변수 참조
length = 55
species = 'Gentoo'

df.query('bill_length_mm >= @length and species == @species')

# query 메서드 조건문의 문자열 메서드 사용
df.query('island.str.contains("oe")', engine='python')

df.query('species.str.endswith("e")', engine='python')

# isin을 이용한 리스트 내 항목 참조
filtering = ["Adelie", "Chinstrap"]
df.query('species.isin(@filtering)', engine='python')