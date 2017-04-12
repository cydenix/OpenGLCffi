from OpenGLCffi.GL import params
@params(api='gl', prms=['index', 'texture', 'level', 'layered', 'layer', 'access', 'format'])
def glBindImageTextureEXT(index, texture, level, layered, layer, access, format):
	pass


@params(api='gl', prms=['barriers'])
def glMemoryBarrierEXT(barriers):
	pass


