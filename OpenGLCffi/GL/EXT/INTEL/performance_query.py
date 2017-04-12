from OpenGLCffi.GL import params
@params(api='gl', prms=['queryHandle'])
def glBeginPerfQueryINTEL(queryHandle):
	pass


@params(api='gl', prms=['queryId', 'queryHandle'])
def glCreatePerfQueryINTEL(queryId, queryHandle):
	pass


@params(api='gl', prms=['queryHandle'])
def glDeletePerfQueryINTEL(queryHandle):
	pass


@params(api='gl', prms=['queryHandle'])
def glEndPerfQueryINTEL(queryHandle):
	pass


@params(api='gl', prms=['queryId'])
def glGetFirstPerfQueryIdINTEL(queryId):
	pass


@params(api='gl', prms=['queryId', 'nextQueryId'])
def glGetNextPerfQueryIdINTEL(queryId, nextQueryId):
	pass


@params(api='gl', prms=['queryId', 'counterId', 'counterNameLength', 'counterName', 'counterDescLength', 'counterDesc', 'counterOffset', 'counterDataSize', 'counterTypeEnum', 'counterDataTypeEnum', 'rawCounterMaxValue'])
def glGetPerfCounterInfoINTEL(queryId, counterId, counterNameLength, counterName, counterDescLength, counterDesc, counterOffset, counterDataSize, counterTypeEnum, counterDataTypeEnum, rawCounterMaxValue):
	pass


@params(api='gl', prms=['queryHandle', 'flags', 'dataSize', 'data', 'bytesWritten'])
def glGetPerfQueryDataINTEL(queryHandle, flags, dataSize, data, bytesWritten):
	pass


@params(api='gl', prms=['queryName', 'queryId'])
def glGetPerfQueryIdByNameINTEL(queryName, queryId):
	pass


@params(api='gl', prms=['queryId', 'queryNameLength', 'queryName', 'dataSize', 'noCounters', 'noInstances', 'capsMask'])
def glGetPerfQueryInfoINTEL(queryId, queryNameLength, queryName, dataSize, noCounters, noInstances, capsMask):
	pass


