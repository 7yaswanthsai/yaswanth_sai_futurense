import matplotlib.pyplot as plt
import numpy as np

#Piechart
department = ["HR", "Sales", " Technical", "Service"]
count = [25, 19, 42, 13]
plt.pie(count, labels = department, autopct="%1.2f%%")
plt.show()

department = ["HR", "Sales", " Technical", "Service"]
count = [25, 19, 42, 13]
colors = ['red', 'green', 'blue', 'yellow']
explode = [0,0,0.3,0]
plt.pie(count,labels=department,colors=colors,explode=explode,autopct='%1.2f%%',shadow=True,startangle=90)
plt.show()

#Lineplot
x = [1, 2, 3, 4, 5, 6]
y = [4, 5, 6, 3, 2, 3]
plt.plot(x, y, color="blue")
plt.title("x vs y")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

#Multiple Lineplots
x=[1,2,3,4,5,6]
y=[4,5,6,3,2,3]
plt.plot(x,y,linestyle='-.',marker='*')
x1=[2,4,6,8,10]
y1=[1,2,3,4,5]
plt.plot(x1,y1,color="red",marker="o")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Multiple plot")
plt.show()

#Subplot
plt.subplot(2,2,1) 
plt.plot(x,y,'y')
plt.subplot(2,2,2)
plt.plot(x1,y1,color="red",marker="o")
plt.subplot(2,2,3)
plt.plot(x,y,'g')
plt.show()

# line styles

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x,dev_y,color= 'k', linestyle = '--',label = 'All Developers')
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x,py_dev_y,color = 'r', label ='Python Developers')
plt.title('Median salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()

#Barchart
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [25008, 42000, 46752, 50065, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(ages_x,dev_y,color= 'blue', label = 'All Developers')
plt.title('Median salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()

#Lineplot + Barchart
import matplotlib.pyplot as plt
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [25008, 42000, 46752, 50065, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(ages_x,dev_y,color= 'r', label = 'All Developers')
py_dev_y = [45372, 48876, 53850, 55250, 63016,
            65998, 68125, 70000, 71496, 75370, 85066]
plt.plot(ages_x,
         py_dev_y,
         color = 'blue',
         linewidth = 3,
         marker = 'o',
         label ='Python Developers')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,
         js_dev_y,
         color = 'yellow',
         linewidth = 3,
         marker = 'X',
         label ='JavaScript Developers')

plt.title('Median salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()

#Scatterplot
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(grades_range, girls_grades, color='pink')
plt.scatter(grades_range, boys_grades, color='blue')
plt.xlabel('Grades Range')
plt.ylabel('Grades Scored')
plt.title('Scatter plot')
plt.show()

#Histogram
x = np.random.uniform(0,4,100)
plt.style.use("ggplot")
plt.hist(x,5, color="skyblue", edgecolor="black")   
plt.show()

#Normal Distribution
x=np.random.normal(5,1,10000)
plt.hist(x,200)
plt.show()

#Areaplot
x=range(1,6)
y=[1,5,7,9,1]
plt.fill_between(x, y)
plt.show()

#Boxplot
x=range(1,6)
y=[1,4,6,8,4]
plt.fill_between(x, y)
plt.show()



