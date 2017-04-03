from OpenGLCffi.GLES2 import params
@params('x', 'y', 'width', 'height', 'preserveMask', api='gles2')
def glStartTilingQCOM(x, y, width, height, preserveMask):
	pass


@params('preserveMask', api='gles2')
def glEndTilingQCOM(preserveMask):
	pass


