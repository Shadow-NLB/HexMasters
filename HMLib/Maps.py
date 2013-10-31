# This file is basically a utility for me to render maps with

import Hexagon
import pygame.image

resourceRoot = (r'Q:\HexMasters\Resource\Tiles')
grassFlat = pygame.image.load(resourceRoot + r'\GrassHex.png')
dirtTile = pygame.image.load(resourceRoot + r'\DirtHex.png')
waterTile = pygame.image.load(resourceRoot + r'\WaterHex.png')

def makeHexTile(surface, hex) :
	maskSurface = surface.copy()
	maskSurface.fill((0,0,0,255))
	tile = surface.copy()
	pygame.draw.polygon(maskSurface, pygame.Color(255, 0, 0, 0),  hex.points())
	tile.blit(maskSurface, (0,0), None, pygame.BLEND_RGBA_SUB)
	return tile

class MapDefinition(object):
   def __init__(self, height=0, width=0, hex=Hexagon.Hexagon(10)):
      self.map = [[None for x in xrange(0,width)] for y in xrange(0,height)]
      self.height = height
      self.width = width
      self.hex = hex
   def makeHexTile(self, surface) :
      maskSurface = surface.copy()
      maskSurface.fill((0,0,0,255))
      tile = surface.copy()
      pygame.draw.polygon(maskSurface, pygame.Color(255, 0, 0, 0),  self.hex.points())
      tile.blit(maskSurface, (0,0), None, pygame.BLEND_RGBA_SUB)
      return tile
   def renderToSurface(self):
      surface = pygame.Surface((self.width*self.hex.width(), (self.height+.5)*self.hex.tileOffset()[1]))
      i = 0
      for row in self.map:
         yOffset = self.hex.tileOffset()[1] * i
         print 'Printing row'.format(i)
         j = 0
         for tile in row:
            xOffset = j * self.hex.width() + (self.hex.tileOffset()[0] if (i % 2 == 1) else 0)
            print "Print at coordinates: {0}".format((xOffset, yOffset))
            surface.blit(tile, (xOffset, yOffset));
            j = j + 1
         i = i + 1
      return surface
# Use case

# make a new map instance
myMap = MapDefinition(height = 6, width = 5, hex = Hexagon.Hexagon(50))

# import some visual resources
resourceRoot = (r'Q:\HexMasters\Resource\Tiles')
grassImage = pygame.image.load(resourceRoot + r'\GrassHex.png')
dirtImage = pygame.image.load(resourceRoot + r'\DirtHex.png')
waterImage = pygame.image.load(resourceRoot + r'\WaterHex.png')

# Use the map to transform the resources into usable tiles
grassTile = myMap.makeHexTile(grassImage)
dirtTile = myMap.makeHexTile(dirtImage)
waterTile = myMap.makeHexTile(waterImage)

# Now make a bunch of assignments to the map "array" to actually set up the map
myMap.map = [[grassTile for x in xrange(5)] for y in xrange(6)]
myMap.map[0][0] = dirtTile
myMap.map[0][1] = waterTile
myMap.map[0][2] = waterTile
myMap.map[0][3] = waterTile
myMap.map[0][4] = dirtTile
print myMap.map
pygame.image.save(myMap.renderToSurface(), r'C:\temp\renderedMap.BMP')



