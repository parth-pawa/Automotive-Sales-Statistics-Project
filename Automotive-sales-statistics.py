file1 = open(r"/Users/parthpawa/PycharmProjects/ ITM 200/Data.csv",'r')
statFile = open(r'/Users/parthpawa/PycharmProjects/ ITM 200/stats.txt','w')

import matplotlib.pyplot as plt

m21 = 0
m22 = 0
text1 = file1.readlines()
salesIn2021 = []
salesIn2022 = []
sales2 = []
months = {}
for line in text1:
    c = line.split(',')
    if c[0] == 'Month' or c[0] == 2022:
        continue
    count = 1
    sales = 0
    while count <= 12:
        sales = int(c[count]) + sales
        count = count + 1
    sales2.append(sales)

    if '2021' == c[0]:
        count = 1
        for i in range(1,13,1):
            salesIn2021.append(int(c[i]))
            if count < 7:
                m21 += int(c[i])
            count = count + 1
    if '2022' == c[0]:
        for i in range(1,7,1):
            salesIn2022.append(int(c[i]))
            m22 += int(c[i])
sgr = (m22-m21) / m21
projected = []
for i in range(7, 13, 1):
    projected.append(float("{:.2f}".format(salesIn2021[i-1] + salesIn2021[i-1]*sgr)))

x = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

y = sales2[0:10]
for i in range(10):
    statFile.write(str(x[i]) + ' = ' + str(y[i]) + '\n')
plt.figure(1)
plt.bar(x, y)
plt.show()


statFile.write('\nSGR:' + str(sgr))
statFile.write("\nEstimated sale in month M of 2022: " + str(projected))

x2 = [' Jul ', ' Aug', ' Sep ', ' Oct ', ' Nov ', ' Dec ']
y2 = projected
plt.figure(2)
plt.barh(x2,y2)
plt.show()



