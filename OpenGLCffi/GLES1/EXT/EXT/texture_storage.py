from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['target', 'levels', 'internalformat', 'width'])
def glTexStorage1DEXT(target, levels, internalformat, width):
	pass


@params(api='gles1', prms=['target', 'levels', 'internalformat', 'width', 'height'])
def glTexStorage2DEXT(target, levels, internalformat, width, height):
	pass


@params(api='gles1', prms=['target', 'levels', 'internalformat', 'width', 'height', 'depth'])
def glTexStorage3DEXT(target, levels, internalformat, width, height, depth):
	pass


@params(api='gles1', prms=['texture', 'target', 'levels', 'internalformat', 'width'])
def glTextureStorage1DEXT(texture, target, levels, internalformat, width):
	pass


@params(api='gles1', prms=['texture', 'target', 'levels', 'internalformat', 'width', 'height'])
def glTextureStorage2DEXT(texture, target, levels, internalformat, width, height):
	pass


@params(api='gles1', prms=['texture', 'target', 'levels', 'internalformat', 'width', 'height', 'depth'])
def glTextureStorage3DEXT(texture, target, levels, internalformat, width, height, depth):
	pass


