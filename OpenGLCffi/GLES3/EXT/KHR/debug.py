from OpenGLCffi.GLES3 import params
@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gles3')
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gles3')
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params('callback', 'userParam', api='gles3')
def glDebugMessageCallback(callback, userParam):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gles3')
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('source', 'id', 'length', 'message', api='gles3')
def glPushDebugGroup(source, id, length, message):
	pass


@params(api = 'gles3')
def glPopDebugGroup():
	pass


@params('identifier', 'name', 'length', 'label', api='gles3')
def glObjectLabel(identifier, name, length, label):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label', api='gles3')
def glGetObjectLabel(identifier, name, bufSize, length):
	pass


@params('ptr', 'length', 'label', api='gles3')
def glObjectPtrLabel(ptr, length, label):
	pass


@params('ptr', 'bufSize', 'length', 'label', api='gles3')
def glGetObjectPtrLabel(ptr, bufSize, length):
	pass


@params('pname', 'params', api='gles3')
def glGetPointerv(pname):
	pass


@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gles3')
def glDebugMessageControlKHR(source, type, severity, count, ids, enabled):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gles3')
def glDebugMessageInsertKHR(source, type, id, severity, length, buf):
	pass


@params('callback', 'userParam', api='gles3')
def glDebugMessageCallbackKHR(callback, userParam):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gles3')
def glGetDebugMessageLogKHR(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('source', 'id', 'length', 'message', api='gles3')
def glPushDebugGroupKHR(source, id, length, message):
	pass


@params(api = 'gles3')
def glPopDebugGroupKHR():
	pass


@params('identifier', 'name', 'length', 'label', api='gles3')
def glObjectLabelKHR(identifier, name, length, label):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label', api='gles3')
def glGetObjectLabelKHR(identifier, name, bufSize, length):
	pass


@params('ptr', 'length', 'label', api='gles3')
def glObjectPtrLabelKHR(ptr, length, label):
	pass


@params('ptr', 'bufSize', 'length', 'label', api='gles3')
def glGetObjectPtrLabelKHR(ptr, bufSize, length):
	pass


@params('pname', 'params', api='gles3')
def glGetPointervKHR(pname):
	pass


