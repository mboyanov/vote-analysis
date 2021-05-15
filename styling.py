from matplotlib import cm
cols = [i for i in range(1,31)]
pc = {
    4: cm.get_cmap('Reds'),
    9: cm.get_cmap('Purples'),
    28: cm.get_cmap('Blues'),
    29: cm.get_cmap('BuPu'),
    18: cm.get_cmap('Greens'),
    11: cm.get_cmap('Blues')
}
def to_hex(rgba):
    def pad(x):
        if len(x) == 1:
            return "0"+x
        return x
    return "".join([pad(hex(x)[2:]) for x in rgba[:3]])

def party_colors(v):
    bgdf = v.copy()
    bgdf[cols] = 'background-color: white'
    for p, colormap in pc.items():
        bgdf[p] =  [f'background-color: #{to_hex(c)}' for c in colormap(v[p], bytes=True)]
    return bgdf

