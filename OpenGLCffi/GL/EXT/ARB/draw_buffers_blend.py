@params('buf', 'mode', api='gl')
def glBlendEquationiARB(buf, mode):
	pass


@params('buf', 'modeRGB', 'modeAlpha', api='gl')
def glBlendEquationSeparateiARB(buf, modeRGB, modeAlpha):
	pass


@params('buf', 'src', 'dst', api='gl')
def glBlendFunciARB(buf, src, dst):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha', api='gl')
def glBlendFuncSeparateiARB(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


