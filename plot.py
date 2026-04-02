import matplotlib.pyplot as plt
names=['A','B','C','D']
Marks=[85,90,78,92]
plt.scatter(names,Marks)
plt.xlabel('Names')
plt.ylabel('Marks')
plt.title(' Marks of students')
plt.savefig('scatter_plot.png')
print("Scatter plot saved as scatter_plot.png")