from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'offset', 'size', 'commit'])
def glBufferPageCommitmentARB(target, offset, size, commit):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'commit'])
def glNamedBufferPageCommitmentEXT(buffer, offset, size, commit):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'commit'])
def glNamedBufferPageCommitmentARB(buffer, offset, size, commit):
	pass


