from OpenGLCffi.GL import params
@params(api='gl', prms=['type', 'pointer'])
def glElementPointerATI(type, pointer):
	pass


@params(api='gl', prms=['mode', 'count'])
def glDrawElementArrayATI(mode, count):
	pass


@params(api='gl', prms=['mode', 'start', 'end', 'count'])
def glDrawRangeElementArrayATI(mode, start, end, count):
	pass


