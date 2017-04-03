from OpenGLCffi.GLES3 import params
@params('first', 'count', 'v', api='gles3')
def glViewportArrayvNV(first, count, v):
	pass


@params('index', 'x', 'y', 'w', 'h', api='gles3')
def glViewportIndexedfNV(index, x, y, w, h):
	pass


@params('index', 'v', api='gles3')
def glViewportIndexedfvNV(index, v):
	pass


@params('first', 'count', 'v', api='gles3')
def glScissorArrayvNV(first, count, v):
	pass


@params('index', 'left', 'bottom', 'width', 'height', api='gles3')
def glScissorIndexedNV(index, left, bottom, width, height):
	pass


@params('index', 'v', api='gles3')
def glScissorIndexedvNV(index, v):
	pass


@params('first', 'count', 'v', api='gles3')
def glDepthRangeArrayfvNV(first, count, v):
	pass


@params('index', 'n', 'f', api='gles3')
def glDepthRangeIndexedfNV(index, n, f):
	pass


@params('target', 'index', 'data', api='gles3')
def glGetFloati_vNV(target, index):
	pass


@params('target', 'index', api='gles3')
def glEnableiNV(target, index):
	pass


@params('target', 'index', api='gles3')
def glDisableiNV(target, index):
	pass


@params('target', 'index', api='gles3')
def glIsEnablediNV(target, index):
	pass


