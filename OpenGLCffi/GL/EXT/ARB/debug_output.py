from OpenGLCffi.GL import params
@params(api='gl', prms=['source', 'type', 'severity', 'count', 'ids', 'enabled'])
def glDebugMessageControlARB(source, type, severity, count, ids, enabled):
	pass


@params(api='gl', prms=['source', 'type', 'id', 'severity', 'length', 'buf'])
def glDebugMessageInsertARB(source, type, id, severity, length, buf):
	pass


@params(api='gl', prms=['callback', 'userParam'])
def glDebugMessageCallbackARB(callback, userParam):
	pass


@params(api='gl', prms=['count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog'])
def glGetDebugMessageLogARB(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


