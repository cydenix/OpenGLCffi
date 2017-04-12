from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['textures', 'maxTextures', 'numTextures'])
def glExtGetTexturesQCOM(textures, maxTextures, numTextures):
	pass


@params(api='gles1', prms=['buffers', 'maxBuffers', 'numBuffers'])
def glExtGetBuffersQCOM(buffers, maxBuffers, numBuffers):
	pass


@params(api='gles1', prms=['renderbuffers', 'maxRenderbuffers', 'numRenderbuffers'])
def glExtGetRenderbuffersQCOM(renderbuffers, maxRenderbuffers, numRenderbuffers):
	pass


@params(api='gles1', prms=['framebuffers', 'maxFramebuffers', 'numFramebuffers'])
def glExtGetFramebuffersQCOM(framebuffers, maxFramebuffers, numFramebuffers):
	pass


@params(api='gles1', prms=['texture', 'face', 'level', 'pname', 'params'])
def glExtGetTexLevelParameterivQCOM(texture, face, level, pname, params):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glExtTexObjectStateOverrideiQCOM(target, pname, param):
	pass


@params(api='gles1', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'texels'])
def glExtGetTexSubImageQCOM(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, texels):
	pass


@params(api='gles1', prms=['target', 'params'])
def glExtGetBufferPointervQCOM(target, params):
	pass


