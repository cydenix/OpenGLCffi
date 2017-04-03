from OpenGLCffi.GL import params
@params('length', 'marker', api='gl')
def glInsertEventMarkerEXT(length, marker):
	pass


@params('length', 'marker', api='gl')
def glPushGroupMarkerEXT(length, marker):
	pass


@params(api = 'gl')
def glPopGroupMarkerEXT():
	pass


