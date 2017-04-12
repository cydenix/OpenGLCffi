from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'id', 'instancecount'])
def glDrawTransformFeedbackInstanced(mode, id, instancecount):
	pass


@params(api='gl', prms=['mode', 'id', 'stream', 'instancecount'])
def glDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount):
	pass


