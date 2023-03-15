import sys
import feelpp
import numpy as np
print(f"feelpp loaded from {feelpp.__file__}")
sys.argv = ['feelpp1']
e = feelpp.Environment(sys.argv,config=feelpp.localRepository("feelpp1"))
y = feelpp.expr("sin(2*pi*x):x")
y.setParameterValues({"x":2.0})

import numpy as np
x = np.linspace(-1,1,100) 
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y.evaluate("x",x), mode='lines', name='$y$'), )
fig.update_xaxes(title_text=r"x")
fig.update_yaxes(title_text=r"y")
fig.show()
from feelpp.integrate import integrate
geo = {
        '2': feelpp.create_rectangle(),
        '3': feelpp.create_box(),
    }
mesh_name = geo['2'][0]
print(mesh_name)
mesh = feelpp.load(feelpp.mesh(dim=2), geo['2'][0], 0.1)
meas = integrate(range=feelpp.elements(mesh),expr="1")
print(f"measure is : {meas}")
assert np.abs(meas[0]-2.0) < 1e-10