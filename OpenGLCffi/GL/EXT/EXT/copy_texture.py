from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'level', 'internalformat', 'x', 'y', 'width', 'border'])
def glCopyTexImage1DEXT(target, level, internalformat, x, y, width, border):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border'])
def glCopyTexImage2DEXT(target, level, internalformat, x, y, width, height, border):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'x', 'y', 'width'])
def glCopyTexSubImage1DEXT(target, level, xoffset, x, y, width):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage2DEXT(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage3DEXT(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


