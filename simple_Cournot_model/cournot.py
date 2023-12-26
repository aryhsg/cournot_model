from sympy import *
import numpy as np
from matplotlib import pyplot as plt

class Cournot:
    def __init__(self, firm: list, p_intercept, p_slope):
        self.firm = firm
        self.p_intercept = p_intercept
        self.p_slope = p_slope
        self.P_inverse = self.p_intercept + self.p_slope * (self.firm[0].q + self.firm[1].q)
        self.pf = []
        self.reaction_list = []

    def profit(self):
        for i in range(len(self.firm)):
            pi = self.P_inverse * self.firm[i].q - self.firm[i].cost()
            self.pf.append(pi)
        return self.pf

    def reaction_func(self):
        for i in range(len(self.firm)):
            foc = diff(self.pf[i], self.firm[i].q)
            self.reaction_list.append(foc)
        return self.reaction_list

    def equilibrium(self):
        solution = solve((self.reaction_list[0], self.reaction_list[1]), (self.firm[0].q, self.firm[1].q))
        return solution

    def figure(self):
        q1_vals = np.linspace(0, 5000, 100)
        q2_vals = np.linspace(0, 5000, 100)

        Q1, Q2 = np.meshgrid(q1_vals, q2_vals)

        # Evaluate the first equation in self.foc_list
        FOC1 = lambdify((self.firm[0].q, self.firm[1].q), self.reaction_list[0], 'numpy')
        Z1 = FOC1(Q1, Q2)

        # Evaluate the second equation in self.foc_list
        FOC2 = lambdify((self.firm[0].q, self.firm[1].q), self.reaction_list[1], 'numpy')
        Z2 = FOC2(Q1, Q2)

        # Plot contours for the two equations
        plt.contour(Q1, Q2, Z1, levels=[0], colors='r', label='reaction1')
        plt.contour(Q1, Q2, Z2, levels=[0], colors='b', label='reaction2')

        plt.xlabel('Firm 1 Quantity')
        plt.ylabel('Firm 2 Quantity')
        plt.legend(title=("reaction1", "reaction2"))
        plt.show()