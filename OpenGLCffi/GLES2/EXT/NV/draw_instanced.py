from OpenGLCffi.GLES2 import params
@params('mode', 'first', 'count', 'primcount', api='gles2')
def glDrawArraysInstancedNV(mode, first, count, primcount):
	pass


@params('mode', 'count', 'type', 'indices', 'primcount', api='gles2')
def glDrawElementsInstancedNV(mode, count, type, indices, primcount):
	pass


