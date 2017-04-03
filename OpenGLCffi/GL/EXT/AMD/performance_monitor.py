from OpenGLCffi.GL import params
@params('numGroups', 'groupsSize', 'groups', api='gl')
def glGetPerfMonitorGroupsAMD(numGroups, groupsSize, groups):
	pass


@params('group', 'numCounters', 'maxActiveCounters', 'counterSize', 'counters', api='gl')
def glGetPerfMonitorCountersAMD(group, numCounters, maxActiveCounters, counterSize, counters):
	pass


@params('group', 'bufSize', 'length', 'groupString', api='gl')
def glGetPerfMonitorGroupStringAMD(group, bufSize, length, groupString):
	pass


@params('group', 'counter', 'bufSize', 'length', 'counterString', api='gl')
def glGetPerfMonitorCounterStringAMD(group, counter, bufSize, length, counterString):
	pass


@params('group', 'counter', 'pname', 'data', api='gl')
def glGetPerfMonitorCounterInfoAMD(group, counter, pname, data):
	pass


@params('n', 'monitors', api='gl')
def glGenPerfMonitorsAMD(n, monitors):
	pass


@params('n', 'monitors', api='gl')
def glDeletePerfMonitorsAMD(n, monitors):
	pass


@params('monitor', 'enable', 'group', 'numCounters', 'counterList', api='gl')
def glSelectPerfMonitorCountersAMD(monitor, enable, group, numCounters, counterList):
	pass


@params('monitor', api='gl')
def glBeginPerfMonitorAMD(monitor):
	pass


@params('monitor', api='gl')
def glEndPerfMonitorAMD(monitor):
	pass


@params('monitor', 'pname', 'dataSize', 'data', 'bytesWritten', api='gl')
def glGetPerfMonitorCounterDataAMD(monitor, pname, dataSize, data, bytesWritten):
	pass


