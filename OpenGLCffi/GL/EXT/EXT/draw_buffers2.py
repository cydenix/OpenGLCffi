from OpenGLCffi.GL import params
@params(api='gl', prms=['index', 'r', 'g', 'b', 'a'])
def glColorMaskIndexedEXT(index, r, g, b, a):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetBooleanIndexedvEXT(target, index, data):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetIntegerIndexedvEXT(target, index, data):
	pass


@params(api='gl', prms=['target', 'index'])
def glEnableIndexedEXT(target, index):
	pass


@params(api='gl', prms=['target', 'index'])
def glDisableIndexedEXT(target, index):
	pass


@params(api='gl', prms=['target', 'index'])
def glIsEnabledIndexedEXT(target, index):
	pass


