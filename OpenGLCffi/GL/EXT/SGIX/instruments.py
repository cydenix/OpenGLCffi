from OpenGLCffi.GL import params
@params(api='gl', prms=[])
def glGetInstrumentsSGIX():
	pass


@params(api='gl', prms=['size', 'buffer'])
def glInstrumentsBufferSGIX(size, buffer):
	pass


@params(api='gl', prms=['marker_p'])
def glPollInstrumentsSGIX(marker_p):
	pass


@params(api='gl', prms=['marker'])
def glReadInstrumentsSGIX(marker):
	pass


@params(api='gl', prms=[])
def glStartInstrumentsSGIX():
	pass


@params(api='gl', prms=['marker'])
def glStopInstrumentsSGIX(marker):
	pass


