from OpenGLCffi.GLX import params
@params(api='glx', prms=['maxCount', 'ids'])
def glXGetGPUIDsAMD(maxCount, ids):
	pass


@params(api='glx', prms=['id', 'property', 'dataType', 'size', 'data'])
def glXGetGPUInfoAMD(id, property, dataType, size, data):
	pass


@params(api='glx', prms=['ctx'])
def glXGetContextGPUIDAMD(ctx):
	pass


@params(api='glx', prms=['id', 'share_list'])
def glXCreateAssociatedContextAMD(id, share_list):
	pass


@params(api='glx', prms=['id', 'share_context', 'attribList'])
def glXCreateAssociatedContextAttribsAMD(id, share_context, attribList):
	pass


@params(api='glx', prms=['ctx'])
def glXDeleteAssociatedContextAMD(ctx):
	pass


@params(api='glx', prms=['ctx'])
def glXMakeAssociatedContextCurrentAMD(ctx):
	pass


@params(api='glx', prms=[])
def glXGetCurrentAssociatedContextAMD():
	pass


@params(api='glx', prms=['dstCtx', 'srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter'])
def glXBlitContextFramebufferAMD(dstCtx, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


