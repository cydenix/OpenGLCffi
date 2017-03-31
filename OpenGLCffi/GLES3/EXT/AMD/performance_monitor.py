@params('numGroups', 'groupsSize', 'groups', api='gles3')
def glGetPerfMonitorGroupsAMD(numGroups, groupsSize, groups):
	pass


@params('group', 'numCounters', 'maxActiveCounters', 'counterSize', 'counters', api='gles3')
def glGetPerfMonitorCountersAMD(group, numCounters, maxActiveCounters, counterSize, counters):
	pass


@params('group', 'bufSize', 'length', 'groupString', api='gles3')
def glGetPerfMonitorGroupStringAMD(group, bufSize, length, groupString):
	pass


@params('group', 'counter', 'bufSize', 'length', 'counterString', api='gles3')
def glGetPerfMonitorCounterStringAMD(group, counter, bufSize, length, counterString):
	pass


@params('group', 'counter', 'pname', 'data', api='gles3')
def glGetPerfMonitorCounterInfoAMD(group, counter, pname):
	pass


@params('n', 'monitors', api='gles3')
def glGenPerfMonitorsAMD(n, monitors):
	pass


@params('n', 'monitors', api='gles3')
def glDeletePerfMonitorsAMD(n, monitors):
	pass


@params('monitor', 'enable', 'group', 'numCounters', 'counterList', api='gles3')
def glSelectPerfMonitorCountersAMD(monitor, enable, group, numCounters, counterList):
	pass


@params('monitor', api='gles3')
def glBeginPerfMonitorAMD(monitor):
	pass


@params('monitor', api='gles3')
def glEndPerfMonitorAMD(monitor):
	pass


@params('monitor', 'pname', 'dataSize', 'data', 'bytesWritten', api='gles3')
def glGetPerfMonitorCounterDataAMD(monitor, pname, dataSize, bytesWritten):
	pass


