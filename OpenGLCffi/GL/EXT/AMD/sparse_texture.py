from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'internalFormat', 'width', 'height', 'depth', 'layers', 'flags'])
def glTexStorageSparseAMD(target, internalFormat, width, height, depth, layers, flags):
	pass


@params(api='gl', prms=['texture', 'target', 'internalFormat', 'width', 'height', 'depth', 'layers', 'flags'])
def glTextureStorageSparseAMD(texture, target, internalFormat, width, height, depth, layers, flags):
	pass


