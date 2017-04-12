from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'first', 'count', 'buffers'])
def glBindBuffersBase(target, first, count, buffers):
	pass


@params(api='gl', prms=['target', 'first', 'count', 'buffers', 'offsets', 'sizes'])
def glBindBuffersRange(target, first, count, buffers, offsets, sizes):
	pass


@params(api='gl', prms=['first', 'count', 'textures'])
def glBindTextures(first, count, textures):
	pass


@params(api='gl', prms=['first', 'count', 'samplers'])
def glBindSamplers(first, count, samplers):
	pass


@params(api='gl', prms=['first', 'count', 'textures'])
def glBindImageTextures(first, count, textures):
	pass


@params(api='gl', prms=['first', 'count', 'buffers', 'offsets', 'strides'])
def glBindVertexBuffers(first, count, buffers, offsets, strides):
	pass


