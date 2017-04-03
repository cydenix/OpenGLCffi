from OpenGLCffi.GLES2 import params
@params('first', 'count', 'v', api='gles2')
def glViewportArrayvNV(first, count, v):
	pass


@params('index', 'x', 'y', 'w', 'h', api='gles2')
def glViewportIndexedfNV(index, x, y, w, h):
	pass


@params('index', 'v', api='gles2')
def glViewportIndexedfvNV(index, v):
	pass


@params('first', 'count', 'v', api='gles2')
def glScissorArrayvNV(first, count, v):
	pass


@params('index', 'left', 'bottom', 'width', 'height', api='gles2')
def glScissorIndexedNV(index, left, bottom, width, height):
	pass


@params('index', 'v', api='gles2')
def glScissorIndexedvNV(index, v):
	pass


@params('first', 'count', 'v', api='gles2')
def glDepthRangeArrayfvNV(first, count, v):
	pass


@params('index', 'n', 'f', api='gles2')
def glDepthRangeIndexedfNV(index, n, f):
	pass


@params('target', 'index', 'data', api='gles2')
def glGetFloati_vNV(target, index):
	pass


@params('target', 'index', api='gles2')
def glEnableiNV(target, index):
	pass


@params('target', 'index', api='gles2')
def glDisableiNV(target, index):
	pass


@params('target', 'index', api='gles2')
def glIsEnablediNV(target, index):
	pass


