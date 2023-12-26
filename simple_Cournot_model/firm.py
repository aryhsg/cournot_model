from sympy import *

class Firm:
    def __init__(self, q: str, cost_func: str):
        self.q = symbols(q)
        self.cost_func = cost_func

    def cost(self):
        cost_function = sympify(self.cost_func)
        return cost_function