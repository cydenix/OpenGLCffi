from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'first', 'count', 'primcount'])
def glDrawArraysInstancedARB(mode, first, count, primcount):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'primcount'])
def glDrawElementsInstancedARB(mode, count, type, indices, primcount):
	pass


