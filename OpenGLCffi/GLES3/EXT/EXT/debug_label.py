from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['type', 'object', 'length', 'label'])
def glLabelObjectEXT(type, object, length, label):
	pass


@params(api='gles3', prms=['type', 'object', 'bufSize', 'length', 'label'])
def glGetObjectLabelEXT(type, object, bufSize, length):
	pass


