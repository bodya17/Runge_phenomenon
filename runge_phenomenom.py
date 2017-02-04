
# coding: utf-8

# In[7]:

import plotly
from plotly.graph_objs import Scatter, Layout
import sympy
import numpy as np


# In[9]:

x = sympy.Symbol('x')


# In[16]:

plotly.offline.init_notebook_mode()


# In[28]:

f = 1 / (1 + 25*x**2)


# In[38]:

def plot(funs, from_to, name='Графік'):
    graphs = []
    for f in funs:
        fun = np.vectorize(sympy.lambdify(x, f))
        start = from_to[1]
        end  = from_to[2]
        x_vals = np.linspace(start, end, 1000)
        y_vals = fun(x_vals)
        graphs.append(Scatter(x=x_vals, y=y_vals))
    plotly.offline.iplot(graphs)


# In[39]:

def inter_runga(n):
    points = [2 * i / n - 1 for i in range(n+1)]
    runge = np.vectorize(sympy.lambdify(x, f))
    inter = sympy.polys.polyfuncs.interpolate(list(zip(points, runge(points))), x)
    plot([f, inter], (x, -1, 1))


# In[41]:

inter_runga(10)


# In[ ]:



