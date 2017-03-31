@params('range', api='gl')
def glGenFragmentShadersATI(range):
	pass


@params('id', api='gl')
def glBindFragmentShaderATI(id):
	pass


@params('id', api='gl')
def glDeleteFragmentShaderATI(id):
	pass


@params(api = 'gl')
def glBeginFragmentShaderATI():
	pass


@params(api = 'gl')
def glEndFragmentShaderATI():
	pass


@params('dst', 'coord', 'swizzle', api='gl')
def glPassTexCoordATI(dst, coord, swizzle):
	pass


@params('dst', 'interp', 'swizzle', api='gl')
def glSampleMapATI(dst, interp, swizzle):
	pass


@params('op', 'dst', 'dstMask', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', api='gl')
def glColorFragmentOp1ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod):
	pass


@params('op', 'dst', 'dstMask', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', 'arg2', 'arg2Rep', 'arg2Mod', api='gl')
def glColorFragmentOp2ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod):
	pass


@params('op', 'dst', 'dstMask', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', 'arg2', 'arg2Rep', 'arg2Mod', 'arg3', 'arg3Rep', 'arg3Mod', api='gl')
def glColorFragmentOp3ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod, arg3, arg3Rep, arg3Mod):
	pass


@params('op', 'dst', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', api='gl')
def glAlphaFragmentOp1ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod):
	pass


@params('op', 'dst', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', 'arg2', 'arg2Rep', 'arg2Mod', api='gl')
def glAlphaFragmentOp2ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod):
	pass


@params('op', 'dst', 'dstMod', 'arg1', 'arg1Rep', 'arg1Mod', 'arg2', 'arg2Rep', 'arg2Mod', 'arg3', 'arg3Rep', 'arg3Mod', api='gl')
def glAlphaFragmentOp3ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod, arg3, arg3Rep, arg3Mod):
	pass


@params('dst', 'value', api='gl')
def glSetFragmentShaderConstantATI(dst, value):
	pass


