from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['numGroups', 'groupsSize', 'groups'])
def glGetPerfMonitorGroupsAMD(numGroups, groupsSize, groups):
	pass


@params(api='gles3', prms=['group', 'numCounters', 'maxActiveCounters', 'counterSize', 'counters'])
def glGetPerfMonitorCountersAMD(group, numCounters, maxActiveCounters, counterSize, counters):
	pass


@params(api='gles3', prms=['group', 'bufSize', 'length', 'groupString'])
def glGetPerfMonitorGroupStringAMD(group, bufSize, length, groupString):
	pass


@params(api='gles3', prms=['group', 'counter', 'bufSize', 'length', 'counterString'])
def glGetPerfMonitorCounterStringAMD(group, counter, bufSize, length, counterString):
	pass


@params(api='gles3', prms=['group', 'counter', 'pname', 'data'])
def glGetPerfMonitorCounterInfoAMD(group, counter, pname):
	pass


@params(api='gles3', prms=['n', 'monitors'])
def glGenPerfMonitorsAMD(n, monitors):
	pass


@params(api='gles3', prms=['n', 'monitors'])
def glDeletePerfMonitorsAMD(n, monitors):
	pass


@params(api='gles3', prms=['monitor', 'enable', 'group', 'numCounters', 'counterList'])
def glSelectPerfMonitorCountersAMD(monitor, enable, group, numCounters, counterList):
	pass


@params(api='gles3', prms=['monitor'])
def glBeginPerfMonitorAMD(monitor):
	pass


@params(api='gles3', prms=['monitor'])
def glEndPerfMonitorAMD(monitor):
	pass


@params(api='gles3', prms=['monitor', 'pname', 'dataSize', 'data', 'bytesWritten'])
def glGetPerfMonitorCounterDataAMD(monitor, pname, dataSize, bytesWritten):
	pass


