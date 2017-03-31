@params('type', 'namelen', 'name', 'stringlen', 'string', api='gl')
def glNamedStringARB(type, namelen, name, stringlen, string):
	pass


@params('namelen', 'name', api='gl')
def glDeleteNamedStringARB(namelen, name):
	pass


@params('shader', 'count', 'constpath', 'length', api='gl')
def glCompileShaderIncludeARB(shader, count, constpath, length):
	pass


@params('namelen', 'name', api='gl')
def glIsNamedStringARB(namelen, name):
	pass


@params('namelen', 'name', 'bufSize', 'stringlen', 'string', api='gl')
def glGetNamedStringARB(namelen, name, bufSize, stringlen, string):
	pass


@params('namelen', 'name', 'pname', 'params', api='gl')
def glGetNamedStringivARB(namelen, name, pname, params):
	pass


