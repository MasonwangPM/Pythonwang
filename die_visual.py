import pygal
from die import Die

# 创建两个8面骰子
die_1 = Die(8)
die_2 = Die(8)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#print(results)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#将for循环替换成列表解析
#frequencies = [results.count(value) for value in range(2, max_result+1)]

# 对结果进行可视化（直方图）
hist = pygal.Bar()

hist.title = "Results of rolling two D8 100000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequuency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')

print(frequencies)
