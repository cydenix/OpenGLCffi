from OpenGLCffi.GL import params
@params(api='gl', prms=['n', 'fences'])
def glGenFencesAPPLE(n, fences):
	pass


@params(api='gl', prms=['n', 'fences'])
def glDeleteFencesAPPLE(n, fences):
	pass


@params(api='gl', prms=['fence'])
def glSetFenceAPPLE(fence):
	pass


@params(api='gl', prms=['fence'])
def glIsFenceAPPLE(fence):
	pass


@params(api='gl', prms=['fence'])
def glTestFenceAPPLE(fence):
	pass


@params(api='gl', prms=['fence'])
def glFinishFenceAPPLE(fence):
	pass


@params(api='gl', prms=['object', 'name'])
def glTestObjectAPPLE(object, name):
	pass


@params(api='gl', prms=['object', 'name'])
def glFinishObjectAPPLE(object, name):
	pass


