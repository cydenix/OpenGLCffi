from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['queryHandle'])
def glBeginPerfQueryINTEL(queryHandle):
	pass


@params(api='gles2', prms=['queryId', 'queryHandle'])
def glCreatePerfQueryINTEL(queryId, queryHandle):
	pass


@params(api='gles2', prms=['queryHandle'])
def glDeletePerfQueryINTEL(queryHandle):
	pass


@params(api='gles2', prms=['queryHandle'])
def glEndPerfQueryINTEL(queryHandle):
	pass


@params(api='gles2', prms=['queryId'])
def glGetFirstPerfQueryIdINTEL(queryId):
	pass


@params(api='gles2', prms=['queryId', 'nextQueryId'])
def glGetNextPerfQueryIdINTEL(queryId, nextQueryId):
	pass


@params(api='gles2', prms=['queryId', 'counterId', 'counterNameLength', 'counterName', 'counterDescLength', 'counterDesc', 'counterOffset', 'counterDataSize', 'counterTypeEnum', 'counterDataTypeEnum', 'rawCounterMaxValue'])
def glGetPerfCounterInfoINTEL(queryId, counterId, counterNameLength, counterName, counterDescLength, counterDesc, counterOffset, counterDataSize, counterTypeEnum, counterDataTypeEnum, rawCounterMaxValue):
	pass


@params(api='gles2', prms=['queryHandle', 'flags', 'dataSize', 'data', 'bytesWritten'])
def glGetPerfQueryDataINTEL(queryHandle, flags, dataSize, bytesWritten):
	pass


@params(api='gles2', prms=['queryName', 'queryId'])
def glGetPerfQueryIdByNameINTEL(queryName, queryId):
	pass


@params(api='gles2', prms=['queryId', 'queryNameLength', 'queryName', 'dataSize', 'noCounters', 'noInstances', 'capsMask'])
def glGetPerfQueryInfoINTEL(queryId, queryNameLength, queryName, dataSize, noCounters, noInstances, capsMask):
	pass


