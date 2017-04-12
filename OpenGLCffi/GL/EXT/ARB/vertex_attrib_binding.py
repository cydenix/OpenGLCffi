from OpenGLCffi.GL import params
@params(api='gl', prms=['bindingindex', 'buffer', 'offset', 'stride'])
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	pass


@params(api='gl', prms=['attribindex', 'size', 'type', 'normalized', 'relativeoffset'])
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	pass


@params(api='gl', prms=['attribindex', 'size', 'type', 'relativeoffset'])
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['attribindex', 'size', 'type', 'relativeoffset'])
def glVertexAttribLFormat(attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['attribindex', 'bindingindex'])
def glVertexAttribBinding(attribindex, bindingindex):
	pass


@params(api='gl', prms=['bindingindex', 'divisor'])
def glVertexBindingDivisor(bindingindex, divisor):
	pass


