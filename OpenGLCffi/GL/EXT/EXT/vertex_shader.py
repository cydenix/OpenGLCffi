from OpenGLCffi.GL import params
@params(api='gl', prms=[])
def glBeginVertexShaderEXT():
	pass


@params(api='gl', prms=[])
def glEndVertexShaderEXT():
	pass


@params(api='gl', prms=['id'])
def glBindVertexShaderEXT(id):
	pass


@params(api='gl', prms=['range'])
def glGenVertexShadersEXT(range):
	pass


@params(api='gl', prms=['id'])
def glDeleteVertexShaderEXT(id):
	pass


@params(api='gl', prms=['op', 'res', 'arg1'])
def glShaderOp1EXT(op, res, arg1):
	pass


@params(api='gl', prms=['op', 'res', 'arg1', 'arg2'])
def glShaderOp2EXT(op, res, arg1, arg2):
	pass


@params(api='gl', prms=['op', 'res', 'arg1', 'arg2', 'arg3'])
def glShaderOp3EXT(op, res, arg1, arg2, arg3):
	pass


@params(api='gl', prms=['res', 'in', 'outX', 'outY', 'outZ', 'outW'])
def glSwizzleEXT(res, in, outX, outY, outZ, outW):
	pass


@params(api='gl', prms=['res', 'in', 'outX', 'outY', 'outZ', 'outW'])
def glWriteMaskEXT(res, in, outX, outY, outZ, outW):
	pass


@params(api='gl', prms=['res', 'src', 'num'])
def glInsertComponentEXT(res, src, num):
	pass


@params(api='gl', prms=['res', 'src', 'num'])
def glExtractComponentEXT(res, src, num):
	pass


@params(api='gl', prms=['datatype', 'storagetype', 'range', 'components'])
def glGenSymbolsEXT(datatype, storagetype, range, components):
	pass


@params(api='gl', prms=['id', 'type', 'addr'])
def glSetInvariantEXT(id, type, addr):
	pass


@params(api='gl', prms=['id', 'type', 'addr'])
def glSetLocalConstantEXT(id, type, addr):
	pass


@params(api='gl', prms=['id', 'addr'])
def glVariantbvEXT(id, addr):
	pass


@params(api='gl', prms=['id', 'addr'])
def glVariantsvEXT(id, addr):
	pass


@params(api='gl', prms=['id', 'addr'])
def glVariantivEXT(id, addr):
	pass


@params(api='gl', prms=['id', 'addr'])
def glVariantfvEXT(id, addr):
	pass


@params(api='gl', prms=['id', 'addr'])
def glVariantdvEXT(id, addr):
	pass


@params(api='gl', prms=['id', 'addr'])
def glVariantubvEXT(id, addr):
	pass


@params(api='gl', prms=['id', 'addr'])
def glVariantusvEXT(id, addr):
	pass


@params(api='gl', prms=['id', 'addr'])
def glVariantuivEXT(id, addr):
	pass


@params(api='gl', prms=['id', 'type', 'stride', 'addr'])
def glVariantPointerEXT(id, type, stride, addr):
	pass


@params(api='gl', prms=['id'])
def glEnableVariantClientStateEXT(id):
	pass


@params(api='gl', prms=['id'])
def glDisableVariantClientStateEXT(id):
	pass


@params(api='gl', prms=['light', 'value'])
def glBindLightParameterEXT(light, value):
	pass


@params(api='gl', prms=['face', 'value'])
def glBindMaterialParameterEXT(face, value):
	pass


@params(api='gl', prms=['unit', 'coord', 'value'])
def glBindTexGenParameterEXT(unit, coord, value):
	pass


@params(api='gl', prms=['unit', 'value'])
def glBindTextureUnitParameterEXT(unit, value):
	pass


@params(api='gl', prms=['value'])
def glBindParameterEXT(value):
	pass


@params(api='gl', prms=['id', 'cap'])
def glIsVariantEnabledEXT(id, cap):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetVariantBooleanvEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetVariantIntegervEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetVariantFloatvEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetVariantPointervEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetInvariantBooleanvEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetInvariantIntegervEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetInvariantFloatvEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetLocalConstantBooleanvEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetLocalConstantIntegervEXT(id, value, data):
	pass


@params(api='gl', prms=['id', 'value', 'data'])
def glGetLocalConstantFloatvEXT(id, value, data):
	pass


