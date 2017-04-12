from OpenGLCffi.GL import params
@params(api='gl', prms=['numGroups', 'groupsSize', 'groups'])
def glGetPerfMonitorGroupsAMD(numGroups, groupsSize, groups):
	pass


@params(api='gl', prms=['group', 'numCounters', 'maxActiveCounters', 'counterSize', 'counters'])
def glGetPerfMonitorCountersAMD(group, numCounters, maxActiveCounters, counterSize, counters):
	pass


@params(api='gl', prms=['group', 'bufSize', 'length', 'groupString'])
def glGetPerfMonitorGroupStringAMD(group, bufSize, length, groupString):
	pass


@params(api='gl', prms=['group', 'counter', 'bufSize', 'length', 'counterString'])
def glGetPerfMonitorCounterStringAMD(group, counter, bufSize, length, counterString):
	pass


@params(api='gl', prms=['group', 'counter', 'pname', 'data'])
def glGetPerfMonitorCounterInfoAMD(group, counter, pname, data):
	pass


@params(api='gl', prms=['n', 'monitors'])
def glGenPerfMonitorsAMD(n, monitors):
	pass


@params(api='gl', prms=['n', 'monitors'])
def glDeletePerfMonitorsAMD(n, monitors):
	pass


@params(api='gl', prms=['monitor', 'enable', 'group', 'numCounters', 'counterList'])
def glSelectPerfMonitorCountersAMD(monitor, enable, group, numCounters, counterList):
	pass


@params(api='gl', prms=['monitor'])
def glBeginPerfMonitorAMD(monitor):
	pass


@params(api='gl', prms=['monitor'])
def glEndPerfMonitorAMD(monitor):
	pass


@params(api='gl', prms=['monitor', 'pname', 'dataSize', 'data', 'bytesWritten'])
def glGetPerfMonitorCounterDataAMD(monitor, pname, dataSize, data, bytesWritten):
	pass


