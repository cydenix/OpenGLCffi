from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'id'])
def glBindTransformFeedbackNV(target, id):
	pass


@params(api='gl', prms=['n', 'ids'])
def glDeleteTransformFeedbacksNV(n, ids):
	pass


@params(api='gl', prms=['n', 'ids'])
def glGenTransformFeedbacksNV(n, ids):
	pass


@params(api='gl', prms=['id'])
def glIsTransformFeedbackNV(id):
	pass


@params(api='gl', prms=[])
def glPauseTransformFeedbackNV():
	pass


@params(api='gl', prms=[])
def glResumeTransformFeedbackNV():
	pass


@params(api='gl', prms=['mode', 'id'])
def glDrawTransformFeedbackNV(mode, id):
	pass


