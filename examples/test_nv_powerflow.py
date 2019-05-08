import math
import sys

sys.path.append(r"C:\Users\Martin\Desktop\git\state-estimation\acs\state_estimation")
sys.path.append(r"C:\Users\Martin\Desktop\git\state-estimation\examples")


from network import *
import py_95bus_network_data
from nv_powerflow import *

class PerUnit:
    def __init__(self, S, V):
        self.S = S
        self.V = V
        self.I = S/V
        self.Z = S/(V**2)
		
		
""" Insert here per unit values of the grid for power and voltage """
S = 100*(10**6)
V = (11*(10**3))/math.sqrt(3)
slackV = 1.02

Base = PerUnit(S,V)
branch, node = py_95bus_network_data.Network_95_nodes(Base, slackV)
V, I, Iinj, S1, S2, Sinj, num_iter = solve(branch, node)

print("S1:")
print(S1)
print("\n\n")

print("Sinj:")
print(Sinj)
print("\n\n")

print("num_iter:" + str(num_iter))
print("\n\n")


