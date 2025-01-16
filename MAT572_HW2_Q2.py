import numpy as np
import matplotlib.pyplot as plt

A_values = np.linspace(0.01, 5, 400)  # A should be positive, start slightly above 0

# Define the boundary functions for B as functions of A
def boundary_B_A_less_1(A):
    return np.nan * A

def boundary_B_grazer_washout(A):
    return A / (A - 1)

def boundary_B_internal(A):
    return A / (2 * (-1 + np.sqrt(A)))

# Initialize the plot
plt.figure(figsize=(10, 8))

# Plotting region 1
plt.fill_between(A_values, 0, np.max(A_values), where=(A_values < 1),
                 color="lightblue", label="bacteria and grazers go to extinction: A < 1")

# Plotting region 2
plt.fill_between(A_values, 0, boundary_B_grazer_washout(A_values), where=(A_values > 1),
                 color="lightgreen", label=r"grazer washout: $A > 1$, $0 < B < \frac{A}{A-1}$")

# Plotting region 3
plt.fill_between(A_values, boundary_B_grazer_washout(A_values), boundary_B_internal(A_values),
                 where=(A_values > 1), color="lightcoral",
                 label=r"internal equilibrium is a stable node: $A > 1$, $\frac{A}{A-1} < B < \frac{A}{2(\sqrt{A}-1)}$")

# Plotting region 4
plt.fill_between(A_values, boundary_B_internal(A_values), np.max(A_values),
                 where=(A_values > 1), color="lightgrey",
                 label=r"internal equilibrium is a stable spiral: $A > 1$, $B > \frac{A}{2(\sqrt{A}-1)}$")

plt.xlabel("A")
plt.ylabel("B")
plt.xlim(0, 5) # A goes from 0 to 5
plt.ylim(0, 5) # B goes from 0 to 5
plt.legend(loc="upper right")
plt.title("Two-Bifurcation Diagram")
plt.grid(True)
plt.show()
