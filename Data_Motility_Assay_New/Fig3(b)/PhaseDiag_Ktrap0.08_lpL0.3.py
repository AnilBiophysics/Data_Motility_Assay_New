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
    [1, 0.6726415, 0.81390, 0.806973, 0.8051335, 0.806724, 0.80523200, 0.80871,0.80576],
    [1, 0.78494, 0.80175, 0.8162335, 0.80625, 0.812205, 0.811644, 0.810341,0.806429],
    [1, 0.9999, 0.78421, 0.7944125, 0.804280, 0.813006, 0.802013, 0.809959,0.811140],
    [1, 1, 0.9631, 0.76026, 0.793120 , 0.82010, 0.80957, 0.803739,0.79714200],
    [1, 1, 1, 0.99998, 0.731382, 0.75964, 0.78625, 0.76158,0.789509],
    [1,1, 1, 1, 1, 0.9999, 0.9999, 0.9541,0.537143],
    [1, 1, 1, 1, 1, 1, 1, 1,1],
    [1, 1, 1, 1, 1, 1, 1, 1,1]
])

cmap = ListedColormap(['skyblue', 'tomato'])
binary_matrix = np.where(matrix > 0.8, 1, 0)
fig, ax = plt.subplots(figsize=(8, 6))
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
plt.xlabel('\\boldmath$\Omega$', fontsize=20)
plt.ylabel('\\boldmath$Pe$', fontsize=20)
plt.title('\\boldmath$(b)$', fontsize=25)

yticks = [29.7, 25.7, 21.8, 17.8, 13.8, 9.9, 5.9, 1.9]
xticks = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9]

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
#plt.text(0.7, 0.9, '\\boldmath$(c)$', fontsize=22, fontweight='bold')

plt.savefig('K0.08_u3.33_coexistence.pdf')

