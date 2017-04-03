from OpenGLCffi.GL import params
@params('target', 'id', api='gl')
def glBindTransformFeedback(target, id):
	pass


@params('n', 'ids', api='gl')
def glDeleteTransformFeedbacks(n, ids):
	pass


@params('n', 'ids', api='gl')
def glGenTransformFeedbacks(n, ids):
	pass


@params('id', api='gl')
def glIsTransformFeedback(id):
	pass


@params(api = 'gl')
def glPauseTransformFeedback():
	pass


@params(api = 'gl')
def glResumeTransformFeedback():
	pass


@params('mode', 'id', api='gl')
def glDrawTransformFeedback(mode, id):
	pass


