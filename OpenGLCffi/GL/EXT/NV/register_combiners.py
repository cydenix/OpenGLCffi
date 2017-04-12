from OpenGLCffi.GL import params
@params(api='gl', prms=['pname', 'params'])
def glCombinerParameterfvNV(pname, params):
	pass


@params(api='gl', prms=['pname', 'param'])
def glCombinerParameterfNV(pname, param):
	pass


@params(api='gl', prms=['pname', 'params'])
def glCombinerParameterivNV(pname, params):
	pass


@params(api='gl', prms=['pname', 'param'])
def glCombinerParameteriNV(pname, param):
	pass


@params(api='gl', prms=['stage', 'portion', 'variable', 'input', 'mapping', 'componentUsage'])
def glCombinerInputNV(stage, portion, variable, input, mapping, componentUsage):
	pass


@params(api='gl', prms=['stage', 'portion', 'abOutput', 'cdOutput', 'sumOutput', 'scale', 'bias', 'abDotProduct', 'cdDotProduct', 'muxSum'])
def glCombinerOutputNV(stage, portion, abOutput, cdOutput, sumOutput, scale, bias, abDotProduct, cdDotProduct, muxSum):
	pass


@params(api='gl', prms=['variable', 'input', 'mapping', 'componentUsage'])
def glFinalCombinerInputNV(variable, input, mapping, componentUsage):
	pass


@params(api='gl', prms=['stage', 'portion', 'variable', 'pname', 'params'])
def glGetCombinerInputParameterfvNV(stage, portion, variable, pname, params):
	pass


@params(api='gl', prms=['stage', 'portion', 'variable', 'pname', 'params'])
def glGetCombinerInputParameterivNV(stage, portion, variable, pname, params):
	pass


@params(api='gl', prms=['stage', 'portion', 'pname', 'params'])
def glGetCombinerOutputParameterfvNV(stage, portion, pname, params):
	pass


@params(api='gl', prms=['stage', 'portion', 'pname', 'params'])
def glGetCombinerOutputParameterivNV(stage, portion, pname, params):
	pass


@params(api='gl', prms=['variable', 'pname', 'params'])
def glGetFinalCombinerInputParameterfvNV(variable, pname, params):
	pass


@params(api='gl', prms=['variable', 'pname', 'params'])
def glGetFinalCombinerInputParameterivNV(variable, pname, params):
	pass


