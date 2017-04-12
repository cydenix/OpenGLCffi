from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels'])
def glTexImage3DEXT(target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels'])
def glTexSubImage3DEXT(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


