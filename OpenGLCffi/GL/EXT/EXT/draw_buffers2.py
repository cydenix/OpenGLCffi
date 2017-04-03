from OpenGLCffi.GL import params
@params('index', 'r', 'g', 'b', 'a', api='gl')
def glColorMaskIndexedEXT(index, r, g, b, a):
	pass


@params('target', 'index', 'data', api='gl')
def glGetBooleanIndexedvEXT(target, index, data):
	pass


@params('target', 'index', 'data', api='gl')
def glGetIntegerIndexedvEXT(target, index, data):
	pass


@params('target', 'index', api='gl')
def glEnableIndexedEXT(target, index):
	pass


@params('target', 'index', api='gl')
def glDisableIndexedEXT(target, index):
	pass


@params('target', 'index', api='gl')
def glIsEnabledIndexedEXT(target, index):
	pass


