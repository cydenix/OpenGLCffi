from OpenGLCffi.GL import params
@params(api='gl', prms=['type', 'object', 'length', 'label'])
def glLabelObjectEXT(type, object, length, label):
	pass


@params(api='gl', prms=['type', 'object', 'bufSize', 'length', 'label'])
def glGetObjectLabelEXT(type, object, bufSize, length, label):
	pass


