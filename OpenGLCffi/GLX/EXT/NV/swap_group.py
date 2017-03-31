@params('dpy', 'drawable', 'group', api='glx')
def glXJoinSwapGroupNV(dpy, drawable, group):
	pass


@params('dpy', 'group', 'barrier', api='glx')
def glXBindSwapBarrierNV(dpy, group, barrier):
	pass


@params('dpy', 'drawable', 'group', 'barrier', api='glx')
def glXQuerySwapGroupNV(dpy, drawable, group, barrier):
	pass


@params('dpy', 'screen', 'maxGroups', 'maxBarriers', api='glx')
def glXQueryMaxSwapGroupsNV(dpy, screen, maxGroups, maxBarriers):
	pass


@params('dpy', 'screen', 'count', api='glx')
def glXQueryFrameCountNV(dpy, screen, count):
	pass


@params('dpy', 'screen', api='glx')
def glXResetFrameCountNV(dpy, screen):
	pass


