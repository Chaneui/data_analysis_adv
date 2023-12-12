import pandas as pd
import numpy as np

df = pd.read_csv('./datasets/bike_rentals/bike_rentals.csv')
df.iloc[2, 3] = np.nan # 결측치를 임의로 만들기 위해 추가
df.head(10)