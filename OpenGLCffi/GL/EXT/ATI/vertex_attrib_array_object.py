from OpenGLCffi.GL import params
@params(api='gl', prms=['index', 'size', 'type', 'normalized', 'stride', 'buffer', 'offset'])
def glVertexAttribArrayObjectATI(index, size, type, normalized, stride, buffer, offset):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribArrayObjectfvATI(index, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribArrayObjectivATI(index, pname, params):
	pass


