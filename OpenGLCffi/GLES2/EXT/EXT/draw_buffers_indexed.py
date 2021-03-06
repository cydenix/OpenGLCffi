from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'index'])
def glEnableiEXT(target, index):
	pass


@params(api='gles2', prms=['target', 'index'])
def glDisableiEXT(target, index):
	pass


@params(api='gles2', prms=['buf', 'mode'])
def glBlendEquationiEXT(buf, mode):
	pass


@params(api='gles2', prms=['buf', 'modeRGB', 'modeAlpha'])
def glBlendEquationSeparateiEXT(buf, modeRGB, modeAlpha):
	pass


@params(api='gles2', prms=['buf', 'src', 'dst'])
def glBlendFunciEXT(buf, src, dst):
	pass


@params(api='gles2', prms=['buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha'])
def glBlendFuncSeparateiEXT(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params(api='gles2', prms=['index', 'r', 'g', 'b', 'a'])
def glColorMaskiEXT(index, r, g, b, a):
	pass


@params(api='gles2', prms=['target', 'index'])
def glIsEnablediEXT(target, index):
	pass


