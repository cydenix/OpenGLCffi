from OpenGLCffi.GL import params
@params('target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations', api='gl')
def glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations', api='gl')
def glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('pname', 'index', 'val', api='gl')
def glGetMultisamplefv(pname, index, val):
	pass


@params('maskNumber', 'mask', api='gl')
def glSampleMaski(maskNumber, mask):
	pass


