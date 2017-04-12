from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['mode', 'indirect', 'drawcount', 'stride'])
def glMultiDrawArraysIndirectEXT(mode, indirect, drawcount, stride):
	pass


@params(api='gles2', prms=['mode', 'type', 'indirect', 'drawcount', 'stride'])
def glMultiDrawElementsIndirectEXT(mode, type, indirect, drawcount, stride):
	pass


