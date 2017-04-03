from OpenGLCffi.GL import params
@params('type', 'pointer', api='gl')
def glElementPointerATI(type, pointer):
	pass


@params('mode', 'count', api='gl')
def glDrawElementArrayATI(mode, count):
	pass


@params('mode', 'start', 'end', 'count', api='gl')
def glDrawRangeElementArrayATI(mode, start, end, count):
	pass


