from pyproj import Transformer

def prevod_souradnic(x,y):
    wgs2jtsk = Transformer.from_crs(4326,5514, always_xy=True)
    souradnice = wgs2jtsk.transform(x,y)
    return souradnice