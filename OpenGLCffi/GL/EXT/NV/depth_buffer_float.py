from OpenGLCffi.GL import params
@params('zNear', 'zFar', api='gl')
def glDepthRangedNV(zNear, zFar):
	pass


@params('depth', api='gl')
def glClearDepthdNV(depth):
	pass


@params('zmin', 'zmax', api='gl')
def glDepthBoundsdNV(zmin, zmax):
	pass


