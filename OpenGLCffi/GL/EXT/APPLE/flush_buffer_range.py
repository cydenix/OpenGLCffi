from OpenGLCffi.GL import params
@params('target', 'pname', 'param', api='gl')
def glBufferParameteriAPPLE(target, pname, param):
	pass


@params('target', 'offset', 'size', api='gl')
def glFlushMappedBufferRangeAPPLE(target, offset, size):
	pass


