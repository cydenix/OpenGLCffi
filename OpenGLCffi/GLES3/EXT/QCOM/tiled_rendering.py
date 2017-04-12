from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['x', 'y', 'width', 'height', 'preserveMask'])
def glStartTilingQCOM(x, y, width, height, preserveMask):
	pass


@params(api='gles3', prms=['preserveMask'])
def glEndTilingQCOM(preserveMask):
	pass


