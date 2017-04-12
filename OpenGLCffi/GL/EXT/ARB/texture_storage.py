from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'levels', 'internalformat', 'width'])
def glTexStorage1D(target, levels, internalformat, width):
	pass


@params(api='gl', prms=['target', 'levels', 'internalformat', 'width', 'height'])
def glTexStorage2D(target, levels, internalformat, width, height):
	pass


@params(api='gl', prms=['target', 'levels', 'internalformat', 'width', 'height', 'depth'])
def glTexStorage3D(target, levels, internalformat, width, height, depth):
	pass


