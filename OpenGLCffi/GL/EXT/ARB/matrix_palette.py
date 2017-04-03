from OpenGLCffi.GL import params
@params('index', api='gl')
def glCurrentPaletteMatrixARB(index):
	pass


@params('size', 'indices', api='gl')
def glMatrixIndexubvARB(size, indices):
	pass


@params('size', 'indices', api='gl')
def glMatrixIndexusvARB(size, indices):
	pass


@params('size', 'indices', api='gl')
def glMatrixIndexuivARB(size, indices):
	pass


@params('size', 'type', 'stride', 'pointer', api='gl')
def glMatrixIndexPointerARB(size, type, stride, pointer):
	pass


