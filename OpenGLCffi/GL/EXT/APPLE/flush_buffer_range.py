from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'pname', 'param'])
def glBufferParameteriAPPLE(target, pname, param):
	pass


@params(api='gl', prms=['target', 'offset', 'size'])
def glFlushMappedBufferRangeAPPLE(target, offset, size):
	pass


