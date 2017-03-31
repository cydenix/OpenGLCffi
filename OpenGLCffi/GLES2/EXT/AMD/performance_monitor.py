@params('numGroups', 'groupsSize', 'groups', api='gles2')
def glGetPerfMonitorGroupsAMD(numGroups, groupsSize, groups):
	pass


@params('group', 'numCounters', 'maxActiveCounters', 'counterSize', 'counters', api='gles2')
def glGetPerfMonitorCountersAMD(group, numCounters, maxActiveCounters, counterSize, counters):
	pass


@params('group', 'bufSize', 'length', 'groupString', api='gles2')
def glGetPerfMonitorGroupStringAMD(group, bufSize, length, groupString):
	pass


@params('group', 'counter', 'bufSize', 'length', 'counterString', api='gles2')
def glGetPerfMonitorCounterStringAMD(group, counter, bufSize, length, counterString):
	pass


@params('group', 'counter', 'pname', 'data', api='gles2')
def glGetPerfMonitorCounterInfoAMD(group, counter, pname):
	pass


@params('n', 'monitors', api='gles2')
def glGenPerfMonitorsAMD(n, monitors):
	pass


@params('n', 'monitors', api='gles2')
def glDeletePerfMonitorsAMD(n, monitors):
	pass


@params('monitor', 'enable', 'group', 'numCounters', 'counterList', api='gles2')
def glSelectPerfMonitorCountersAMD(monitor, enable, group, numCounters, counterList):
	pass


@params('monitor', api='gles2')
def glBeginPerfMonitorAMD(monitor):
	pass


@params('monitor', api='gles2')
def glEndPerfMonitorAMD(monitor):
	pass


@params('monitor', 'pname', 'dataSize', 'data', 'bytesWritten', api='gles2')
def glGetPerfMonitorCounterDataAMD(monitor, pname, dataSize, bytesWritten):
	pass


