@params('type', 'pointer', api='gl')
def glElementPointerAPPLE(type, pointer):
	pass


@params('mode', 'first', 'count', api='gl')
def glDrawElementArrayAPPLE(mode, first, count):
	pass


@params('mode', 'start', 'end', 'first', 'count', api='gl')
def glDrawRangeElementArrayAPPLE(mode, start, end, first, count):
	pass


@params('mode', 'first', 'count', 'primcount', api='gl')
def glMultiDrawElementArrayAPPLE(mode, first, count, primcount):
	pass


@params('mode', 'start', 'end', 'first', 'count', 'primcount', api='gl')
def glMultiDrawRangeElementArrayAPPLE(mode, start, end, first, count, primcount):
	pass


