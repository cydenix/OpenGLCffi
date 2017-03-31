@params('mode', 'id', 'stream', api='gl')
def glDrawTransformFeedbackStream(mode, id, stream):
	pass


@params('target', 'index', 'id', api='gl')
def glBeginQueryIndexed(target, index, id):
	pass


@params('target', 'index', api='gl')
def glEndQueryIndexed(target, index):
	pass


@params('target', 'index', 'pname', 'params', api='gl')
def glGetQueryIndexediv(target, index, pname, params):
	pass


