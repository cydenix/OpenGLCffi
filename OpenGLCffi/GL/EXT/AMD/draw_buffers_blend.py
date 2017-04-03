from OpenGLCffi.GL import params
@params('buf', 'src', 'dst', api='gl')
def glBlendFuncIndexedAMD(buf, src, dst):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha', api='gl')
def glBlendFuncSeparateIndexedAMD(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params('buf', 'mode', api='gl')
def glBlendEquationIndexedAMD(buf, mode):
	pass


@params('buf', 'modeRGB', 'modeAlpha', api='gl')
def glBlendEquationSeparateIndexedAMD(buf, modeRGB, modeAlpha):
	pass


