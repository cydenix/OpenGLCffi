@params('n', 'states', api='gl')
def glCreateStatesNV(n, states):
	pass


@params('n', 'states', api='gl')
def glDeleteStatesNV(n, states):
	pass


@params('state', api='gl')
def glIsStateNV(state):
	pass


@params('state', 'mode', api='gl')
def glStateCaptureNV(state, mode):
	pass


@params('tokenID', 'size', api='gl')
def glGetCommandHeaderNV(tokenID, size):
	pass


@params('shadertype', api='gl')
def glGetStageIndexNV(shadertype):
	pass


@params('primitiveMode', 'buffer', 'indirects', 'sizes', 'count', api='gl')
def glDrawCommandsNV(primitiveMode, buffer, indirects, sizes, count):
	pass


@params('primitiveMode', 'indirects', 'sizes', 'count', api='gl')
def glDrawCommandsAddressNV(primitiveMode, indirects, sizes, count):
	pass


@params('buffer', 'indirects', 'sizes', 'states', 'fbos', 'count', api='gl')
def glDrawCommandsStatesNV(buffer, indirects, sizes, states, fbos, count):
	pass


@params('indirects', 'sizes', 'states', 'fbos', 'count', api='gl')
def glDrawCommandsStatesAddressNV(indirects, sizes, states, fbos, count):
	pass


@params('n', 'lists', api='gl')
def glCreateCommandListsNV(n, lists):
	pass


@params('n', 'lists', api='gl')
def glDeleteCommandListsNV(n, lists):
	pass


@params('list', api='gl')
def glIsCommandListNV(list):
	pass


@params('list', 'segment', 'indirects', 'sizes', 'states', 'fbos', 'count', api='gl')
def glListDrawCommandsStatesClientNV(list, segment, indirects, sizes, states, fbos, count):
	pass


@params('list', 'segments', api='gl')
def glCommandListSegmentsNV(list, segments):
	pass


@params('list', api='gl')
def glCompileCommandListNV(list):
	pass


@params('list', api='gl')
def glCallCommandListNV(list):
	pass


