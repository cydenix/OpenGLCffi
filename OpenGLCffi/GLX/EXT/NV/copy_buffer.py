from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'readCtx', 'writeCtx', 'readTarget', 'writeTarget', 'readOffset', 'writeOffset', 'size'])
def glXCopyBufferSubDataNV(dpy, readCtx, writeCtx, readTarget, writeTarget, readOffset, writeOffset, size):
	pass


@params(api='glx', prms=['dpy', 'readCtx', 'writeCtx', 'readBuffer', 'writeBuffer', 'readOffset', 'writeOffset', 'size'])
def glXNamedCopyBufferSubDataNV(dpy, readCtx, writeCtx, readBuffer, writeBuffer, readOffset, writeOffset, size):
	pass


