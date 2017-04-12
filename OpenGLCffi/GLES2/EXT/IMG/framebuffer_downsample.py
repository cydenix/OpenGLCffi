from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'attachment', 'textarget', 'texture', 'level', 'xscale', 'yscale'])
def glFramebufferTexture2DDownsampleIMG(target, attachment, textarget, texture, level, xscale, yscale):
	pass


@params(api='gles2', prms=['target', 'attachment', 'texture', 'level', 'layer', 'xscale', 'yscale'])
def glFramebufferTextureLayerDownsampleIMG(target, attachment, texture, level, layer, xscale, yscale):
	pass


