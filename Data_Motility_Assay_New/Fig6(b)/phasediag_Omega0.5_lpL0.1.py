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
    [0.85199, 0.82892, 0.844029, 0.8361290, 0.813, 0.81156800, 0.794151, 0.7079],
    [0.8471, 0.83864, 0.829922, 0.82067, 0.79402, 0.699939, 0.55982, 0.78196],
    [0.8444, 0.836782, 0.810832, 0.80604, 0.697458, 0.679209, 0.9304, 0.9999],
    [0.83032, 0.814030, 0.776139, 0.62839, 0.868153, 0.99661, 1, 1],
    [0.78752, 0.67580, 0.51595, 0.90873, 0.9999, 1, 1, 1],
    [0.63983,0.868435, 0.99999, 1, 1, 1, 1, 1],
    [0.9996, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
])

cmap = ListedColormap(['skyblue', 'tomato'])
binary_matrix = np.where(matrix > 0.8, 1, 0)
fig, ax = plt.subplots(figsize=(8, 6.5))
#heatmap = sns.heatmap(binary_matrix, cmap=cmap, annot=False, linewidths=0, linecolor='white', cbar=False, ax=ax)

for i in range(matrix.shape[0]):
	for j in range(matrix.shape[1]):
		value = matrix[i, j]
		if value > 0.85199:
			marker = 'o' 
			color = 'red'
			edge_color = 'red'
			edge_thickness = 3
			size = 100

		elif 0.8 < value <= 0.85199:
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
plt.xlabel('\\boldmath$K_{trap}\sigma^2/k_BT$', fontsize=21)
plt.ylabel('\\boldmath$Pe$', fontsize=21)
plt.title('\\boldmath$(b)$', fontsize=26)

yticks = [29.7, 25.7, 21.8, 17.8, 13.8, 9.9, 5.9, 1.9]
xticks = [0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]

ax.set_xticks(np.arange(len(xticks)) + 0.5)
ax.set_yticks(np.arange(len(yticks)) + 0.5)

ax.set_xticklabels(['\\boldmath{$%.2f$}' % tick for tick in xticks], fontsize=21)
ax.set_yticklabels(['\\boldmath{$%.1f$}' % tick for tick in yticks], fontsize=21)

border_width = 3  
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.text(-0.2, 0.05, '\\boldmath$(\\times 10^4)$', fontsize=21, fontweight='bold')
#plt.text(0.7, 0.9, '\\boldmath$(b)$', fontsize=22, fontweight='bold')

plt.savefig('Omega0.5_u10_heatmap_two_colors.pdf')

