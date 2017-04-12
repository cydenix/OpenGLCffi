from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['source', 'type', 'severity', 'count', 'ids', 'enabled'])
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params(api='gles3', prms=['source', 'type', 'id', 'severity', 'length', 'buf'])
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params(api='gles3', prms=['callback', 'userParam'])
def glDebugMessageCallback(callback, userParam):
	pass


@params(api='gles3', prms=['count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog'])
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params(api='gles3', prms=['source', 'id', 'length', 'message'])
def glPushDebugGroup(source, id, length, message):
	pass


@params(api='gles3', prms=[])
def glPopDebugGroup():
	pass


@params(api='gles3', prms=['identifier', 'name', 'length', 'label'])
def glObjectLabel(identifier, name, length, label):
	pass


@params(api='gles3', prms=['identifier', 'name', 'bufSize', 'length', 'label'])
def glGetObjectLabel(identifier, name, bufSize, length):
	pass


@params(api='gles3', prms=['ptr', 'length', 'label'])
def glObjectPtrLabel(ptr, length, label):
	pass


@params(api='gles3', prms=['ptr', 'bufSize', 'length', 'label'])
def glGetObjectPtrLabel(ptr, bufSize, length):
	pass


@params(api='gles3', prms=['pname', 'params'])
def glGetPointerv(pname):
	pass


@params(api='gles3', prms=['source', 'type', 'severity', 'count', 'ids', 'enabled'])
def glDebugMessageControlKHR(source, type, severity, count, ids, enabled):
	pass


@params(api='gles3', prms=['source', 'type', 'id', 'severity', 'length', 'buf'])
def glDebugMessageInsertKHR(source, type, id, severity, length, buf):
	pass


@params(api='gles3', prms=['callback', 'userParam'])
def glDebugMessageCallbackKHR(callback, userParam):
	pass


@params(api='gles3', prms=['count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog'])
def glGetDebugMessageLogKHR(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params(api='gles3', prms=['source', 'id', 'length', 'message'])
def glPushDebugGroupKHR(source, id, length, message):
	pass


@params(api='gles3', prms=[])
def glPopDebugGroupKHR():
	pass


@params(api='gles3', prms=['identifier', 'name', 'length', 'label'])
def glObjectLabelKHR(identifier, name, length, label):
	pass


@params(api='gles3', prms=['identifier', 'name', 'bufSize', 'length', 'label'])
def glGetObjectLabelKHR(identifier, name, bufSize, length):
	pass


@params(api='gles3', prms=['ptr', 'length', 'label'])
def glObjectPtrLabelKHR(ptr, length, label):
	pass


@params(api='gles3', prms=['ptr', 'bufSize', 'length', 'label'])
def glGetObjectPtrLabelKHR(ptr, bufSize, length):
	pass


@params(api='gles3', prms=['pname', 'params'])
def glGetPointervKHR(pname):
	pass


