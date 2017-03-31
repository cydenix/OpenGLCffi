@params('n', 'textures', 'residences', api='gl')
def glAreTexturesResidentEXT(n, textures, residences):
	pass


@params('target', 'texture', api='gl')
def glBindTextureEXT(target, texture):
	pass


@params('n', 'textures', api='gl')
def glDeleteTexturesEXT(n, textures):
	pass


@params('n', 'textures', api='gl')
def glGenTexturesEXT(n, textures):
	pass


@params('texture', api='gl')
def glIsTextureEXT(texture):
	pass


@params('n', 'textures', 'priorities', api='gl')
def glPrioritizeTexturesEXT(n, textures, priorities):
	pass


