s = pd.Series([1, 2, 3, np.nan, np.nan, 6, 7, np.nan, np.nan])
s

# interpolation 메서드를 이용한 결측치 내삽
s.interpolate(
    method="spline", order=1, limit_direction="forward", limit=2
)

