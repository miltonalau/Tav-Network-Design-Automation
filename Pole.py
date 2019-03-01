
class Pole(object):
    lat = float(0)
    lon = float(0)

    def __init__(self, tag, lat, lon):
        self.id = tag
        self.lat = lat
        self.lon = lon

def make_pole(tag, lat, lon):
    pole = Pole(tag, lat, lon)
    return pole