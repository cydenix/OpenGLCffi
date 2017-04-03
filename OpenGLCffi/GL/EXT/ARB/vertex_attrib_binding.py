from OpenGLCffi.GL import params
@params('bindingindex', 'buffer', 'offset', 'stride', api='gl')
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	pass


@params('attribindex', 'size', 'type', 'normalized', 'relativeoffset', api='gl')
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	pass


@params('attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	pass


@params('attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexAttribLFormat(attribindex, size, type, relativeoffset):
	pass


@params('attribindex', 'bindingindex', api='gl')
def glVertexAttribBinding(attribindex, bindingindex):
	pass


@params('bindingindex', 'divisor', api='gl')
def glVertexBindingDivisor(bindingindex, divisor):
	pass


