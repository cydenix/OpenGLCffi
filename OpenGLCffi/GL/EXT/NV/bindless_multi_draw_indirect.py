from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'indirect', 'drawCount', 'stride', 'vertexBufferCount'])
def glMultiDrawArraysIndirectBindlessNV(mode, indirect, drawCount, stride, vertexBufferCount):
	pass


@params(api='gl', prms=['mode', 'type', 'indirect', 'drawCount', 'stride', 'vertexBufferCount'])
def glMultiDrawElementsIndirectBindlessNV(mode, type, indirect, drawCount, stride, vertexBufferCount):
	pass


