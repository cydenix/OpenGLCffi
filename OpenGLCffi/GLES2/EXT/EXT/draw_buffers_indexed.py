@params('target', 'index', api='gles2')
def glEnableiEXT(target, index):
	pass


@params('target', 'index', api='gles2')
def glDisableiEXT(target, index):
	pass


@params('buf', 'mode', api='gles2')
def glBlendEquationiEXT(buf, mode):
	pass


@params('buf', 'modeRGB', 'modeAlpha', api='gles2')
def glBlendEquationSeparateiEXT(buf, modeRGB, modeAlpha):
	pass


@params('buf', 'src', 'dst', api='gles2')
def glBlendFunciEXT(buf, src, dst):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha', api='gles2')
def glBlendFuncSeparateiEXT(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params('index', 'r', 'g', 'b', 'a', api='gles2')
def glColorMaskiEXT(index, r, g, b, a):
	pass


@params('target', 'index', api='gles2')
def glIsEnablediEXT(target, index):
	pass


