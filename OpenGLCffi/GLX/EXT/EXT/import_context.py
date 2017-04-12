from OpenGLCffi.GLX import params
@params(api='glx', prms=[])
def glXGetCurrentDisplayEXT():
	pass


@params(api='glx', prms=['dpy', 'context', 'attribute', 'value'])
def glXQueryContextInfoEXT(dpy, context, attribute):
	pass


@params(api='glx', prms=['context'])
def glXGetContextIDEXT(context):
	pass


@params(api='glx', prms=['dpy', 'contextID'])
def glXImportContextEXT(dpy, contextID):
	pass


@params(api='glx', prms=['dpy', 'context'])
def glXFreeContextEXT(dpy, context):
	pass


