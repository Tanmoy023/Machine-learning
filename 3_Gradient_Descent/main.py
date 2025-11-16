import numpy as np


def Gradient_Descent(x, y):
    m_curr = b_curr = 0
    itretion = 10000
    n = len(x)
    learning_rate = 0.08
    for i in range(itretion):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val**2 for val in (y - y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))  # md stand for 'm_derivative'
        bd = -(2 / n) * sum(y - y_predicted)  # bd stand for 'b_derivative'
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print(f"m : {m_curr}, b : {b_curr}, cost : {cost}, itretion : {i}")
    pass


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

Gradient_Descent(x, y)
