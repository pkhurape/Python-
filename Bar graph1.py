import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2] ,label =" 2020",color='r')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='2019',color='g')

plt.legend()
plt.xlabel('Bar number')
plt.ylabel('Bar Height')
plt.title('Bar graph')
plt.show()