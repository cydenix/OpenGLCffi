from OpenGLCffi.GL import params
@params(api = 'gl')
def glGetInstrumentsSGIX():
	pass


@params('size', 'buffer', api='gl')
def glInstrumentsBufferSGIX(size, buffer):
	pass


@params('marker_p', api='gl')
def glPollInstrumentsSGIX(marker_p):
	pass


@params('marker', api='gl')
def glReadInstrumentsSGIX(marker):
	pass


@params(api = 'gl')
def glStartInstrumentsSGIX():
	pass


@params('marker', api='gl')
def glStopInstrumentsSGIX(marker):
	pass


