from OpenGLCffi.GLES3 import params
@params('length', 'marker', api='gles3')
def glInsertEventMarkerEXT(length, marker):
	pass


@params('length', 'marker', api='gles3')
def glPushGroupMarkerEXT(length, marker):
	pass


@params(api = 'gles3')
def glPopGroupMarkerEXT():
	pass


