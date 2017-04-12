from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data'])
def glCompressedTexImage3DARB(target, level, internalformat, width, height, depth, border, imageSize, data):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data'])
def glCompressedTexImage2DARB(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'data'])
def glCompressedTexImage1DARB(target, level, internalformat, width, border, imageSize, data):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage3DARB(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage2DARB(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage1DARB(target, level, xoffset, width, format, imageSize, data):
	pass


@params(api='gl', prms=['target', 'level', 'img'])
def glGetCompressedTexImageARB(target, level, img):
	pass


