from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'size4d', 'border', 'format', 'type', 'pixels'])
def glTexImage4DSGIS(target, level, internalformat, width, height, depth, size4d, border, format, type, pixels):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'woffset', 'width', 'height', 'depth', 'size4d', 'format', 'type', 'pixels'])
def glTexSubImage4DSGIS(target, level, xoffset, yoffset, zoffset, woffset, width, height, depth, size4d, format, type, pixels):
	pass


