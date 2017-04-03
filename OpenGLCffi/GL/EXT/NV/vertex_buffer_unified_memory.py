from OpenGLCffi.GL import params
@params('pname', 'index', 'address', 'length', api='gl')
def glBufferAddressRangeNV(pname, index, address, length):
	pass


@params('size', 'type', 'stride', api='gl')
def glVertexFormatNV(size, type, stride):
	pass


@params('type', 'stride', api='gl')
def glNormalFormatNV(type, stride):
	pass


@params('size', 'type', 'stride', api='gl')
def glColorFormatNV(size, type, stride):
	pass


@params('type', 'stride', api='gl')
def glIndexFormatNV(type, stride):
	pass


@params('size', 'type', 'stride', api='gl')
def glTexCoordFormatNV(size, type, stride):
	pass


@params('stride', api='gl')
def glEdgeFlagFormatNV(stride):
	pass


@params('size', 'type', 'stride', api='gl')
def glSecondaryColorFormatNV(size, type, stride):
	pass


@params('type', 'stride', api='gl')
def glFogCoordFormatNV(type, stride):
	pass


@params('index', 'size', 'type', 'normalized', 'stride', api='gl')
def glVertexAttribFormatNV(index, size, type, normalized, stride):
	pass


@params('index', 'size', 'type', 'stride', api='gl')
def glVertexAttribIFormatNV(index, size, type, stride):
	pass


@params('value', 'index', 'result', api='gl')
def glGetIntegerui64i_vNV(value, index, result):
	pass


