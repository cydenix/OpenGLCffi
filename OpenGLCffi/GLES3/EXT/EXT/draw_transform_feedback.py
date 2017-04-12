from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['mode', 'id'])
def glDrawTransformFeedbackEXT(mode, id):
	pass


@params(api='gles3', prms=['mode', 'id', 'instancecount'])
def glDrawTransformFeedbackInstancedEXT(mode, id, instancecount):
	pass


