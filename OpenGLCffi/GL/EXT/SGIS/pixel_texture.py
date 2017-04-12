from OpenGLCffi.GL import params
@params(api='gl', prms=['pname', 'param'])
def glPixelTexGenParameteriSGIS(pname, param):
	pass


@params(api='gl', prms=['pname', 'params'])
def glPixelTexGenParameterivSGIS(pname, params):
	pass


@params(api='gl', prms=['pname', 'param'])
def glPixelTexGenParameterfSGIS(pname, param):
	pass


@params(api='gl', prms=['pname', 'params'])
def glPixelTexGenParameterfvSGIS(pname, params):
	pass


@params(api='gl', prms=['pname', 'params'])
def glGetPixelTexGenParameterivSGIS(pname, params):
	pass


@params(api='gl', prms=['pname', 'params'])
def glGetPixelTexGenParameterfvSGIS(pname, params):
	pass


