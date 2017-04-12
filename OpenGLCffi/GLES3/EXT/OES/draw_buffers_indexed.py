from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'index'])
def glEnableiOES(target, index):
	pass


@params(api='gles3', prms=['target', 'index'])
def glDisableiOES(target, index):
	pass


@params(api='gles3', prms=['buf', 'mode'])
def glBlendEquationiOES(buf, mode):
	pass


@params(api='gles3', prms=['buf', 'modeRGB', 'modeAlpha'])
def glBlendEquationSeparateiOES(buf, modeRGB, modeAlpha):
	pass


@params(api='gles3', prms=['buf', 'src', 'dst'])
def glBlendFunciOES(buf, src, dst):
	pass


@params(api='gles3', prms=['buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha'])
def glBlendFuncSeparateiOES(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params(api='gles3', prms=['index', 'r', 'g', 'b', 'a'])
def glColorMaskiOES(index, r, g, b, a):
	pass


@params(api='gles3', prms=['target', 'index'])
def glIsEnablediOES(target, index):
	pass


