@params('category', 'severity', 'count', 'ids', 'enabled', api='gl')
def glDebugMessageEnableAMD(category, severity, count, ids, enabled):
	pass


@params('category', 'severity', 'id', 'length', 'buf', api='gl')
def glDebugMessageInsertAMD(category, severity, id, length, buf):
	pass


@params('callback', 'userParam', api='gl')
def glDebugMessageCallbackAMD(callback, userParam):
	pass


@params('count', 'bufsize', 'categories', 'severities', 'ids', 'lengths', 'message', api='gl')
def glGetDebugMessageLogAMD(count, bufsize, categories, severities, ids, lengths, message):
	pass


