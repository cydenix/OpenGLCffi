from OpenGLCffi.GL import params
@params(api='gl', prms=['range'])
def glGenFragmentShadersATI(range):
	pass


@params(api='gl', prms=['id'])
def glBindFragmentShaderATI(id):
	pass


@params(api='gl', prms=['id'])
def glDeleteFragmentShaderATI(id):
	pass


@params(api='gl', prms=[])
def glBeginFragmentShaderATI():
	pass


@params(api='gl', prms=[])
def glEndFragmentShaderATI():
	pass


@params(api='gl', prms=['dst', 'coord', 'swizzle'])
def glPassTexCoordATI(dst, coord, swizzle):
	pass


@params(api='gl', prms=['dst', 'interp', 'swizzle'])
def glSampleMapATI(dst, interp, swizzle):
	pass


@params(api='gl', prms=['op', 'dst', 'dstMask', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod'])
def glColorFragmentOp1ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod):
	pass


@params(api='gl', prms=['op', 'dst', 'dstMask', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', 'arg2', 'arg2Rep', 'arg2Mod'])
def glColorFragmentOp2ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod):
	pass


@params(api='gl', prms=['op', 'dst', 'dstMask', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', 'arg2', 'arg2Rep', 'arg2Mod', 'arg3', 'arg3Rep', 'arg3Mod'])
def glColorFragmentOp3ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod, arg3, arg3Rep, arg3Mod):
	pass


@params(api='gl', prms=['op', 'dst', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod'])
def glAlphaFragmentOp1ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod):
	pass


@params(api='gl', prms=['op', 'dst', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', 'arg2', 'arg2Rep', 'arg2Mod'])
def glAlphaFragmentOp2ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod):
	pass


@params(api='gl', prms=['op', 'dst', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', 'arg2', 'arg2Rep', 'arg2Mod', 'arg3', 'arg3Rep', 'arg3Mod'])
def glAlphaFragmentOp3ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod, arg3, arg3Rep, arg3Mod):
	pass


@params(api='gl', prms=['dst', 'value'])
def glSetFragmentShaderConstantATI(dst, value):
	pass


