from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['x', 'y', 'width', 'height', 'preserveMask'])
def glStartTilingQCOM(x, y, width, height, preserveMask):
	pass


@params(api='gles1', prms=['preserveMask'])
def glEndTilingQCOM(preserveMask):
	pass


