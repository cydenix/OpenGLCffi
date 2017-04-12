from OpenGLCffi.GL import params
@params(api='gl', prms=['texture'])
def glSyncTextureINTEL(texture):
	pass


@params(api='gl', prms=['texture', 'level'])
def glUnmapTexture2DINTEL(texture, level):
	pass


@params(api='gl', prms=['texture', 'level', 'access', 'stride', 'layout'])
def glMapTexture2DINTEL(texture, level, access, stride, layout):
	pass


