from OpenGLCffi.GL import params
@params(api = 'gl')
def glPrimitiveRestartNV():
	pass


@params('index', api='gl')
def glPrimitiveRestartIndexNV(index):
	pass


