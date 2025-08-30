# Matpolib all kind of graph

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# plt.plot(x,y)
# plt.title("marks")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# plt.scatter(x,y,color="red",marker="x")
# plt.title("marks")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# import matplotlib.pyplot as plt

# data = [1,1,1,2,2,2,3,4,5]

# plt.hist(data, bins=3, color="red", edgecolor="black")
# plt.title("Histrogram")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# plt.bar(x, y, color="red")
# plt.title("Bar chart")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = ['A','B','C','D','E']

# plt.pie(x, labels=y, autopct='%1.1f%%', colors=['gold','Yellow','red','blue'])
# plt.title("Pie chart")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# data = []
# for i in range(1, 4):
#     a = np.random.randint(0, i + 1, 100)
#     data.append(a)

# plt.boxplot(data)
# plt.title("Box chart")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# import random 

# scores = [random.randint(40,100) for i in range(20)]
# mean_score = np.mean(scores)
# plt.figure(figsize=(10,6))
# plt.scatter(range(1,21),scores,color='blue',label = 'student_score')
# plt.axhline(y=mean_score,color='red',linestyle='--',label=f'mean score:{mean_score:2f}')
# plt.title("enter scores of 20 students")
# plt.xlabel("student number")
# plt.ylabel("score")
# plt.xticks(range(1,21))
# plt.legend()
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y1 = [2,3,5,9,11]
# y2 = [1,4,6,8,10]

# plt.plot(x,y1,label='series 1',color='blue')
# plt.plot(x,y2,label='series 2',color='red')
# plt.title("mulitiple line plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,3,5,9,11]

# plt.plot(x,y,ls='--',color='purple',marker='o',markersize=8,linewidth=2)
# plt.title("custom plot")
# plt.grid(True)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# import matplotlib.pyplot as plt

# # Temperature data over time
# time = [1, 2, 3, 4, 5, 6, 7, 8]  # Hours
# temperature = [20, 22, 25, 28, 30, 29, 27, 24]  # Temperature in Celsius

# plt.plot(time, temperature, ls='--', color='red', marker='o', markersize=8, linewidth=2)
# plt.title("Temperature Measurement")
# plt.grid(True)
# plt.xlabel("Time (hours)")
# plt.ylabel("Temperature (°C)")
# plt.show()