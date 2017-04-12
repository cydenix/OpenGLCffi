from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['first', 'count', 'v'])
def glViewportArrayvOES(first, count, v):
	pass


@params(api='gles3', prms=['index', 'x', 'y', 'w', 'h'])
def glViewportIndexedfOES(index, x, y, w, h):
	pass


@params(api='gles3', prms=['index', 'v'])
def glViewportIndexedfvOES(index, v):
	pass


@params(api='gles3', prms=['first', 'count', 'v'])
def glScissorArrayvOES(first, count, v):
	pass


@params(api='gles3', prms=['index', 'left', 'bottom', 'width', 'height'])
def glScissorIndexedOES(index, left, bottom, width, height):
	pass


@params(api='gles3', prms=['index', 'v'])
def glScissorIndexedvOES(index, v):
	pass


@params(api='gles3', prms=['first', 'count', 'v'])
def glDepthRangeArrayfvOES(first, count, v):
	pass


@params(api='gles3', prms=['index', 'n', 'f'])
def glDepthRangeIndexedfOES(index, n, f):
	pass


@params(api='gles3', prms=['target', 'index', 'data'])
def glGetFloati_vOES(target, index):
	pass


@params(api='gles3', prms=['target', 'index'])
def glEnableiOES(target, index):
	pass


@params(api='gles3', prms=['target', 'index'])
def glDisableiOES(target, index):
	pass


@params(api='gles3', prms=['target', 'index'])
def glIsEnablediOES(target, index):
	pass


