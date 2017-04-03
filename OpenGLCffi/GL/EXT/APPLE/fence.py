from OpenGLCffi.GL import params
@params('n', 'fences', api='gl')
def glGenFencesAPPLE(n, fences):
	pass


@params('n', 'fences', api='gl')
def glDeleteFencesAPPLE(n, fences):
	pass


@params('fence', api='gl')
def glSetFenceAPPLE(fence):
	pass


@params('fence', api='gl')
def glIsFenceAPPLE(fence):
	pass


@params('fence', api='gl')
def glTestFenceAPPLE(fence):
	pass


@params('fence', api='gl')
def glFinishFenceAPPLE(fence):
	pass


@params('object', 'name', api='gl')
def glTestObjectAPPLE(object, name):
	pass


@params('object', 'name', api='gl')
def glFinishObjectAPPLE(object, name):
	pass


