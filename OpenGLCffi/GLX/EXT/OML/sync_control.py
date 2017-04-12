from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'drawable', 'ust', 'msc', 'sbc'])
def glXGetSyncValuesOML(dpy, drawable, ust, msc, sbc):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'numerator', 'denominator'])
def glXGetMscRateOML(dpy, drawable, numerator, denominator):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'target_msc', 'divisor', 'remainder'])
def glXSwapBuffersMscOML(dpy, drawable, target_msc, divisor, remainder):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'target_msc', 'divisor', 'remainder', 'ust', 'msc', 'sbc'])
def glXWaitForMscOML(dpy, drawable, target_msc, divisor, remainder, ust, msc, sbc):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'target_sbc', 'ust', 'msc', 'sbc'])
def glXWaitForSbcOML(dpy, drawable, target_sbc, ust, msc, sbc):
	pass


