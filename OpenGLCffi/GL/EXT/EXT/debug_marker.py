from OpenGLCffi.GL import params
@params(api='gl', prms=['length', 'marker'])
def glInsertEventMarkerEXT(length, marker):
	pass


@params(api='gl', prms=['length', 'marker'])
def glPushGroupMarkerEXT(length, marker):
	pass


@params(api='gl', prms=[])
def glPopGroupMarkerEXT():
	pass


