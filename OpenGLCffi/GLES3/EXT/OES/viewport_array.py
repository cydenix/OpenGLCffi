from OpenGLCffi.GLES3 import params
@params('first', 'count', 'v', api='gles3')
def glViewportArrayvOES(first, count, v):
	pass


@params('index', 'x', 'y', 'w', 'h', api='gles3')
def glViewportIndexedfOES(index, x, y, w, h):
	pass


@params('index', 'v', api='gles3')
def glViewportIndexedfvOES(index, v):
	pass


@params('first', 'count', 'v', api='gles3')
def glScissorArrayvOES(first, count, v):
	pass


@params('index', 'left', 'bottom', 'width', 'height', api='gles3')
def glScissorIndexedOES(index, left, bottom, width, height):
	pass


@params('index', 'v', api='gles3')
def glScissorIndexedvOES(index, v):
	pass


@params('first', 'count', 'v', api='gles3')
def glDepthRangeArrayfvOES(first, count, v):
	pass


@params('index', 'n', 'f', api='gles3')
def glDepthRangeIndexedfOES(index, n, f):
	pass


@params('target', 'index', 'data', api='gles3')
def glGetFloati_vOES(target, index):
	pass


@params('target', 'index', api='gles3')
def glEnableiOES(target, index):
	pass


@params('target', 'index', api='gles3')
def glDisableiOES(target, index):
	pass


@params('target', 'index', api='gles3')
def glIsEnablediOES(target, index):
	pass


