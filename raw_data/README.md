# How to Use Raw Data

the data is collected by the [**Data Collection.ipynb**](https://github.com/lqiqiqi/i-temp/blob/master/Data%20Collection.ipynb)

```
import time
df.to_csv("raw_data/data_{}_{}.csv".format(time.strftime("%Y%m%d_%H%M", time.localtime()), inp), mode='a', index=False, header=True)
```

Therefore, the raw data file name included datetime they are collected and comfort levels (their targets)



o cold, 1 for cold, 2 for comfortable, 3 for hot and 4 for too hot