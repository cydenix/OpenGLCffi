from OpenGLCffi.GLES2 import params
@params('target', 'levels', 'internalformat', 'width', api='gles2')
def glTexStorage1DEXT(target, levels, internalformat, width):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', api='gles2')
def glTexStorage2DEXT(target, levels, internalformat, width, height):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', 'depth', api='gles2')
def glTexStorage3DEXT(target, levels, internalformat, width, height, depth):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', api='gles2')
def glTextureStorage1DEXT(texture, target, levels, internalformat, width):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', 'height', api='gles2')
def glTextureStorage2DEXT(texture, target, levels, internalformat, width, height):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', 'height', 'depth', api='gles2')
def glTextureStorage3DEXT(texture, target, levels, internalformat, width, height, depth):
	pass


