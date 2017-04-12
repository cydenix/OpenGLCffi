from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'id'])
def glBindTransformFeedback(target, id):
	pass


@params(api='gl', prms=['n', 'ids'])
def glDeleteTransformFeedbacks(n, ids):
	pass


@params(api='gl', prms=['n', 'ids'])
def glGenTransformFeedbacks(n, ids):
	pass


@params(api='gl', prms=['id'])
def glIsTransformFeedback(id):
	pass


@params(api='gl', prms=[])
def glPauseTransformFeedback():
	pass


@params(api='gl', prms=[])
def glResumeTransformFeedback():
	pass


@params(api='gl', prms=['mode', 'id'])
def glDrawTransformFeedback(mode, id):
	pass


