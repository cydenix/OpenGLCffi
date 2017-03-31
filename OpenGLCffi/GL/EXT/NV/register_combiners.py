@params('pname', 'params', api='gl')
def glCombinerParameterfvNV(pname, params):
	pass


@params('pname', 'param', api='gl')
def glCombinerParameterfNV(pname, param):
	pass


@params('pname', 'params', api='gl')
def glCombinerParameterivNV(pname, params):
	pass


@params('pname', 'param', api='gl')
def glCombinerParameteriNV(pname, param):
	pass


@params('stage', 'portion', 'variable', 'input', 'mapping', 'componentUsage', api='gl')
def glCombinerInputNV(stage, portion, variable, input, mapping, componentUsage):
	pass


@params('stage', 'portion', 'abOutput', 'cdOutput', 'sumOutput', 'scale', 'bias', 'abDotProduct', 'cdDotProduct', 'muxSum', api='gl')
def glCombinerOutputNV(stage, portion, abOutput, cdOutput, sumOutput, scale, bias, abDotProduct, cdDotProduct, muxSum):
	pass


@params('variable', 'input', 'mapping', 'componentUsage', api='gl')
def glFinalCombinerInputNV(variable, input, mapping, componentUsage):
	pass


@params('stage', 'portion', 'variable', 'pname', 'params', api='gl')
def glGetCombinerInputParameterfvNV(stage, portion, variable, pname, params):
	pass


@params('stage', 'portion', 'variable', 'pname', 'params', api='gl')
def glGetCombinerInputParameterivNV(stage, portion, variable, pname, params):
	pass


@params('stage', 'portion', 'pname', 'params', api='gl')
def glGetCombinerOutputParameterfvNV(stage, portion, pname, params):
	pass


@params('stage', 'portion', 'pname', 'params', api='gl')
def glGetCombinerOutputParameterivNV(stage, portion, pname, params):
	pass


@params('variable', 'pname', 'params', api='gl')
def glGetFinalCombinerInputParameterfvNV(variable, pname, params):
	pass


@params('variable', 'pname', 'params', api='gl')
def glGetFinalCombinerInputParameterivNV(variable, pname, params):
	pass


