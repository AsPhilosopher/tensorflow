import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([3, 5, 7, 6, 2, 6, 10, 15])
plt.plot(x, y, 'b')  # 绘制折线图 1.x坐标 2.y坐标 3.color
plt.show()
plt.plot(x, y, 'g', lw=10)  # 线条宽带
plt.show()

plt.bar(x, y, 0.5, alpha=0.6, color='b')  # 0.5是柱状图占用比例
plt.show()
