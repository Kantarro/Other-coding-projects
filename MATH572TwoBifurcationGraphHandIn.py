import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap

# System of ODEs
def system(y, z, A, B):
    dydt = A*(1 - y - z)*y - y - B*y*z # = f(x,y)
    dzdt = B*y*z - z # = g(x,y)
    return np.array([dydt, dzdt])

# Constructing the Jacobian matrix, solved by hand previously
def jacobian(y, z, A, B):
    df_dy = A*(1 - 2*y - z) - 1 - B*z
    df_dz = -A*y - B*y
    dg_dy = B*z
    dg_dz = B*y - 1
    return np.array([[df_dy, df_dz], [dg_dy, dg_dz]])

# setting up the equilibrium points
def equilibria(A, B):
    p1 = (0, 0) #(0, 0)
    p2 = (1/B, (A*B - A - B)/(B*(A + B)))
    p3 = ((A - 1)/A, 0)
    return p1, p2, p3

#A & B values and steps
A_vals = np.linspace(0.001, 5, 100)
B_vals = np.linspace(0.001, 5, 100)
stability_map = np.zeros((len(A_vals), len(B_vals)))

#Iterate over "all" parameter combinations
for i, A in enumerate(A_vals):
    for j, B in enumerate(B_vals):
        p1, p2, p3 = equilibria(A, B)

        # Checking stability of the three equilibirum values
        stability = 0 # initially set to be unstable

        # Stability testing at (0, 0)
        y_eq, z_eq = p1
        Jacobian1 = jacobian(y_eq, z_eq, A, B)
        eigenvalues1 = np.linalg.eigvals(Jacobian1)
        Re_parts1 = np.real(eigenvalues1)
        Im_parts1 = np.imag(eigenvalues1)

        if np.all(Re_parts1 < 0) and np.isreal(eigenvalues1).all(): # no imaginary parts with all negative real parts
            stability = 1 # Stable node
        elif np.all(Re_parts1 < 0) and np.any(Im_parts1 != 0): # exist imaginary parts with all negative real parts
            stability = 2 # Stable spiral

        # Stability testing at ((A-1)/A, 0)
        y_eq, z_eq = p3
        Jacobian2 = jacobian(y_eq, z_eq, A, B)
        eigenvalues2 = np.linalg.eigvals(Jacobian2)
        Re_parts2 = np.real(eigenvalues2)
        Im_parts2 = np.imag(eigenvalues2)

        if np.all(Re_parts2 < 0) and np.isreal(eigenvalues2).all():
            stability = 3 # Stable node
        elif np.all(Re_parts2 < 0) and np.any(Im_parts2 != 0):
            stability = 4 # Stable spiral

        # Stability testing at (1/B, (AB-A-B)/(B(A+B)))
        y_eq, z_eq = p2
        Jacobian3 = jacobian(y_eq, z_eq, A, B)
        eigenvalues3 = np.linalg.eigvals(Jacobian3)
        Re_parts3 = np.real(eigenvalues3)
        Im_parts3 = np.imag(eigenvalues3)

        if np.all(Re_parts3 < 0) and np.isreal(eigenvalues3).all():
            stability = 5 # Stable node
        elif np.all(Re_parts3 < 0) and np.any(Im_parts3 != 0):
            stability = 6 # Stable spiral

        # Stability map updated based on stability of equilibrium
        stability_map[i, j] = stability

#Colourmap
color_map = ListedColormap(['red', 'pink', 'lightgreen', 'cyan', 'lightblue', 'orange', 'brown'])

#Plotting the stability map
plt.figure(figsize=(8, 6))
plt.imshow(stability_map.T, extent=[A_vals[0], A_vals[-1], B_vals[0], B_vals[-1]],
           origin='lower', cmap=color_map, interpolation='nearest', vmin=0, vmax=6)

A_line = np.linspace(0.001, 5, 100)
B_line1 = A_line / (2 * (np.sqrt(A_line) - 1)) # B = A / (2(sqrt(A) - 1))
B_line2 = A_line / (A_line - 1) # B = A / (A - 1)
B_line1 = np.clip(B_line1, 0.001, 5)
B_line2 = np.clip(B_line2, 0.001, 5)
plt.plot(A_line, B_line1, 'k--', label=r'$B = \frac{A}{2(\sqrt{A} - 1)}$')
plt.plot(A_line, B_line2, 'k--', label=r'$B = \frac{A}{A - 1}$')

#legend
red_patch = mpatches.Patch(color='red',
                             label=r": If no equilibrium points are stable")
lightgreen_patch = mpatches.Patch(color='lightgreen',
                                  label=r": If $(0,0)$ is a stable spiral")
orange_patch = mpatches.Patch(color='orange',
                              label=r": If $\left(\frac{1}{B}, "r"\frac{AB - A - B}{B(A + B)}\right)$ is a stable node")
brown_patch = mpatches.Patch(color='brown',
                              label=r": If $\left(\frac{1}{B},"r"\frac{AB - A - B}{B(A + B)}\right)$ is a stable spiral")
cyan_patch = mpatches.Patch(color='cyan',
                            label=r": If $\left(\frac{A - 1}{A},"r"0\right)$ is a stable node")
lightblue_patch = mpatches.Patch(color='lightblue',
                                 label=r": If $\left(\frac{A - 1}{A}, 0\right)$ is a stable spiral")
pink_patch = mpatches.Patch(color='pink',
                           label=": If $(0,0)$ is a stable node")
plt.legend(handles=[pink_patch, lightgreen_patch, orange_patch, brown_patch, cyan_patch, lightblue_patch, red_patch],
           loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel("A")
plt.ylabel("B")
plt.title("Two-Bifurcation Diagram Constructed Numerically")
plt.grid(True)

plt.show()
