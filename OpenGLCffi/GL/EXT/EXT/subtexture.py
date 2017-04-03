from OpenGLCffi.GL import params
@params('target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels', api='gl')
def glTexSubImage1DEXT(target, level, xoffset, width, format, type, pixels):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gl')
def glTexSubImage2DEXT(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


