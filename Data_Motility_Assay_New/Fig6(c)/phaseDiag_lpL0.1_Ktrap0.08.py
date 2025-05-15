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
    [1, 1, 0.6954, 0.7637, 0.81156800, 0.825392,0.8301, 0.8336,0.84574], #75
    [1, 1, 0.9845, 0.5262, 0.699939,0.806377, 0.8143, 0.8230,0.83175], #65
    [1, 1, 0.9999, 0.9447, 0.679209, 0.6927975, 0.7563,0.7679,0.784922], #55
    [1, 1, 1, 1, 0.99661, 0.92660, 0.6210675, 0.57660,0.622204 ], #45
    [1, 1, 1, 1, 1, 1, 0.9999, 0.9997,0.9516], #35
    [1, 1, 1, 1, 1, 1, 1, 1,1], #25
    [1, 1, 1, 1, 1, 1, 1, 1,1], #15
    [1, 1, 1, 1, 1, 1, 1, 1,1] #5
])

cmap = ListedColormap(['skyblue', 'tomato'])
binary_matrix = np.where(matrix > 0.8, 1, 0)
fig, ax = plt.subplots(figsize=(8, 6.5))
#heatmap = sns.heatmap(binary_matrix, cmap=cmap, annot=False, linewidths=0, linecolor='white', cbar=False, ax=ax)

for i in range(matrix.shape[0]):
	for j in range(matrix.shape[1]):
		value = matrix[i, j]
		if value > 0.85:
			marker = 'o' 
			color = 'red'
			edge_color = 'red'
			edge_thickness = 3
			size = 100

		elif 0.8 <= value <= 0.85:
			marker = 'D'  
			color = 'green'
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
plt.xlabel('\\boldmath$\Omega$', fontsize=21)
plt.ylabel('\\boldmath$Pe$', fontsize=21)
plt.title('\\boldmath$(c)$', fontsize=26)

yticks = [29.7, 25.7, 21.8, 17.8, 13.8, 9.9, 5.9, 1.9]
xticks = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9]

ax.set_xticks(np.arange(len(xticks)) + 0.5)
ax.set_yticks(np.arange(len(yticks)) + 0.5)

ax.set_xticklabels(['\\boldmath{$%.2f$}' % tick for tick in xticks], fontsize=21)
ax.set_yticklabels(['\\boldmath{$%.1f$}' % tick for tick in yticks], fontsize=21)

border_width = 3  
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.text(-0.2, 0.05, '\\boldmath$(\\times 10^4)$', fontsize=19, fontweight='bold')
#plt.text(0.7, 0.9, '\\boldmath$(d)$', fontsize=22, fontweight='bold')

plt.savefig('K0.08_u10_coexistence.pdf')

