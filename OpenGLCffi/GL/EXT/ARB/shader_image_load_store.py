from OpenGLCffi.GL import params
@params(api='gl', prms=['unit', 'texture', 'level', 'layered', 'layer', 'access', 'format'])
def glBindImageTexture(unit, texture, level, layered, layer, access, format):
	pass


@params(api='gl', prms=['barriers'])
def glMemoryBarrier(barriers):
	pass


