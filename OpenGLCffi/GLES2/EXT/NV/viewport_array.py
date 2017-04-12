from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['first', 'count', 'v'])
def glViewportArrayvNV(first, count, v):
	pass


@params(api='gles2', prms=['index', 'x', 'y', 'w', 'h'])
def glViewportIndexedfNV(index, x, y, w, h):
	pass


@params(api='gles2', prms=['index', 'v'])
def glViewportIndexedfvNV(index, v):
	pass


@params(api='gles2', prms=['first', 'count', 'v'])
def glScissorArrayvNV(first, count, v):
	pass


@params(api='gles2', prms=['index', 'left', 'bottom', 'width', 'height'])
def glScissorIndexedNV(index, left, bottom, width, height):
	pass


@params(api='gles2', prms=['index', 'v'])
def glScissorIndexedvNV(index, v):
	pass


@params(api='gles2', prms=['first', 'count', 'v'])
def glDepthRangeArrayfvNV(first, count, v):
	pass


@params(api='gles2', prms=['index', 'n', 'f'])
def glDepthRangeIndexedfNV(index, n, f):
	pass


@params(api='gles2', prms=['target', 'index', 'data'])
def glGetFloati_vNV(target, index):
	pass


@params(api='gles2', prms=['target', 'index'])
def glEnableiNV(target, index):
	pass


@params(api='gles2', prms=['target', 'index'])
def glDisableiNV(target, index):
	pass


@params(api='gles2', prms=['target', 'index'])
def glIsEnablediNV(target, index):
	pass


