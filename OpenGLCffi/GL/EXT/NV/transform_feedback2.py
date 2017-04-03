from OpenGLCffi.GL import params
@params('target', 'id', api='gl')
def glBindTransformFeedbackNV(target, id):
	pass


@params('n', 'ids', api='gl')
def glDeleteTransformFeedbacksNV(n, ids):
	pass


@params('n', 'ids', api='gl')
def glGenTransformFeedbacksNV(n, ids):
	pass


@params('id', api='gl')
def glIsTransformFeedbackNV(id):
	pass


@params(api = 'gl')
def glPauseTransformFeedbackNV():
	pass


@params(api = 'gl')
def glResumeTransformFeedbackNV():
	pass


@params('mode', 'id', api='gl')
def glDrawTransformFeedbackNV(mode, id):
	pass


