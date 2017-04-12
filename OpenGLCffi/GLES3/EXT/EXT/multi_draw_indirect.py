from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['mode', 'indirect', 'drawcount', 'stride'])
def glMultiDrawArraysIndirectEXT(mode, indirect, drawcount, stride):
	pass


@params(api='gles3', prms=['mode', 'type', 'indirect', 'drawcount', 'stride'])
def glMultiDrawElementsIndirectEXT(mode, type, indirect, drawcount, stride):
	pass


