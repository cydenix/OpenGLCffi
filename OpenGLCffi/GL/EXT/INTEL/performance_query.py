from OpenGLCffi.GL import params
@params('queryHandle', api='gl')
def glBeginPerfQueryINTEL(queryHandle):
	pass


@params('queryId', 'queryHandle', api='gl')
def glCreatePerfQueryINTEL(queryId, queryHandle):
	pass


@params('queryHandle', api='gl')
def glDeletePerfQueryINTEL(queryHandle):
	pass


@params('queryHandle', api='gl')
def glEndPerfQueryINTEL(queryHandle):
	pass


@params('queryId', api='gl')
def glGetFirstPerfQueryIdINTEL(queryId):
	pass


@params('queryId', 'nextQueryId', api='gl')
def glGetNextPerfQueryIdINTEL(queryId, nextQueryId):
	pass


@params('queryId', 'counterId', 'counterNameLength', 'counterName', 'counterDescLength', 'counterDesc', 'counterOffset', 'counterDataSize', 'counterTypeEnum', 'counterDataTypeEnum', 'rawCounterMaxValue', api='gl')
def glGetPerfCounterInfoINTEL(queryId, counterId, counterNameLength, counterName, counterDescLength, counterDesc, counterOffset, counterDataSize, counterTypeEnum, counterDataTypeEnum, rawCounterMaxValue):
	pass


@params('queryHandle', 'flags', 'dataSize', 'data', 'bytesWritten', api='gl')
def glGetPerfQueryDataINTEL(queryHandle, flags, dataSize, data, bytesWritten):
	pass


@params('queryName', 'queryId', api='gl')
def glGetPerfQueryIdByNameINTEL(queryName, queryId):
	pass


@params('queryId', 'queryNameLength', 'queryName', 'dataSize', 'noCounters', 'noInstances', 'capsMask', api='gl')
def glGetPerfQueryInfoINTEL(queryId, queryNameLength, queryName, dataSize, noCounters, noInstances, capsMask):
	pass


