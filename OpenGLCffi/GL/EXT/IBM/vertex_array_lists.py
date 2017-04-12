from OpenGLCffi.GL import params
@params(api='gl', prms=['size', 'type', 'stride', 'pointer', 'ptrstride'])
def glColorPointerListIBM(size, type, stride, pointer, ptrstride):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'pointer', 'ptrstride'])
def glSecondaryColorPointerListIBM(size, type, stride, pointer, ptrstride):
	pass


@params(api='gl', prms=['stride', 'pointer', 'ptrstride'])
def glEdgeFlagPointerListIBM(stride, pointer, ptrstride):
	pass


@params(api='gl', prms=['type', 'stride', 'pointer', 'ptrstride'])
def glFogCoordPointerListIBM(type, stride, pointer, ptrstride):
	pass


@params(api='gl', prms=['type', 'stride', 'pointer', 'ptrstride'])
def glIndexPointerListIBM(type, stride, pointer, ptrstride):
	pass


@params(api='gl', prms=['type', 'stride', 'pointer', 'ptrstride'])
def glNormalPointerListIBM(type, stride, pointer, ptrstride):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'pointer', 'ptrstride'])
def glTexCoordPointerListIBM(size, type, stride, pointer, ptrstride):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'pointer', 'ptrstride'])
def glVertexPointerListIBM(size, type, stride, pointer, ptrstride):
	pass


