from OpenGLCffi.GL import params
@params(api='gl', prms=['size', 'pointer', 'usage'])
def glNewObjectBufferATI(size, pointer, usage):
	pass


@params(api='gl', prms=['buffer'])
def glIsObjectBufferATI(buffer):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'pointer', 'preserve'])
def glUpdateObjectBufferATI(buffer, offset, size, pointer, preserve):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetObjectBufferfvATI(buffer, pname, params):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetObjectBufferivATI(buffer, pname, params):
	pass


@params(api='gl', prms=['buffer'])
def glFreeObjectBufferATI(buffer):
	pass


@params(api='gl', prms=['array', 'size', 'type', 'stride', 'buffer', 'offset'])
def glArrayObjectATI(array, size, type, stride, buffer, offset):
	pass


@params(api='gl', prms=['array', 'pname', 'params'])
def glGetArrayObjectfvATI(array, pname, params):
	pass


@params(api='gl', prms=['array', 'pname', 'params'])
def glGetArrayObjectivATI(array, pname, params):
	pass


@params(api='gl', prms=['id', 'type', 'stride', 'buffer', 'offset'])
def glVariantArrayObjectATI(id, type, stride, buffer, offset):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetVariantArrayObjectfvATI(id, pname, params):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetVariantArrayObjectivATI(id, pname, params):
	pass


