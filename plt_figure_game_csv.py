import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取五感、游戏得分、电影得分
filename = 'mypython.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    senses,  games, movies = [], [], []
    for row in reader:
            sense = row[0]
            game = int(row[1])
            movie = int(row[2])
            senses.append(sense)
            games.append(game)
            movies.append(movie)
    print(game)
    print(movie)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.scatter(senses, games, c='red', alpha=1)
plt.scatter(senses, movies, c='blue', alpha=1)
plt.plot(senses, games, c='red', alpha=0.6)
plt.plot(senses, movies, c='blue', alpha=0.6)
plt.fill_between(senses, games, movies, facecolor='blue', alpha=0.05)

# 设置图形的格式
plt.title("Five sense design scores for games and movies", fontsize=24)
plt.xlabel('', fontsize=16)
#fig.autofmt_xdate() # 改变x轴坐标斜着显示
plt.ylabel("Score 0-10", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.legend(loc='upper right', labels=['game', 'movie'])

plt.show()
