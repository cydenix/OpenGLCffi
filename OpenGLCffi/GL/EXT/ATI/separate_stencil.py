from OpenGLCffi.GL import params
@params(api='gl', prms=['face', 'sfail', 'dpfail', 'dppass'])
def glStencilOpSeparateATI(face, sfail, dpfail, dppass):
	pass


@params(api='gl', prms=['frontfunc', 'backfunc', 'ref', 'mask'])
def glStencilFuncSeparateATI(frontfunc, backfunc, ref, mask):
	pass


