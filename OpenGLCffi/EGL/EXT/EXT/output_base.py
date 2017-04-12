from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'attrib_list', 'layers', 'max_layers', 'num_layers'])
def eglGetOutputLayersEXT(dpy, attrib_list, layers, max_layers, num_layers):
	pass


@params(api='egl', prms=['dpy', 'attrib_list', 'ports', 'max_ports', 'num_ports'])
def eglGetOutputPortsEXT(dpy, attrib_list, ports, max_ports, num_ports):
	pass


@params(api='egl', prms=['dpy', 'layer', 'attribute', 'value'])
def eglOutputLayerAttribEXT(dpy, layer, attribute):
	pass


@params(api='egl', prms=['dpy', 'layer', 'attribute', 'value'])
def eglQueryOutputLayerAttribEXT(dpy, layer, attribute):
	pass


@params(api='egl', prms=['dpy', 'layer', 'name'])
def eglQueryOutputLayerStringEXT(dpy, layer, name):
	pass


@params(api='egl', prms=['dpy', 'port', 'attribute', 'value'])
def eglOutputPortAttribEXT(dpy, port, attribute):
	pass


@params(api='egl', prms=['dpy', 'port', 'attribute', 'value'])
def eglQueryOutputPortAttribEXT(dpy, port, attribute):
	pass


@params(api='egl', prms=['dpy', 'port', 'name'])
def eglQueryOutputPortStringEXT(dpy, port, name):
	pass


