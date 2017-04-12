from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['texture', 'level', 'format', 'type', 'data'])
def glClearTexImageEXT(texture, level, format, type, data):
	pass


@params(api='gles2', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'data'])
def glClearTexSubImageEXT(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
	pass


