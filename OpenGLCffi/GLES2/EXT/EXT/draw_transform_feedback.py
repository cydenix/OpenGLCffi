from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['mode', 'id'])
def glDrawTransformFeedbackEXT(mode, id):
	pass


@params(api='gles2', prms=['mode', 'id', 'instancecount'])
def glDrawTransformFeedbackInstancedEXT(mode, id, instancecount):
	pass


