from OpenGLCffi.GLX import params
@params(api = 'glx')
def glXGetCurrentDisplayEXT():
	pass


@params('dpy', 'context', 'attribute', 'value', api='glx')
def glXQueryContextInfoEXT(dpy, context, attribute):
	pass


@params('context', api='glx')
def glXGetContextIDEXT(context):
	pass


@params('dpy', 'contextID', api='glx')
def glXImportContextEXT(dpy, contextID):
	pass


@params('dpy', 'context', api='glx')
def glXFreeContextEXT(dpy, context):
	pass


