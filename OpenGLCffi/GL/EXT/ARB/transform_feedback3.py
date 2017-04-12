from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'id', 'stream'])
def glDrawTransformFeedbackStream(mode, id, stream):
	pass


@params(api='gl', prms=['target', 'index', 'id'])
def glBeginQueryIndexed(target, index, id):
	pass


@params(api='gl', prms=['target', 'index'])
def glEndQueryIndexed(target, index):
	pass


@params(api='gl', prms=['target', 'index', 'pname', 'params'])
def glGetQueryIndexediv(target, index, pname, params):
	pass


