@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gles2')
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gles2')
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params('callback', 'userParam', api='gles2')
def glDebugMessageCallback(callback, userParam):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gles2')
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('source', 'id', 'length', 'message', api='gles2')
def glPushDebugGroup(source, id, length, message):
	pass


@params(api = 'gles2')
def glPopDebugGroup():
	pass


@params('identifier', 'name', 'length', 'label', api='gles2')
def glObjectLabel(identifier, name, length, label):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label', api='gles2')
def glGetObjectLabel(identifier, name, bufSize, length, label):
	pass


@params('ptr', 'length', 'label', api='gles2')
def glObjectPtrLabel(ptr, length, label):
	pass


@params('ptr', 'bufSize', 'length', 'label', api='gles2')
def glGetObjectPtrLabel(ptr, bufSize, length, label):
	pass


@params('pname', 'params', api='gles2')
def glGetPointerv(pname):
	pass


@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gles2')
def glDebugMessageControlKHR(source, type, severity, count, ids, enabled):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gles2')
def glDebugMessageInsertKHR(source, type, id, severity, length, buf):
	pass


@params('callback', 'userParam', api='gles2')
def glDebugMessageCallbackKHR(callback, userParam):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gles2')
def glGetDebugMessageLogKHR(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('source', 'id', 'length', 'message', api='gles2')
def glPushDebugGroupKHR(source, id, length, message):
	pass


@params(api = 'gles2')
def glPopDebugGroupKHR():
	pass


@params('identifier', 'name', 'length', 'label', api='gles2')
def glObjectLabelKHR(identifier, name, length, label):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label', api='gles2')
def glGetObjectLabelKHR(identifier, name, bufSize, length, label):
	pass


@params('ptr', 'length', 'label', api='gles2')
def glObjectPtrLabelKHR(ptr, length, label):
	pass


@params('ptr', 'bufSize', 'length', 'label', api='gles2')
def glGetObjectPtrLabelKHR(ptr, bufSize, length, label):
	pass


@params('pname', 'params', api='gles2')
def glGetPointervKHR(pname):
	pass


