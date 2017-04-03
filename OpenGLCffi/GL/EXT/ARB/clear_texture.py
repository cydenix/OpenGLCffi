from OpenGLCffi.GL import params
@params('texture', 'level', 'format', 'type', 'data', api='gl')
def glClearTexImage(texture, level, format, type, data):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'data', api='gl')
def glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
	pass


