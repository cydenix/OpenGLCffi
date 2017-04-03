from OpenGLCffi.GL import params
@params('target', 'offset', 'size', 'commit', api='gl')
def glBufferPageCommitmentARB(target, offset, size, commit):
	pass


@params('buffer', 'offset', 'size', 'commit', api='gl')
def glNamedBufferPageCommitmentEXT(buffer, offset, size, commit):
	pass


@params('buffer', 'offset', 'size', 'commit', api='gl')
def glNamedBufferPageCommitmentARB(buffer, offset, size, commit):
	pass


