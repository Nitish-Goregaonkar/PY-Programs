days=['Mon','Tue','wed','thur','fri','sat','sun']
expenses=[200,150,300,250,400,350,220]
import matplotlib.pyplot as plt
plt.plot(days, expenses, marker='o', color='blue', linestyle='-')
plt.xlabel("days of week")
plt.ylabel("expenses in RS")
plt.grid(True)
plt.show()