from OpenGLCffi.GL import params
@params(api='gl', prms=['n', 'states'])
def glCreateStatesNV(n, states):
	pass


@params(api='gl', prms=['n', 'states'])
def glDeleteStatesNV(n, states):
	pass


@params(api='gl', prms=['state'])
def glIsStateNV(state):
	pass


@params(api='gl', prms=['state', 'mode'])
def glStateCaptureNV(state, mode):
	pass


@params(api='gl', prms=['tokenID', 'size'])
def glGetCommandHeaderNV(tokenID, size):
	pass


@params(api='gl', prms=['shadertype'])
def glGetStageIndexNV(shadertype):
	pass


@params(api='gl', prms=['primitiveMode', 'buffer', 'indirects', 'sizes', 'count'])
def glDrawCommandsNV(primitiveMode, buffer, indirects, sizes, count):
	pass


@params(api='gl', prms=['primitiveMode', 'indirects', 'sizes', 'count'])
def glDrawCommandsAddressNV(primitiveMode, indirects, sizes, count):
	pass


@params(api='gl', prms=['buffer', 'indirects', 'sizes', 'states', 'fbos', 'count'])
def glDrawCommandsStatesNV(buffer, indirects, sizes, states, fbos, count):
	pass


@params(api='gl', prms=['indirects', 'sizes', 'states', 'fbos', 'count'])
def glDrawCommandsStatesAddressNV(indirects, sizes, states, fbos, count):
	pass


@params(api='gl', prms=['n', 'lists'])
def glCreateCommandListsNV(n, lists):
	pass


@params(api='gl', prms=['n', 'lists'])
def glDeleteCommandListsNV(n, lists):
	pass


@params(api='gl', prms=['list'])
def glIsCommandListNV(list):
	pass


@params(api='gl', prms=['list', 'segment', 'indirects', 'sizes', 'states', 'fbos', 'count'])
def glListDrawCommandsStatesClientNV(list, segment, indirects, sizes, states, fbos, count):
	pass


@params(api='gl', prms=['list', 'segments'])
def glCommandListSegmentsNV(list, segments):
	pass


@params(api='gl', prms=['list'])
def glCompileCommandListNV(list):
	pass


@params(api='gl', prms=['list'])
def glCallCommandListNV(list):
	pass


