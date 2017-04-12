from OpenGLCffi.GL import params
@params(api='gl', prms=['source', 'type', 'severity', 'count', 'ids', 'enabled'])
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params(api='gl', prms=['source', 'type', 'id', 'severity', 'length', 'buf'])
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params(api='gl', prms=['callback', 'userParam'])
def glDebugMessageCallback(callback, userParam):
	pass


@params(api='gl', prms=['count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog'])
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params(api='gl', prms=['source', 'id', 'length', 'message'])
def glPushDebugGroup(source, id, length, message):
	pass


@params(api='gl', prms=[])
def glPopDebugGroup():
	pass


@params(api='gl', prms=['identifier', 'name', 'length', 'label'])
def glObjectLabel(identifier, name, length, label):
	pass


@params(api='gl', prms=['identifier', 'name', 'bufSize', 'length', 'label'])
def glGetObjectLabel(identifier, name, bufSize, length, label):
	pass


@params(api='gl', prms=['ptr', 'length', 'label'])
def glObjectPtrLabel(ptr, length, label):
	pass


@params(api='gl', prms=['ptr', 'bufSize', 'length', 'label'])
def glGetObjectPtrLabel(ptr, bufSize, length, label):
	pass


@params(api='gl', prms=['pname', 'params'])
def glGetPointerv(pname, params):
	pass


@params(api='gl', prms=['source', 'type', 'severity', 'count', 'ids', 'enabled'])
def glDebugMessageControlKHR(source, type, severity, count, ids, enabled):
	pass


@params(api='gl', prms=['source', 'type', 'id', 'severity', 'length', 'buf'])
def glDebugMessageInsertKHR(source, type, id, severity, length, buf):
	pass


@params(api='gl', prms=['callback', 'userParam'])
def glDebugMessageCallbackKHR(callback, userParam):
	pass


@params(api='gl', prms=['count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog'])
def glGetDebugMessageLogKHR(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params(api='gl', prms=['source', 'id', 'length', 'message'])
def glPushDebugGroupKHR(source, id, length, message):
	pass


@params(api='gl', prms=[])
def glPopDebugGroupKHR():
	pass


@params(api='gl', prms=['identifier', 'name', 'length', 'label'])
def glObjectLabelKHR(identifier, name, length, label):
	pass


@params(api='gl', prms=['identifier', 'name', 'bufSize', 'length', 'label'])
def glGetObjectLabelKHR(identifier, name, bufSize, length, label):
	pass


@params(api='gl', prms=['ptr', 'length', 'label'])
def glObjectPtrLabelKHR(ptr, length, label):
	pass


@params(api='gl', prms=['ptr', 'bufSize', 'length', 'label'])
def glGetObjectPtrLabelKHR(ptr, bufSize, length, label):
	pass


@params(api='gl', prms=['pname', 'params'])
def glGetPointervKHR(pname, params):
	pass


