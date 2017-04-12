from OpenGLCffi.GL import params
@params(api='gl', prms=['buf', 'mode'])
def glBlendEquationiARB(buf, mode):
	pass


@params(api='gl', prms=['buf', 'modeRGB', 'modeAlpha'])
def glBlendEquationSeparateiARB(buf, modeRGB, modeAlpha):
	pass


@params(api='gl', prms=['buf', 'src', 'dst'])
def glBlendFunciARB(buf, src, dst):
	pass


@params(api='gl', prms=['buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha'])
def glBlendFuncSeparateiARB(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


