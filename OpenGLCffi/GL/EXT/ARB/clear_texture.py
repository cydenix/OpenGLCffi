from OpenGLCffi.GL import params
@params(api='gl', prms=['texture', 'level', 'format', 'type', 'data'])
def glClearTexImage(texture, level, format, type, data):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'data'])
def glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
	pass


