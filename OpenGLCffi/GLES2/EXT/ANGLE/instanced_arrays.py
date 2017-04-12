from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['mode', 'first', 'count', 'primcount'])
def glDrawArraysInstancedANGLE(mode, first, count, primcount):
	pass


@params(api='gles2', prms=['mode', 'count', 'type', 'indices', 'primcount'])
def glDrawElementsInstancedANGLE(mode, count, type, indices, primcount):
	pass


@params(api='gles2', prms=['index', 'divisor'])
def glVertexAttribDivisorANGLE(index, divisor):
	pass


