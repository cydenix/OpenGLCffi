@params('queryHandle', api='gles3')
def glBeginPerfQueryINTEL(queryHandle):
	pass


@params('queryId', 'queryHandle', api='gles3')
def glCreatePerfQueryINTEL(queryId, queryHandle):
	pass


@params('queryHandle', api='gles3')
def glDeletePerfQueryINTEL(queryHandle):
	pass


@params('queryHandle', api='gles3')
def glEndPerfQueryINTEL(queryHandle):
	pass


@params('queryId', api='gles3')
def glGetFirstPerfQueryIdINTEL(queryId):
	pass


@params('queryId', 'nextQueryId', api='gles3')
def glGetNextPerfQueryIdINTEL(queryId, nextQueryId):
	pass


@params('queryId', 'counterId', 'counterNameLength', 'counterName', 'counterDescLength', 'counterDesc', 'counterOffset', 'counterDataSize', 'counterTypeEnum', 'counterDataTypeEnum', 'rawCounterMaxValue', api='gles3')
def glGetPerfCounterInfoINTEL(queryId, counterId, counterNameLength, counterName, counterDescLength, counterDesc, counterOffset, counterDataSize, counterTypeEnum, counterDataTypeEnum, rawCounterMaxValue):
	pass


@params('queryHandle', 'flags', 'dataSize', 'data', 'bytesWritten', api='gles3')
def glGetPerfQueryDataINTEL(queryHandle, flags, dataSize, bytesWritten):
	pass


@params('queryName', 'queryId', api='gles3')
def glGetPerfQueryIdByNameINTEL(queryName, queryId):
	pass


@params('queryId', 'queryNameLength', 'queryName', 'dataSize', 'noCounters', 'noInstances', 'capsMask', api='gles3')
def glGetPerfQueryInfoINTEL(queryId, queryNameLength, queryName, dataSize, noCounters, noInstances, capsMask):
	pass


