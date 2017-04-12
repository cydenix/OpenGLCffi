from OpenGLCffi.GL import params
@params(api='gl', prms=['zNear', 'zFar'])
def glDepthRangedNV(zNear, zFar):
	pass


@params(api='gl', prms=['depth'])
def glClearDepthdNV(depth):
	pass


@params(api='gl', prms=['zmin', 'zmax'])
def glDepthBoundsdNV(zmin, zmax):
	pass


