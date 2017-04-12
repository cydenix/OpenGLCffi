from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'drawable', 'group'])
def glXJoinSwapGroupNV(dpy, drawable, group):
	pass


@params(api='glx', prms=['dpy', 'group', 'barrier'])
def glXBindSwapBarrierNV(dpy, group, barrier):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'group', 'barrier'])
def glXQuerySwapGroupNV(dpy, drawable, group, barrier):
	pass


@params(api='glx', prms=['dpy', 'screen', 'maxGroups', 'maxBarriers'])
def glXQueryMaxSwapGroupsNV(dpy, screen, maxGroups, maxBarriers):
	pass


@params(api='glx', prms=['dpy', 'screen', 'count'])
def glXQueryFrameCountNV(dpy, screen, count):
	pass


@params(api='glx', prms=['dpy', 'screen'])
def glXResetFrameCountNV(dpy, screen):
	pass


