@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gl')
def glDebugMessageControlARB(source, type, severity, count, ids, enabled):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gl')
def glDebugMessageInsertARB(source, type, id, severity, length, buf):
	pass


@params('callback', 'userParam', api='gl')
def glDebugMessageCallbackARB(callback, userParam):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gl')
def glGetDebugMessageLogARB(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


