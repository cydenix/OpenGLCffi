from OpenGLCffi.GL import params
@params(api='gl', prms=['marker'])
def glAsyncMarkerSGIX(marker):
	pass


@params(api='gl', prms=['markerp'])
def glFinishAsyncSGIX(markerp):
	pass


@params(api='gl', prms=['markerp'])
def glPollAsyncSGIX(markerp):
	pass


@params(api='gl', prms=['range'])
def glGenAsyncMarkersSGIX(range):
	pass


@params(api='gl', prms=['marker', 'range'])
def glDeleteAsyncMarkersSGIX(marker, range):
	pass


@params(api='gl', prms=['marker'])
def glIsAsyncMarkerSGIX(marker):
	pass


