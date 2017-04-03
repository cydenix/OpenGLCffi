from OpenGLCffi.GL import params
@params('target', 'first', 'count', 'buffers', api='gl')
def glBindBuffersBase(target, first, count, buffers):
	pass


@params('target', 'first', 'count', 'buffers', 'offsets', 'sizes', api='gl')
def glBindBuffersRange(target, first, count, buffers, offsets, sizes):
	pass


@params('first', 'count', 'textures', api='gl')
def glBindTextures(first, count, textures):
	pass


@params('first', 'count', 'samplers', api='gl')
def glBindSamplers(first, count, samplers):
	pass


@params('first', 'count', 'textures', api='gl')
def glBindImageTextures(first, count, textures):
	pass


@params('first', 'count', 'buffers', 'offsets', 'strides', api='gl')
def glBindVertexBuffers(first, count, buffers, offsets, strides):
	pass


