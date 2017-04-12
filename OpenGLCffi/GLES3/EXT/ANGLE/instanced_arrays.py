from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['mode', 'first', 'count', 'primcount'])
def glDrawArraysInstancedANGLE(mode, first, count, primcount):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'primcount'])
def glDrawElementsInstancedANGLE(mode, count, type, indices, primcount):
	pass


@params(api='gles3', prms=['index', 'divisor'])
def glVertexAttribDivisorANGLE(index, divisor):
	pass


