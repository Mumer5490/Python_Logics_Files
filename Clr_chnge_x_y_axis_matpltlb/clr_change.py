import matplotlib.pyplot as plt
plt.plot([1,2,3])
ax = plt.gca()
ax.spines["bottom"].set_color("green")      # x axis line
ax.spines["top"].set_color("purple")
ax.spines["left"].set_color("brown")        # y axis line
ax.tick_params(axis="x", colors="red")      # x tick labels
ax.tick_params(axis="y", colors="orange")   # y tick labels
plt.show()