from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['matrixpaletteindex'])
def glCurrentPaletteMatrixOES(matrixpaletteindex):
	pass


@params(api='gles1', prms=[])
def glLoadPaletteFromModelViewMatrixOES():
	pass


@params(api='gles1', prms=['size', 'type', 'stride', 'pointer'])
def glMatrixIndexPointerOES(size, type, stride, pointer):
	pass


@params(api='gles1', prms=['size', 'type', 'stride', 'pointer'])
def glWeightPointerOES(size, type, stride, pointer):
	pass


