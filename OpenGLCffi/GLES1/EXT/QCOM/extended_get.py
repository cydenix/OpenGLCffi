from OpenGLCffi.GLES1 import params
@params('textures', 'maxTextures', 'numTextures', api='gles1')
def glExtGetTexturesQCOM(textures, maxTextures, numTextures):
	pass


@params('buffers', 'maxBuffers', 'numBuffers', api='gles1')
def glExtGetBuffersQCOM(buffers, maxBuffers, numBuffers):
	pass


@params('renderbuffers', 'maxRenderbuffers', 'numRenderbuffers', api='gles1')
def glExtGetRenderbuffersQCOM(renderbuffers, maxRenderbuffers, numRenderbuffers):
	pass


@params('framebuffers', 'maxFramebuffers', 'numFramebuffers', api='gles1')
def glExtGetFramebuffersQCOM(framebuffers, maxFramebuffers, numFramebuffers):
	pass


@params('texture', 'face', 'level', 'pname', 'params', api='gles1')
def glExtGetTexLevelParameterivQCOM(texture, face, level, pname, params):
	pass


@params('target', 'pname', 'param', api='gles1')
def glExtTexObjectStateOverrideiQCOM(target, pname, param):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'texels', api='gles1')
def glExtGetTexSubImageQCOM(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, texels):
	pass


@params('target', 'params', api='gles1')
def glExtGetBufferPointervQCOM(target, params):
	pass


