@params('dpy', 'attrib_list', 'layers', 'max_layers', 'num_layers', api='egl')
def eglGetOutputLayersEXT(dpy, attrib_list, layers, max_layers, num_layers):
	pass


@params('dpy', 'attrib_list', 'ports', 'max_ports', 'num_ports', api='egl')
def eglGetOutputPortsEXT(dpy, attrib_list, ports, max_ports, num_ports):
	pass


@params('dpy', 'layer', 'attribute', 'value', api='egl')
def eglOutputLayerAttribEXT(dpy, layer, attribute):
	pass


@params('dpy', 'layer', 'attribute', 'value', api='egl')
def eglQueryOutputLayerAttribEXT(dpy, layer, attribute):
	pass


@params('dpy', 'layer', 'name', api='egl')
def eglQueryOutputLayerStringEXT(dpy, layer, name):
	pass


@params('dpy', 'port', 'attribute', 'value', api='egl')
def eglOutputPortAttribEXT(dpy, port, attribute):
	pass


@params('dpy', 'port', 'attribute', 'value', api='egl')
def eglQueryOutputPortAttribEXT(dpy, port, attribute):
	pass


@params('dpy', 'port', 'name', api='egl')
def eglQueryOutputPortStringEXT(dpy, port, name):
	pass


