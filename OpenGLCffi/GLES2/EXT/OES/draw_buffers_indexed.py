from OpenGLCffi.GLES2 import params
@params('target', 'index', api='gles2')
def glEnableiOES(target, index):
	pass


@params('target', 'index', api='gles2')
def glDisableiOES(target, index):
	pass


@params('buf', 'mode', api='gles2')
def glBlendEquationiOES(buf, mode):
	pass


@params('buf', 'modeRGB', 'modeAlpha', api='gles2')
def glBlendEquationSeparateiOES(buf, modeRGB, modeAlpha):
	pass


@params('buf', 'src', 'dst', api='gles2')
def glBlendFunciOES(buf, src, dst):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha', api='gles2')
def glBlendFuncSeparateiOES(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params('index', 'r', 'g', 'b', 'a', api='gles2')
def glColorMaskiOES(index, r, g, b, a):
	pass


@params('target', 'index', api='gles2')
def glIsEnablediOES(target, index):
	pass


