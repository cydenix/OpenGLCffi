@params('marker', api='gl')
def glAsyncMarkerSGIX(marker):
	pass


@params('markerp', api='gl')
def glFinishAsyncSGIX(markerp):
	pass


@params('markerp', api='gl')
def glPollAsyncSGIX(markerp):
	pass


@params('range', api='gl')
def glGenAsyncMarkersSGIX(range):
	pass


@params('marker', 'range', api='gl')
def glDeleteAsyncMarkersSGIX(marker, range):
	pass


@params('marker', api='gl')
def glIsAsyncMarkerSGIX(marker):
	pass


