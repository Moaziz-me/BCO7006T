import pandas as pd

a = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
# print(a[a < 9])
# print(a/2)

# sa = pd.Series([a, 4,pd.NaN, -9])

# print(sa)

data = {'color': ['blue', 'green', 'yellow', ' red', 'white'],
        'object': ['ball', 'pen', 'pencil', 'paper', 'mug'],
        'price': [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
# print(frame)

# d1 = pd.DataFrame([
#     {'object': 'pen', 'green', 'yellow', ' red', 'white'},
# {'object': 'ball', 'pen', 'pencil', 'paper', 'mug'},
# {'price': }])

print(frame)
# print(frame.columns)
# print(frame.index)
# print(frame['price'])
# print(frame.price)
print(frameframe['new']=12)