import pygmt

fig = pygmt.Figure()
fig.coast(
    region="IS", projection="M10c", frame=True, land="gray"
)
fig.savefig('figname.pdf')
fig.show(method="external")