from OpenGLCffi.GL import params
@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gl')
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gl')
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params('callback', 'userParam', api='gl')
def glDebugMessageCallback(callback, userParam):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gl')
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('source', 'id', 'length', 'message', api='gl')
def glPushDebugGroup(source, id, length, message):
	pass


@params(api = 'gl')
def glPopDebugGroup():
	pass


@params('identifier', 'name', 'length', 'label', api='gl')
def glObjectLabel(identifier, name, length, label):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label', api='gl')
def glGetObjectLabel(identifier, name, bufSize, length, label):
	pass


@params('ptr', 'length', 'label', api='gl')
def glObjectPtrLabel(ptr, length, label):
	pass


@params('ptr', 'bufSize', 'length', 'label', api='gl')
def glGetObjectPtrLabel(ptr, bufSize, length, label):
	pass


@params('pname', 'params', api='gl')
def glGetPointerv(pname, params):
	pass


@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gl')
def glDebugMessageControlKHR(source, type, severity, count, ids, enabled):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gl')
def glDebugMessageInsertKHR(source, type, id, severity, length, buf):
	pass


@params('callback', 'userParam', api='gl')
def glDebugMessageCallbackKHR(callback, userParam):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gl')
def glGetDebugMessageLogKHR(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('source', 'id', 'length', 'message', api='gl')
def glPushDebugGroupKHR(source, id, length, message):
	pass


@params(api = 'gl')
def glPopDebugGroupKHR():
	pass


@params('identifier', 'name', 'length', 'label', api='gl')
def glObjectLabelKHR(identifier, name, length, label):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label', api='gl')
def glGetObjectLabelKHR(identifier, name, bufSize, length, label):
	pass


@params('ptr', 'length', 'label', api='gl')
def glObjectPtrLabelKHR(ptr, length, label):
	pass


@params('ptr', 'bufSize', 'length', 'label', api='gl')
def glGetObjectPtrLabelKHR(ptr, bufSize, length, label):
	pass


@params('pname', 'params', api='gl')
def glGetPointervKHR(pname, params):
	pass


