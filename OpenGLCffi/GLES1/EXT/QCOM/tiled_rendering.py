from OpenGLCffi.GLES1 import params
@params('x', 'y', 'width', 'height', 'preserveMask', api='gles1')
def glStartTilingQCOM(x, y, width, height, preserveMask):
	pass


@params('preserveMask', api='gles1')
def glEndTilingQCOM(preserveMask):
	pass


