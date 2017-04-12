from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['mode', 'first', 'count', 'primcount'])
def glDrawArraysInstancedNV(mode, first, count, primcount):
	pass


@params(api='gles2', prms=['mode', 'count', 'type', 'indices', 'primcount'])
def glDrawElementsInstancedNV(mode, count, type, indices, primcount):
	pass


