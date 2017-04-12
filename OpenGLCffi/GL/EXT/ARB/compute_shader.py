from OpenGLCffi.GL import params
@params(api='gl', prms=['num_groups_x', 'num_groups_y', 'num_groups_z'])
def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
	pass


@params(api='gl', prms=['indirect'])
def glDispatchComputeIndirect(indirect):
	pass


