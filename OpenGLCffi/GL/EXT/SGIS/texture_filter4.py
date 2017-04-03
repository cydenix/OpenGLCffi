from OpenGLCffi.GL import params
@params('target', 'filter', 'weights', api='gl')
def glGetTexFilterFuncSGIS(target, filter, weights):
	pass


@params('target', 'filter', 'n', 'weights', api='gl')
def glTexFilterFuncSGIS(target, filter, n, weights):
	pass


