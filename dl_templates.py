import requests
diff = 3
size = 9

layout = {'size': size, 'level': diff}
r = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/', params=layout, timeout=3)
r = r.json()
r = r['squares']
print(r)

diff_1 = [{'x': 0, 'y': 0, 'value': 5}, {'x': 0, 'y': 3, 'value': 8}, {'x': 0, 'y': 4, 'value': 1},
          {'x': 0, 'y': 8, 'value': 4}, {'x': 1, 'y': 1, 'value': 2}, {'x': 1, 'y': 4, 'value': 5},
          {'x': 1, 'y': 5, 'value': 4}, {'x': 1, 'y': 6, 'value': 1}, {'x': 1, 'y': 7, 'value': 6},
          {'x': 2, 'y': 3, 'value': 7}, {'x': 2, 'y': 5, 'value': 9}, {'x': 2, 'y': 8, 'value': 5},
          {'x': 3, 'y': 2, 'value': 1}, {'x': 3, 'y': 6, 'value': 7}, {'x': 3, 'y': 7, 'value': 5},
          {'x': 3, 'y': 8, 'value': 6}, {'x': 4, 'y': 0, 'value': 2}, {'x': 4, 'y': 3, 'value': 6},
          {'x': 4, 'y': 4, 'value': 9}, {'x': 4, 'y': 5, 'value': 7}, {'x': 5, 'y': 0, 'value': 8},
          {'x': 5, 'y': 1, 'value': 7}, {'x': 5, 'y': 2, 'value': 6}, {'x': 5, 'y': 5, 'value': 1},
          {'x': 5, 'y': 6, 'value': 2}, {'x': 6, 'y': 1, 'value': 5}, {'x': 6, 'y': 2, 'value': 9},
          {'x': 6, 'y': 3, 'value': 1}, {'x': 6, 'y': 5, 'value': 3}, {'x': 6, 'y': 8, 'value': 2},
          {'x': 7, 'y': 1, 'value': 1}, {'x': 7, 'y': 3, 'value': 4}, {'x': 7, 'y': 6, 'value': 5},
          {'x': 7, 'y': 7, 'value': 9}, {'x': 7, 'y': 8, 'value': 8}, {'x': 8, 'y': 0, 'value': 7},
          {'x': 8, 'y': 1, 'value': 8}, {'x': 8, 'y': 3, 'value': 9}, {'x': 8, 'y': 4, 'value': 6},
          {'x': 8, 'y': 7, 'value': 1}, {'x': 8, 'y': 8, 'value': 3}]

diff_2 = [{'x': 0, 'y': 2, 'value': 6}, {'x': 0, 'y': 4, 'value': 2}, {'x': 0, 'y': 6, 'value': 3},
          {'x': 0, 'y': 8, 'value': 1}, {'x': 1, 'y': 4, 'value': 7}, {'x': 1, 'y': 6, 'value': 6},
          {'x': 2, 'y': 0, 'value': 5}, {'x': 2, 'y': 1, 'value': 1}, {'x': 2, 'y': 7, 'value': 8},
          {'x': 3, 'y': 0, 'value': 3}, {'x': 3, 'y': 6, 'value': 7}, {'x': 3, 'y': 8, 'value': 8},
          {'x': 4, 'y': 3, 'value': 3}, {'x': 4, 'y': 5, 'value': 5}, {'x': 4, 'y': 6, 'value': 1},
          {'x': 5, 'y': 0, 'value': 8}, {'x': 5, 'y': 2, 'value': 5}, {'x': 5, 'y': 5, 'value': 7},
          {'x': 5, 'y': 7, 'value': 3}, {'x': 5, 'y': 8, 'value': 9}, {'x': 6, 'y': 1, 'value': 8},
          {'x': 6, 'y': 3, 'value': 7}, {'x': 6, 'y': 7, 'value': 1}, {'x': 7, 'y': 0, 'value': 9},
          {'x': 7, 'y': 4, 'value': 5}, {'x': 7, 'y': 8, 'value': 3}, {'x': 8, 'y': 2, 'value': 2},
          {'x': 8, 'y': 4, 'value': 3}, {'x': 8, 'y': 5, 'value': 6}, {'x': 8, 'y': 6, 'value': 9}]

diff_3 = [{'x': 0, 'y': 1, 'value': 2}, {'x': 0, 'y': 4, 'value': 9}, {'x': 0, 'y': 7, 'value': 8},
          {'x': 1, 'y': 0, 'value': 9}, {'x': 1, 'y': 8, 'value': 3}, {'x': 2, 'y': 2, 'value': 3},
          {'x': 2, 'y': 4, 'value': 5}, {'x': 3, 'y': 1, 'value': 1}, {'x': 3, 'y': 5, 'value': 7},
          {'x': 3, 'y': 6, 'value': 9}, {'x': 4, 'y': 0, 'value': 6}, {'x': 4, 'y': 5, 'value': 5},
          {'x': 4, 'y': 8, 'value': 1}, {'x': 5, 'y': 3, 'value': 9}, {'x': 5, 'y': 6, 'value': 6},
          {'x': 6, 'y': 2, 'value': 6}, {'x': 7, 'y': 3, 'value': 6}, {'x': 8, 'y': 1, 'value': 9},
          {'x': 8, 'y': 5, 'value': 8}, {'x': 8, 'y': 7, 'value': 6}]
