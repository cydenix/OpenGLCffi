from OpenGLCffi.GL import params
@params(api='gl', prms=['n', 'textures', 'residences'])
def glAreTexturesResidentEXT(n, textures, residences):
	pass


@params(api='gl', prms=['target', 'texture'])
def glBindTextureEXT(target, texture):
	pass


@params(api='gl', prms=['n', 'textures'])
def glDeleteTexturesEXT(n, textures):
	pass


@params(api='gl', prms=['n', 'textures'])
def glGenTexturesEXT(n, textures):
	pass


@params(api='gl', prms=['texture'])
def glIsTextureEXT(texture):
	pass


@params(api='gl', prms=['n', 'textures', 'priorities'])
def glPrioritizeTexturesEXT(n, textures, priorities):
	pass


