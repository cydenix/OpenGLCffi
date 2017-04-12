from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['mode', 'start', 'count', 'primcount'])
def glDrawArraysInstancedEXT(mode, start, count, primcount):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'primcount'])
def glDrawElementsInstancedEXT(mode, count, type, indices, primcount):
	pass


