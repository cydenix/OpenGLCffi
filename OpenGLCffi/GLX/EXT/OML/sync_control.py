from OpenGLCffi.GLX import params
@params('dpy', 'drawable', 'ust', 'msc', 'sbc', api='glx')
def glXGetSyncValuesOML(dpy, drawable, ust, msc, sbc):
	pass


@params('dpy', 'drawable', 'numerator', 'denominator', api='glx')
def glXGetMscRateOML(dpy, drawable, numerator, denominator):
	pass


@params('dpy', 'drawable', 'target_msc', 'divisor', 'remainder', api='glx')
def glXSwapBuffersMscOML(dpy, drawable, target_msc, divisor, remainder):
	pass


@params('dpy', 'drawable', 'target_msc', 'divisor', 'remainder', 'ust', 'msc', 'sbc', api='glx')
def glXWaitForMscOML(dpy, drawable, target_msc, divisor, remainder, ust, msc, sbc):
	pass


@params('dpy', 'drawable', 'target_sbc', 'ust', 'msc', 'sbc', api='glx')
def glXWaitForSbcOML(dpy, drawable, target_sbc, ust, msc, sbc):
	pass


