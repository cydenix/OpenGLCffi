from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['length', 'marker'])
def glInsertEventMarkerEXT(length, marker):
	pass


@params(api='gles2', prms=['length', 'marker'])
def glPushGroupMarkerEXT(length, marker):
	pass


@params(api='gles2', prms=[])
def glPopGroupMarkerEXT():
	pass


