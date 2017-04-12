from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['mode', 'start', 'count', 'primcount'])
def glDrawArraysInstancedEXT(mode, start, count, primcount):
	pass


@params(api='gles2', prms=['mode', 'count', 'type', 'indices', 'primcount'])
def glDrawElementsInstancedEXT(mode, count, type, indices, primcount):
	pass


