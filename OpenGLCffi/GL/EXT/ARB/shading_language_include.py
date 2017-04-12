from OpenGLCffi.GL import params
@params(api='gl', prms=['type', 'namelen', 'name', 'stringlen', 'string'])
def glNamedStringARB(type, namelen, name, stringlen, string):
	pass


@params(api='gl', prms=['namelen', 'name'])
def glDeleteNamedStringARB(namelen, name):
	pass


@params(api='gl', prms=['shader', 'count', 'constpath', 'length'])
def glCompileShaderIncludeARB(shader, count, constpath, length):
	pass


@params(api='gl', prms=['namelen', 'name'])
def glIsNamedStringARB(namelen, name):
	pass


@params(api='gl', prms=['namelen', 'name', 'bufSize', 'stringlen', 'string'])
def glGetNamedStringARB(namelen, name, bufSize, stringlen, string):
	pass


@params(api='gl', prms=['namelen', 'name', 'pname', 'params'])
def glGetNamedStringivARB(namelen, name, pname, params):
	pass


