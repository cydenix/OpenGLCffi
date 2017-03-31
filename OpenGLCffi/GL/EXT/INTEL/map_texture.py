@params('texture', api='gl')
def glSyncTextureINTEL(texture):
	pass


@params('texture', 'level', api='gl')
def glUnmapTexture2DINTEL(texture, level):
	pass


@params('texture', 'level', 'access', 'stride', 'layout', api='gl')
def glMapTexture2DINTEL(texture, level, access, stride, layout):
	pass


