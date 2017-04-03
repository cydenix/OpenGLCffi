from OpenGLCffi.GLES3 import params
@params('texture', 'level', 'format', 'type', 'data', api='gles3')
def glClearTexImageEXT(texture, level, format, type, data):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'data', api='gles3')
def glClearTexSubImageEXT(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
	pass


