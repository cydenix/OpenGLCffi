from OpenGLCffi.GL import params
@params(api='gl', prms=['category', 'severity', 'count', 'ids', 'enabled'])
def glDebugMessageEnableAMD(category, severity, count, ids, enabled):
	pass


@params(api='gl', prms=['category', 'severity', 'id', 'length', 'buf'])
def glDebugMessageInsertAMD(category, severity, id, length, buf):
	pass


@params(api='gl', prms=['callback', 'userParam'])
def glDebugMessageCallbackAMD(callback, userParam):
	pass


@params(api='gl', prms=['count', 'bufsize', 'categories', 'severities', 'ids', 'lengths', 'message'])
def glGetDebugMessageLogAMD(count, bufsize, categories, severities, ids, lengths, message):
	pass


