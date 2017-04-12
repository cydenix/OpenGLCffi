from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels'])
def glTexImage3DOES(target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels'])
def glTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params(api='gles3', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data'])
def glCompressedTexImage3DOES(target, level, internalformat, width, height, depth, border, imageSize, data):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params(api='gles3', prms=['target', 'attachment', 'textarget', 'texture', 'level', 'zoffset'])
def glFramebufferTexture3DOES(target, attachment, textarget, texture, level, zoffset):
	pass


