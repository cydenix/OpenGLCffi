from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['x', 'y', 'width', 'height', 'preserveMask'])
def glStartTilingQCOM(x, y, width, height, preserveMask):
	pass


@params(api='gles2', prms=['preserveMask'])
def glEndTilingQCOM(preserveMask):
	pass


