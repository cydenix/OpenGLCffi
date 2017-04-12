from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'filter', 'weights'])
def glGetTexFilterFuncSGIS(target, filter, weights):
	pass


@params(api='gl', prms=['target', 'filter', 'n', 'weights'])
def glTexFilterFuncSGIS(target, filter, n, weights):
	pass


