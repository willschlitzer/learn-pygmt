import pygmt

fig=pygmt.Figure()
fig.coast(region=[-69, -68, 43.75, 44.75], shorelines=True)
fig.show(method="external")
