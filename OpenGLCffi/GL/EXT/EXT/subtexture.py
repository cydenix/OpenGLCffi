from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels'])
def glTexSubImage1DEXT(target, level, xoffset, width, format, type, pixels):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glTexSubImage2DEXT(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


