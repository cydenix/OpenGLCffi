@params('size', 'pointer', 'usage', api='gl')
def glNewObjectBufferATI(size, pointer, usage):
	pass


@params('buffer', api='gl')
def glIsObjectBufferATI(buffer):
	pass


@params('buffer', 'offset', 'size', 'pointer', 'preserve', api='gl')
def glUpdateObjectBufferATI(buffer, offset, size, pointer, preserve):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetObjectBufferfvATI(buffer, pname, params):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetObjectBufferivATI(buffer, pname, params):
	pass


@params('buffer', api='gl')
def glFreeObjectBufferATI(buffer):
	pass


@params('array', 'size', 'type', 'stride', 'buffer', 'offset', api='gl')
def glArrayObjectATI(array, size, type, stride, buffer, offset):
	pass


@params('array', 'pname', 'params', api='gl')
def glGetArrayObjectfvATI(array, pname, params):
	pass


@params('array', 'pname', 'params', api='gl')
def glGetArrayObjectivATI(array, pname, params):
	pass


@params('id', 'type', 'stride', 'buffer', 'offset', api='gl')
def glVariantArrayObjectATI(id, type, stride, buffer, offset):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetVariantArrayObjectfvATI(id, pname, params):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetVariantArrayObjectivATI(id, pname, params):
	pass


