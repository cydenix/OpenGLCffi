from OpenGLCffi.GLES2 import params
@params('first', 'count', 'v', api='gles2')
def glViewportArrayvOES(first, count, v):
	pass


@params('index', 'x', 'y', 'w', 'h', api='gles2')
def glViewportIndexedfOES(index, x, y, w, h):
	pass


@params('index', 'v', api='gles2')
def glViewportIndexedfvOES(index, v):
	pass


@params('first', 'count', 'v', api='gles2')
def glScissorArrayvOES(first, count, v):
	pass


@params('index', 'left', 'bottom', 'width', 'height', api='gles2')
def glScissorIndexedOES(index, left, bottom, width, height):
	pass


@params('index', 'v', api='gles2')
def glScissorIndexedvOES(index, v):
	pass


@params('first', 'count', 'v', api='gles2')
def glDepthRangeArrayfvOES(first, count, v):
	pass


@params('index', 'n', 'f', api='gles2')
def glDepthRangeIndexedfOES(index, n, f):
	pass


@params('target', 'index', 'data', api='gles2')
def glGetFloati_vOES(target, index):
	pass


@params('target', 'index', api='gles2')
def glEnableiOES(target, index):
	pass


@params('target', 'index', api='gles2')
def glDisableiOES(target, index):
	pass


@params('target', 'index', api='gles2')
def glIsEnablediOES(target, index):
	pass


