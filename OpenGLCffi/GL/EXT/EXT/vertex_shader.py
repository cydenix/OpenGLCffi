from OpenGLCffi.GL import params
@params(api = 'gl')
def glBeginVertexShaderEXT():
	pass


@params(api = 'gl')
def glEndVertexShaderEXT():
	pass


@params('id', api='gl')
def glBindVertexShaderEXT(id):
	pass


@params('range', api='gl')
def glGenVertexShadersEXT(range):
	pass


@params('id', api='gl')
def glDeleteVertexShaderEXT(id):
	pass


@params('op', 'res', 'arg1', api='gl')
def glShaderOp1EXT(op, res, arg1):
	pass


@params('op', 'res', 'arg1', 'arg2', api='gl')
def glShaderOp2EXT(op, res, arg1, arg2):
	pass


@params('op', 'res', 'arg1', 'arg2', 'arg3', api='gl')
def glShaderOp3EXT(op, res, arg1, arg2, arg3):
	pass


@params('res', 'in', 'outX', 'outY', 'outZ', 'outW', api='gl')
def glSwizzleEXT(res, in, outX, outY, outZ, outW):
	pass


@params('res', 'in', 'outX', 'outY', 'outZ', 'outW', api='gl')
def glWriteMaskEXT(res, in, outX, outY, outZ, outW):
	pass


@params('res', 'src', 'num', api='gl')
def glInsertComponentEXT(res, src, num):
	pass


@params('res', 'src', 'num', api='gl')
def glExtractComponentEXT(res, src, num):
	pass


@params('datatype', 'storagetype', 'range', 'components', api='gl')
def glGenSymbolsEXT(datatype, storagetype, range, components):
	pass


@params('id', 'type', 'addr', api='gl')
def glSetInvariantEXT(id, type, addr):
	pass


@params('id', 'type', 'addr', api='gl')
def glSetLocalConstantEXT(id, type, addr):
	pass


@params('id', 'addr', api='gl')
def glVariantbvEXT(id, addr):
	pass


@params('id', 'addr', api='gl')
def glVariantsvEXT(id, addr):
	pass


@params('id', 'addr', api='gl')
def glVariantivEXT(id, addr):
	pass


@params('id', 'addr', api='gl')
def glVariantfvEXT(id, addr):
	pass


@params('id', 'addr', api='gl')
def glVariantdvEXT(id, addr):
	pass


@params('id', 'addr', api='gl')
def glVariantubvEXT(id, addr):
	pass


@params('id', 'addr', api='gl')
def glVariantusvEXT(id, addr):
	pass


@params('id', 'addr', api='gl')
def glVariantuivEXT(id, addr):
	pass


@params('id', 'type', 'stride', 'addr', api='gl')
def glVariantPointerEXT(id, type, stride, addr):
	pass


@params('id', api='gl')
def glEnableVariantClientStateEXT(id):
	pass


@params('id', api='gl')
def glDisableVariantClientStateEXT(id):
	pass


@params('light', 'value', api='gl')
def glBindLightParameterEXT(light, value):
	pass


@params('face', 'value', api='gl')
def glBindMaterialParameterEXT(face, value):
	pass


@params('unit', 'coord', 'value', api='gl')
def glBindTexGenParameterEXT(unit, coord, value):
	pass


@params('unit', 'value', api='gl')
def glBindTextureUnitParameterEXT(unit, value):
	pass


@params('value', api='gl')
def glBindParameterEXT(value):
	pass


@params('id', 'cap', api='gl')
def glIsVariantEnabledEXT(id, cap):
	pass


@params('id', 'value', 'data', api='gl')
def glGetVariantBooleanvEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetVariantIntegervEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetVariantFloatvEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetVariantPointervEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetInvariantBooleanvEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetInvariantIntegervEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetInvariantFloatvEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetLocalConstantBooleanvEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetLocalConstantIntegervEXT(id, value, data):
	pass


@params('id', 'value', 'data', api='gl')
def glGetLocalConstantFloatvEXT(id, value, data):
	pass


