from OpenGLCffi.GL import params
@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'border', api='gl')
def glCopyTexImage1DEXT(target, level, internalformat, x, y, width, border):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border', api='gl')
def glCopyTexImage2DEXT(target, level, internalformat, x, y, width, height, border):
	pass


@params('target', 'level', 'xoffset', 'x', 'y', 'width', api='gl')
def glCopyTexSubImage1DEXT(target, level, xoffset, x, y, width):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTexSubImage2DEXT(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTexSubImage3DEXT(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


