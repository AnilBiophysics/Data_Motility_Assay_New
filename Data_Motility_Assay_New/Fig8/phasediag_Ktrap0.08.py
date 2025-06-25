import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Set LaTeX and font properties
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

matrix = np.array([
    [2.127,2.055,1.914,1.867,1.827,1.793,1.690,1.873,2.484],
    [1.816,2.073,2.205,2.392,2.354,2.520,2.601,2.710,2.516],
    [1.728,2.112,2.115,2.558,2.604,2.868,2.562,2.663,2.207],
    [1.915,2.015,2.425,2.503,2.088,1.536,1.562,1.495,1.304],
    [1.795,2.107,2.179,1.583,1.169,1.085,0.794,0.864,0.660],
    [1.966,2.279,1.327,0.943,0.779,0.766,0.611,0.530,0.529],
    [1.999,1.743,1.094,0.862,0.688,0.611,0.556,0.559,0.529],
    [2.083,1.643,1.189,0.843,0.675,0.577,0.549,0.564,0.571],
])

low_threshold = 1
high_threshold = 1

custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", ["#FFCCCC", "#87CEEB", "#4682B4", "#00008B"])
matrix_normalized = matrix 
#matrix_normalized = np.clip(matrix_normalized, 0, 1)

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(matrix_normalized, cmap=custom_cmap, interpolation="bicubic", aspect="auto")

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        value = matrix[i, j]
        if value < low_threshold:
            ax.scatter(j, i, marker='o', facecolor='none', edgecolor='red', s=50, linewidths=2.5, label="Low" if (i == 0 and j == 0) else "")
        elif low_threshold <= value < high_threshold:
            ax.scatter(j, i, marker='s', facecolor='none', edgecolor='lightblue', s=40, linewidths=2.0, label="Medium" if (i == 0 and j == 1) else "")
        else:
            ax.scatter(j, i, marker='D', facecolor='none', edgecolor='black', s=50, linewidths=2.5, label="High" if (i == 0 and j == 2) else "")

cbar = plt.colorbar(im, ax=ax)
#cbar.set_label('\\boldmath$\\langle \psi_N^2 \\rangle$', fontsize=20)

tick_positions = [1,1.5,2,2.5]
cbar.set_ticks(tick_positions)
cbar.set_ticklabels([f'\\boldmath{{$%.1f$}}' % tick for tick in tick_positions])
cbar.ax.tick_params(labelsize=16)
cbar.set_label('\\boldmath$\langle |\psi_N| \\rangle$', fontsize=18, labelpad=10)

yticks = [1.9, 5.9, 9.9, 13.8, 17.8, 21.8, 25.7, 29.7]
xticks = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,0.8,0.9]

ax.set_xticks(np.arange(len(xticks)))
ax.set_yticks(np.arange(len(yticks)))

ax.set_xticklabels(['\\boldmath{$%.1f$}' % tick for tick in xticks], fontsize=18)
ax.set_yticklabels(['\\boldmath{$%.1f$}' % tick for tick in yticks], fontsize=18)
#ax.set_title(r"\boldmath{$(a)$}", fontsize=20)

plt.xlabel('\\boldmath$\Omega$', fontsize=21, fontweight='bold')
plt.ylabel('\\boldmath$Pe$', fontsize=21, fontweight='bold')

ax.invert_yaxis()

handles, labels = ax.get_legend_handles_labels()
unique_handles_labels = list(dict(zip(labels, handles)).items())  # Remove duplicates
#ax.legend([h for l, h in unique_handles_labels], [l for l, h in unique_handles_labels], fontsize=14, loc="upper right")


#plt.ylim(-0.5, 4.5)
plt.tight_layout()
plt.text(-1.6, 7.4, '\\boldmath$(\\times 10^4)$', fontsize=16, fontweight='bold')
plt.savefig("Phase_diagram_varyOmega_with_markers.pdf")

