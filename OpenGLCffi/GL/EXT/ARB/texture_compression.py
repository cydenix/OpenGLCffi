@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data', api='gl')
def glCompressedTexImage3DARB(target, level, internalformat, width, height, depth, border, imageSize, data):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data', api='gl')
def glCompressedTexImage2DARB(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params('target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'data', api='gl')
def glCompressedTexImage1DARB(target, level, internalformat, width, border, imageSize, data):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data', api='gl')
def glCompressedTexSubImage3DARB(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data', api='gl')
def glCompressedTexSubImage2DARB(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params('target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data', api='gl')
def glCompressedTexSubImage1DARB(target, level, xoffset, width, format, imageSize, data):
	pass


@params('target', 'level', 'img', api='gl')
def glGetCompressedTexImageARB(target, level, img):
	pass


