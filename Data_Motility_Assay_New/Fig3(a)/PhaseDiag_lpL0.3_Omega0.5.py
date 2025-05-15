import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'Droid Sans']
plt.rcParams['text.color'] = 'black'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['figure.dpi'] = 800  

plt.close('all')

matrix = np.array([
    [0.810285, 0.80775000, 0.8110535, 0.809458, 0.813259, 0.8051335, 0.803793, 0.808473],
    [0.814564, 0.8144235, 0.815416, 0.80729100, 0.8067960, 0.80629, 0.80870, 0.808600],
    [0.814444, 0.8061515, 0.814361, 0.82409650, 0.823510, 0.804280, 0.801672, 0.79411150],
    [0.8116925, 0.805377, 0.809755, 0.8200015, 0.810470, 0.793120, 0.770363, 0.4827247],
    [0.814331, 0.8269925, 0.81553, 0.777538, 0.7417735, 0.731382, 0.99814, 1],
    [0.759708, 0.66867, 0.720282, 0.766373, 0.99998, 1, 1, 1],
    [0.73772, 0.94818, 0.99996, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
])

cmap = ListedColormap(['skyblue', 'tomato'])
binary_matrix = np.where(matrix > 0.8, 1, 0)
fig, ax = plt.subplots(figsize=(8, 6))
#heatmap = sns.heatmap(binary_matrix, cmap=cmap, annot=False, linewidths=0, linecolor='white', cbar=False, ax=ax)

for i in range(matrix.shape[0]):
	for j in range(matrix.shape[1]):
		value = matrix[i, j]
		if value > 0.9:
			marker = 'o' 
			color = 'red'
			edge_color = 'red'
			edge_thickness = 3
			size = 100
		elif 0.8 < value <= 0.9:
			marker = 'D'  
			color = 'red'
			edge_color = 'green'
			edge_thickness = 3
			size = 100
		else:
			marker = 's' 
			color = 'blue'
			edge_color = 'blue'
			edge_thickness = 3
			size = 100
		ax.scatter(j + 0.5, i + 0.5, marker=marker, s=size, color=color,facecolor ='none',edgecolors=edge_color,linewidths=edge_thickness)
			
ax.invert_yaxis()
plt.xlabel('\\boldmath$K_{trap}\sigma^2/k_BT$', fontsize=20)
plt.ylabel('\\boldmath$Pe$', fontsize=20)
plt.title('\\boldmath$(a)$', fontsize=25)

yticks = [29.7, 25.7, 21.8, 17.8, 13.8, 9.9, 5.9, 1.9]
xticks = [0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]

ax.set_xticks(np.arange(len(xticks)) + 0.5)
ax.set_yticks(np.arange(len(yticks)) + 0.5)

ax.set_xticklabels(['\\boldmath{$%.2f$}' % tick for tick in xticks], fontsize=16)
ax.set_yticklabels(['\\boldmath{$%.1f$}' % tick for tick in yticks], fontsize=16)

border_width = 3  
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)

plt.text(-0.2, 0.05, '\\boldmath$(\\times 10^4)$', fontsize=16, fontweight='bold')
#plt.text(0.7, 0.9, '\\boldmath$(a)$', fontsize=22, fontweight='bold')

plt.savefig('Omega0.5_u3.33_heatmap_two_colors.pdf')

