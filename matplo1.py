from matplotlib import pyplot as plt
players="ronaldo" , "Messi" , "Neymar", "Lewando"
score=[45,30,15,10]
explode=(0.1,0,0,0)
figl, axl=plt.subplots()
axl.pie(score, explode=explode, labels=players, shadow=True, startangle=90)
axl.axis("equal")
plt.show()