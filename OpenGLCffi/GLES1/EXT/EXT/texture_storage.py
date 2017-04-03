from OpenGLCffi.GLES1 import params
@params('target', 'levels', 'internalformat', 'width', api='gles1')
def glTexStorage1DEXT(target, levels, internalformat, width):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', api='gles1')
def glTexStorage2DEXT(target, levels, internalformat, width, height):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', 'depth', api='gles1')
def glTexStorage3DEXT(target, levels, internalformat, width, height, depth):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', api='gles1')
def glTextureStorage1DEXT(texture, target, levels, internalformat, width):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', 'height', api='gles1')
def glTextureStorage2DEXT(texture, target, levels, internalformat, width, height):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', 'height', 'depth', api='gles1')
def glTextureStorage3DEXT(texture, target, levels, internalformat, width, height, depth):
	pass


