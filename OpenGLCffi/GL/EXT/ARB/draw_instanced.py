from OpenGLCffi.GL import params
@params('mode', 'first', 'count', 'primcount', api='gl')
def glDrawArraysInstancedARB(mode, first, count, primcount):
	pass


@params('mode', 'count', 'type', 'indices', 'primcount', api='gl')
def glDrawElementsInstancedARB(mode, count, type, indices, primcount):
	pass


