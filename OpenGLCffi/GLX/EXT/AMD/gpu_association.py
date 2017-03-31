@params('maxCount', 'ids', api='glx')
def glXGetGPUIDsAMD(maxCount, ids):
	pass


@params('id', 'property', 'dataType', 'size', 'data', api='glx')
def glXGetGPUInfoAMD(id, property, dataType, size, data):
	pass


@params('ctx', api='glx')
def glXGetContextGPUIDAMD(ctx):
	pass


@params('id', 'share_list', api='glx')
def glXCreateAssociatedContextAMD(id, share_list):
	pass


@params('id', 'share_context', 'attribList', api='glx')
def glXCreateAssociatedContextAttribsAMD(id, share_context, attribList):
	pass


@params('ctx', api='glx')
def glXDeleteAssociatedContextAMD(ctx):
	pass


@params('ctx', api='glx')
def glXMakeAssociatedContextCurrentAMD(ctx):
	pass


@params(api = 'glx')
def glXGetCurrentAssociatedContextAMD():
	pass


@params('dstCtx', 'srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter', api='glx')
def glXBlitContextFramebufferAMD(dstCtx, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


