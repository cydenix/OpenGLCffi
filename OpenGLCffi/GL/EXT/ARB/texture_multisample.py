from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations'])
def glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations'])
def glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params(api='gl', prms=['pname', 'index', 'val'])
def glGetMultisamplefv(pname, index, val):
	pass


@params(api='gl', prms=['maskNumber', 'mask'])
def glSampleMaski(maskNumber, mask):
	pass


