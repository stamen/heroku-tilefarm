from urllib import urlopen
from StringIO import StringIO

try:
    from PIL import Image
except ImportError:
    import Image

from ModestMaps.Tiles import toMicrosoft

class Proxy:

    def __init__(self, layer):
        self.layer = layer
    
    def renderTile(self, width, height, srs, coord):
        """
        """
        server = str((coord.row + coord.column) % 8)
        quad = toMicrosoft(coord.column, coord.row, coord.zoom)
        url = 'http://ecn.t%(server)s.tiles.virtualearth.net/tiles/a%(quad)s.jpeg?g=586&mkt=en-us&n=z' % locals()
        
        buffer = StringIO(urlopen(url).read())
        image = Image.open(buffer)
        
        return image
