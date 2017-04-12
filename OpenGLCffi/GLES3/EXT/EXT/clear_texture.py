from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['texture', 'level', 'format', 'type', 'data'])
def glClearTexImageEXT(texture, level, format, type, data):
	pass


@params(api='gles3', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'data'])
def glClearTexSubImageEXT(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
	pass


