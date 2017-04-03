from OpenGLCffi.GLES3 import params
@params('x', 'y', 'width', 'height', 'preserveMask', api='gles3')
def glStartTilingQCOM(x, y, width, height, preserveMask):
	pass


@params('preserveMask', api='gles3')
def glEndTilingQCOM(preserveMask):
	pass


