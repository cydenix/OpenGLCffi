from OpenGLCffi.GL import params
@params(api='gl', prms=['type', 'pointer'])
def glElementPointerAPPLE(type, pointer):
	pass


@params(api='gl', prms=['mode', 'first', 'count'])
def glDrawElementArrayAPPLE(mode, first, count):
	pass


@params(api='gl', prms=['mode', 'start', 'end', 'first', 'count'])
def glDrawRangeElementArrayAPPLE(mode, start, end, first, count):
	pass


@params(api='gl', prms=['mode', 'first', 'count', 'primcount'])
def glMultiDrawElementArrayAPPLE(mode, first, count, primcount):
	pass


@params(api='gl', prms=['mode', 'start', 'end', 'first', 'count', 'primcount'])
def glMultiDrawRangeElementArrayAPPLE(mode, start, end, first, count, primcount):
	pass


