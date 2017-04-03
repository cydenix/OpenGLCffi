from OpenGLCffi.GL import params
@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'size4d', 'border', 'format', 'type', 'pixels', api='gl')
def glTexImage4DSGIS(target, level, internalformat, width, height, depth, size4d, border, format, type, pixels):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'woffset', 'width', 'height', 'depth', 'size4d', 'format', 'type', 'pixels', api='gl')
def glTexSubImage4DSGIS(target, level, xoffset, yoffset, zoffset, woffset, width, height, depth, size4d, format, type, pixels):
	pass


