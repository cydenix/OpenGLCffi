from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'indirect', 'drawCount', 'maxDrawCount', 'stride', 'vertexBufferCount'])
def glMultiDrawArraysIndirectBindlessCountNV(mode, indirect, drawCount, maxDrawCount, stride, vertexBufferCount):
	pass


@params(api='gl', prms=['mode', 'type', 'indirect', 'drawCount', 'maxDrawCount', 'stride', 'vertexBufferCount'])
def glMultiDrawElementsIndirectBindlessCountNV(mode, type, indirect, drawCount, maxDrawCount, stride, vertexBufferCount):
	pass


