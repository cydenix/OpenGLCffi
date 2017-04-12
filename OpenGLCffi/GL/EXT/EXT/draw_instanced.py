from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'start', 'count', 'primcount'])
def glDrawArraysInstancedEXT(mode, start, count, primcount):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'primcount'])
def glDrawElementsInstancedEXT(mode, count, type, indices, primcount):
	pass


