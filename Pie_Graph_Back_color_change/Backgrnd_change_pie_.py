# importing libraries
import matplotlib.pyplot as plt
import seaborn
# text color change
plt.rcParams['text.color'] = 'white'

# Background_color_change
fig, ax = plt.subplots(figsize = (20,12))
ax.grid(False)
# plt.style.use('ggplot')
fig.set_facecolor('maroon') 

# declaring data
data = [44, 45, 40]
keys = ['Total Tweetes', 'Positive Tweets', 'Negative Tweets']

# define Seaborn color palette to use
palette_color = seaborn.color_palette('bright')

# plotting data on chart
plt.pie(data, labels=keys, colors=palette_color,  autopct='%.0f%%' )
# fig.set_facecolor('lightgrey')

# displaying chart
plt.show()

