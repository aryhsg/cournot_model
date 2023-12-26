from sympy import *
import numpy as np
from matplotlib import pyplot as plt

class Cournot:
    def __init__(self, firm: list, mkt_demand_func: str):
        self.firm = firm
        self.mkt_demand_func = sympify(mkt_demand_func)
        self.pf = []
        self.reaction_list = []
        self.profit_list_generated = False
        self.reaction_list_generated = False
        self.result = {}

    def profit(self):
        if self.profit_list_generated == False:
            for i in range(len(self.firm)):
                pi = self.mkt_demand_func * self.firm[i].q - self.firm[i].cost()
                self.pf.append(pi)
            self.profit_list_generated = True

        return self.pf

    def reaction_func(self):
        if self.reaction_list_generated == False:
            for i in range(len(self.firm)):
                foc = diff(self.pf[i], self.firm[i].q)
                self.reaction_list.append(foc)
            self.reaction_list_generated = True

        return self.reaction_list


    def equilibrium(self):
        self.result = solve((self.reaction_list[0], self.reaction_list[1]), (self.firm[0].q, self.firm[1].q))
        return self.result

    def figure(self):
        upper_bound1  = float(self.result[self.firm[0].q]) + 500
        lower_bound1 = float(self.result[self.firm[0].q]) - 500
        upper_bound2  = float(self.result[self.firm[1].q]) + 500
        lower_bound2 = float(self.result[self.firm[1].q]) - 500

        q1_vals = np.linspace(lower_bound1 , upper_bound1, 100)
        q2_vals = np.linspace(lower_bound2, upper_bound2, 100)

        Q1, Q2 = np.meshgrid(q1_vals, q2_vals)

        # Evaluate the first equation in self.foc_list
        FOC1 = lambdify((self.firm[0].q, self.firm[1].q), self.reaction_list[0], 'numpy')
        Z1 = FOC1(Q1, Q2)

        # Evaluate the second equation in self.foc_list
        FOC2 = lambdify((self.firm[0].q, self.firm[1].q), self.reaction_list[1], 'numpy')
        Z2 = FOC2(Q1, Q2)

        # Plot contours for the two equations
        plt.contour(Q1, Q2, Z1, levels=[0], colors='r')
        plt.contour(Q1, Q2, Z2, levels=[0], colors='b')

        plt.xlabel('Firm 1 Quantity')
        plt.ylabel('Firm 2 Quantity')

        plt.show()