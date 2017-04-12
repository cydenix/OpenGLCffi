from OpenGLCffi.GL import params
@params(api='gl', prms=['buf', 'src', 'dst'])
def glBlendFuncIndexedAMD(buf, src, dst):
	pass


@params(api='gl', prms=['buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha'])
def glBlendFuncSeparateIndexedAMD(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params(api='gl', prms=['buf', 'mode'])
def glBlendEquationIndexedAMD(buf, mode):
	pass


@params(api='gl', prms=['buf', 'modeRGB', 'modeAlpha'])
def glBlendEquationSeparateIndexedAMD(buf, modeRGB, modeAlpha):
	pass


