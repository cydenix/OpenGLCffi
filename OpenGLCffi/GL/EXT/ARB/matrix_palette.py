from OpenGLCffi.GL import params
@params(api='gl', prms=['index'])
def glCurrentPaletteMatrixARB(index):
	pass


@params(api='gl', prms=['size', 'indices'])
def glMatrixIndexubvARB(size, indices):
	pass


@params(api='gl', prms=['size', 'indices'])
def glMatrixIndexusvARB(size, indices):
	pass


@params(api='gl', prms=['size', 'indices'])
def glMatrixIndexuivARB(size, indices):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'pointer'])
def glMatrixIndexPointerARB(size, type, stride, pointer):
	pass


