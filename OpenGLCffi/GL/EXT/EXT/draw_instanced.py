from OpenGLCffi.GL import params
@params('mode', 'start', 'count', 'primcount', api='gl')
def glDrawArraysInstancedEXT(mode, start, count, primcount):
	pass


@params('mode', 'count', 'type', 'indices', 'primcount', api='gl')
def glDrawElementsInstancedEXT(mode, count, type, indices, primcount):
	pass


