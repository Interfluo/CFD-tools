# ==================================================================================================================== #
from math import *                                              # ---------------------------------------------------- #
# ==================================================================================================================== #
# Simulation Quantities ---------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
rho = 1.225                                                     # density [kg/m^3] ----------------------------------- #
Re = 5e5                                                        # Reynolds Number ------------------------------------ #
y_plus = 1                                                      # Desired y+ ----------------------------------------- #
nu = 1e-5                                                       # kinematic viscosity [m^2/s] ------------------------ #
L = 1                                                           # characteristic length [m] -------------------------- #
U_inf = 5                                                       # free-stream velocity [m/s] ------------------------- #
# ==================================================================================================================== #
# Calculated Quantities ---------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
C_f = 0.0576*Re**(-1/5)                                         # skin friction coefficient -------------------------- #
T_w = 1/2*C_f*rho*U_inf**2                                      # local wall shear stress ---------------------------- #
u_T = sqrt(T_w/rho)                                             # friction velocity ---------------------------------- #
y_H = 2*y_plus*nu/u_T                                           # first layer cell height ---------------------------- #
print("==============================================================")  # ------------------------------------------- #
print("Inflation layers calculated based on the following quantities:")  # ------------------------------------------- #
print("--------------------------------------------------------------")  # ------------------------------------------- #
print("density (rho):", rho)                                    # ---------------------------------------------------- #
print("Reynolds number (Re):", Re)                              # ---------------------------------------------------- #
print("y+:", y_plus)                                            # ---------------------------------------------------- #
print("kinematic viscosity (nu):", nu)                          # ---------------------------------------------------- #
print("characteristic length (L):", L)                          # ---------------------------------------------------- #
print("free-stream velocity (U_inf):", U_inf)                   # ---------------------------------------------------- #
print("--------------------------------------------------------------")  # ------------------------------------------- #
print("first layer height (y_H):", y_H)                         # ---------------------------------------------------- #
# calculate total inflation layer height (y_T = delta_99). This is based on empirical results and needs to be modified #
# for the use case at hand, below is an example for a flat plate) ---------------------------------------------------- #
if Re < 5e5:                                                    # ---------------------------------------------------- #
    y_T = 4.91*L/sqrt(Re)                                       # ---------------------------------------------------- #
else:                                                           # ---------------------------------------------------- #
    y_T = 0.38*L/(Re**(1/5))                                    # ---------------------------------------------------- #
# Total number of inflation layers, based on suggestions, only use as a first guess. --------------------------------- #
if y_plus > 20:                                                 # ---------------------------------------------------- #
    N = 10                                                      # ---------------------------------------------------- #
else:                                                           # ---------------------------------------------------- #
    N = 25                                                      # ---------------------------------------------------- #
print("total number of layers (N):", N)                         # ---------------------------------------------------- #
# secant method for finding root of y_H*(1-G^N)/(1-G) - y_T = 0 ------------------------------------------------------ #
x0 = 1.05                                                       # initial guess for x0 (based on lower bound) -------- #
x1 = 1.3                                                        # initial guess for x1 (based on upper bound) -------- #
while abs(x0-x1) > 0.001:                                       # ---------------------------------------------------- #
    fx0 = y_H*(1-x0**N)/(1-x0) - y_T                            # ---------------------------------------------------- #
    fx1 = y_H*(1-x1**N)/(1-x1) - y_T                            # ---------------------------------------------------- #
    x2 = x1 - fx1*(x1-x0)/(fx1-fx0)                             # ---------------------------------------------------- #
    x0 = x1                                                     # ---------------------------------------------------- #
    x1 = x2                                                     # ---------------------------------------------------- #
G = x1                                                          # growth ratio --------------------------------------- #
print("growth ratio (G):", G)                                   # ---------------------------------------------------- #
print("==============================================================")  # ------------------------------------------- #
# ==================================================================================================================== #
