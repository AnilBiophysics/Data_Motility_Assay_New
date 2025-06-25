import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator


plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'Droid Sans']
plt.rcParams['text.color'] = 'black'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['figure.dpi'] = 400

t5, r2_5, r4_5 = np.loadtxt('Pe1.9-1e4_K0.5_avg_r2_r4_t.txt', unpack=True)
t25, r2_25, r4_25 = np.loadtxt('Pe9.9-1e4_K0.5_avg_r2_r4_t.txt', unpack=True)
t65, r2_65, r4_65 = np.loadtxt('Pe25.7-1e4_K0.5_avg_r2_r4_t.txt', unpack=True)

t65_K0, r2_65_K0, r4_65_K0 = np.loadtxt('Pe25.7-1e4_K0_avg_r2_r4_t.txt', unpack=True)
t65_K0_1, r2_65_K0_1, r4_65_K0_1 = np.loadtxt('Pe25.7-1e4_K0.1_avg_r2_r4_t.txt', unpack=True)
t65_K0_5, r2_65_K0_5, r4_65_K0_5 = np.loadtxt('Pe25.7-1e4_K0.5_avg_r2_r4_t.txt', unpack=True)

# Calculate kurtosis
kurtosis_5 = r4_5 / (3 * (r2_5**2)) - 1
kurtosis_25 = r4_25 / (3 * (r2_25**2)) - 1
kurtosis_65 = r4_65 / (3 * (r2_65**2)) - 1

kurtosis_65_K0 = r4_65_K0 / (3 * (r2_65_K0**2)) - 1
kurtosis_65_K0_1 = r4_65_K0_1 / (3 * (r2_65_K0_1**2)) - 1
kurtosis_65_K0_5 = r4_65_K0_5 / (3 * (r2_65_K0_5**2)) - 1

fig, ax = plt.subplots(1, 2, figsize=(9, 4))

# first subplot (ax[0])
ax[0].plot(t5[::10]/62511.75, kurtosis_5[::10], label="\\boldmath$Pe=1.9\\times 10^4$", color='darkblue', linestyle='-', markersize=2,marker='^', markeredgecolor='darkblue', markerfacecolor='none')
ax[0].plot(t25/62511.75, kurtosis_25, label="\\boldmath$Pe=9.9\\times 10^4$", color='red', marker='^', linestyle='--', linewidth=0.5, markersize=1, markeredgecolor='red', markerfacecolor='none')
ax[0].plot(t65/62511.75, kurtosis_65, label="\\boldmath$Pe = 25.7\\times 10^4$", color='green', linestyle='-', markersize=2, markeredgecolor='green', markerfacecolor='none')

ax[0].set_xscale('log')
ax[0].set_xticks([1e-5, 1e-4, 1e-3, 1e-2, 1e-1,1e0])
ax[0].set_xticklabels(['\\boldmath$10^{-5}$', '\\boldmath$10^{-4}$', '\\boldmath$10^{-3}$', '\\boldmath$10^{-2}$', '\\boldmath$10^{-1}$','\\boldmath$10^{0}$'], fontsize=12)
ax[0].set_yticks([-0.42, -0.40, -0.38, -0.36, -0.34, -0.32, -0.30])
ax[0].set_yticklabels(['\\boldmath$-0.42$', '\\boldmath$-0.40$', '\\boldmath$-0.38$', '\\boldmath$-0.36$', '\\boldmath$-0.34$', '\\boldmath$-0.32$', '\\boldmath$-0.30$'], fontsize=12)
ax[0].set_xlabel('\\boldmath$\Delta t/\\tau$', fontsize=12)
ax[0].set_ylabel('\\boldmath$\mathcal{K}$', fontsize=12)
ax[0].legend(loc='best', fontsize=13)
ax[0].set_xlim(2*10**-5, 10**-1)
ax[0].set_ylim(-0.42, -0.30)

#second subplot (ax[1])
ax[1].plot(t65_K0[::20]/62511.75, kurtosis_65_K0[::20], label="\\boldmath$K_{trap}=0$", color='blue', marker='^', linestyle=':', markersize=2, markeredgecolor='blue', markerfacecolor='none')
ax[1].plot(t65_K0_1[::20]/62511.75, kurtosis_65_K0_1[::20], label="\\boldmath$K_{trap}=0.1$", color='green', marker='o', linestyle='-', markersize=2, markeredgecolor='green', markerfacecolor='none')
ax[1].plot(t65_K0_5/62511.75, kurtosis_65_K0_5, label="\\boldmath$K_{trap}=0.5$", color='red', linestyle='-')

ax[1].set_xscale('log')
ax[1].set_xticks([1e-5, 1e-4, 1e-3, 1e-2, 1e-1,1e0])
ax[1].set_xticklabels(['\\boldmath$10^{-5}$', '\\boldmath$10^{-4}$', '\\boldmath$10^{-3}$', '\\boldmath$10^{-2}$', '\\boldmath$10^{-1}$','\\boldmath$10^{0}$'], fontsize=10)
ax[1].set_yticks([-0.50, -0.45, -0.40, -0.35, -0.30, -0.25])
ax[1].set_yticklabels(['\\boldmath$-0.50$', '\\boldmath$-0.45$', '\\boldmath$-0.40$', '\\boldmath$-0.35$', '\\boldmath$-0.30$', '\\boldmath$-0.25$'], fontsize=10)
ax[1].set_xlabel('\\boldmath$\Delta t/\\tau$', fontsize=12)
ax[1].legend(loc='best', fontsize=13)
ax[1].set_xlim(2*10**-5, 10**0)


for a in ax:
	a.tick_params(which='minor', length=4, width=1, colors='black', direction='in', labelsize=0, top=True, right=True)
	a.tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=10, top=True, right=True)
	#a.set_xlim(1, 10**4)
	for spine in a.spines.values():
		spine.set_linewidth(2)  # Adjust this value to change the thickness of the border
	# Save the plot
ax[0].set_title(r'\boldmath$(a)$', fontsize=15, verticalalignment='top')
ax[1].set_title(r'\boldmath$(b)$', fontsize=15, verticalalignment='top')

plt.tight_layout()
plt.savefig('vary_kurtosis.pdf', bbox_inches='tight')


