import requests
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli


#cookie = {'steamLoginSecure': '76561198165481402%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MTFGOV8yMTlBRDVDNV9DN0EyRCIsICJzdWIiOiAiNzY1NjExOTgxNjU0ODE0MDIiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY2ODYxNjQxNywgIm5iZiI6IDE2NTk4ODk4OTksICJpYXQiOiAxNjY4NTI5ODk5LCAianRpIjogIjExRjlfMjE5QUQ1QzVfRTAxQTQiLCAib2F0IjogMTY2ODUyOTg5OSwgInJ0X2V4cCI6IDE2ODY1MDEwOTcsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxNjUuODIuMjM3LjUyIiwgImlwX2NvbmZpcm1lciI6ICIxNzIuNTYuMjE2LjIxMCIgfQ.yI8YBO96X9Dad9EaAPnC0rByOQnS3mz5wpxJ_nIMT5SKNzPcj7oprOaj5kgNv3orO4xFVo_e9lhsLZSOAQeWCw'}
#data = requests.get('http://steamcommunity.com/market/pricehistory/?country=US&currency=1&appid=730&market_hash_name=Falchion%20Case', cookies=cookie)
#print(data.content)
#print(np.dtype(data.content))

#r = bernoulli.rvs(0.5, 1)
#print(r)

data = requests.get("https://csgofloat.com/db?name=AK-47%20%7C%20Case%20Hardened&defIndex=7&paintIndex=44&min=0&max=1")
print(data.content)