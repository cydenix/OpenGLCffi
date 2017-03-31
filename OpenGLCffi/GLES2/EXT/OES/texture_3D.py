@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels', api='gles2')
def glTexImage3DOES(target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels', api='gles2')
def glTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height', api='gles2')
def glCopyTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data', api='gles2')
def glCompressedTexImage3DOES(target, level, internalformat, width, height, depth, border, imageSize, data):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data', api='gles2')
def glCompressedTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', 'zoffset', api='gles2')
def glFramebufferTexture3DOES(target, attachment, textarget, texture, level, zoffset):
	pass


