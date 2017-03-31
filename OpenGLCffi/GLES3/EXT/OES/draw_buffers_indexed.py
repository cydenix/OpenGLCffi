@params('target', 'index', api='gles3')
def glEnableiOES(target, index):
	pass


@params('target', 'index', api='gles3')
def glDisableiOES(target, index):
	pass


@params('buf', 'mode', api='gles3')
def glBlendEquationiOES(buf, mode):
	pass


@params('buf', 'modeRGB', 'modeAlpha', api='gles3')
def glBlendEquationSeparateiOES(buf, modeRGB, modeAlpha):
	pass


@params('buf', 'src', 'dst', api='gles3')
def glBlendFunciOES(buf, src, dst):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha', api='gles3')
def glBlendFuncSeparateiOES(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params('index', 'r', 'g', 'b', 'a', api='gles3')
def glColorMaskiOES(index, r, g, b, a):
	pass


@params('target', 'index', api='gles3')
def glIsEnablediOES(target, index):
	pass


