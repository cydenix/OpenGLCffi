from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['mode', 'first', 'count', 'primcount'])
def glDrawArraysInstancedNV(mode, first, count, primcount):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'primcount'])
def glDrawElementsInstancedNV(mode, count, type, indices, primcount):
	pass


