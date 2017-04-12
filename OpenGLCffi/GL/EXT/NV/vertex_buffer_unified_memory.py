from OpenGLCffi.GL import params
@params(api='gl', prms=['pname', 'index', 'address', 'length'])
def glBufferAddressRangeNV(pname, index, address, length):
	pass


@params(api='gl', prms=['size', 'type', 'stride'])
def glVertexFormatNV(size, type, stride):
	pass


@params(api='gl', prms=['type', 'stride'])
def glNormalFormatNV(type, stride):
	pass


@params(api='gl', prms=['size', 'type', 'stride'])
def glColorFormatNV(size, type, stride):
	pass


@params(api='gl', prms=['type', 'stride'])
def glIndexFormatNV(type, stride):
	pass


@params(api='gl', prms=['size', 'type', 'stride'])
def glTexCoordFormatNV(size, type, stride):
	pass


@params(api='gl', prms=['stride'])
def glEdgeFlagFormatNV(stride):
	pass


@params(api='gl', prms=['size', 'type', 'stride'])
def glSecondaryColorFormatNV(size, type, stride):
	pass


@params(api='gl', prms=['type', 'stride'])
def glFogCoordFormatNV(type, stride):
	pass


@params(api='gl', prms=['index', 'size', 'type', 'normalized', 'stride'])
def glVertexAttribFormatNV(index, size, type, normalized, stride):
	pass


@params(api='gl', prms=['index', 'size', 'type', 'stride'])
def glVertexAttribIFormatNV(index, size, type, stride):
	pass


@params(api='gl', prms=['value', 'index', 'result'])
def glGetIntegerui64i_vNV(value, index, result):
	pass


