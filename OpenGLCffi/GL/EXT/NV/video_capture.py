@params('video_capture_slot', api='gl')
def glBeginVideoCaptureNV(video_capture_slot):
	pass


@params('video_capture_slot', 'stream', 'frame_region', 'offset', api='gl')
def glBindVideoCaptureStreamBufferNV(video_capture_slot, stream, frame_region, offset):
	pass


@params('video_capture_slot', 'stream', 'frame_region', 'target', 'texture', api='gl')
def glBindVideoCaptureStreamTextureNV(video_capture_slot, stream, frame_region, target, texture):
	pass


@params('video_capture_slot', api='gl')
def glEndVideoCaptureNV(video_capture_slot):
	pass


@params('video_capture_slot', 'pname', 'params', api='gl')
def glGetVideoCaptureivNV(video_capture_slot, pname, params):
	pass


@params('video_capture_slot', 'stream', 'pname', 'params', api='gl')
def glGetVideoCaptureStreamivNV(video_capture_slot, stream, pname, params):
	pass


@params('video_capture_slot', 'stream', 'pname', 'params', api='gl')
def glGetVideoCaptureStreamfvNV(video_capture_slot, stream, pname, params):
	pass


@params('video_capture_slot', 'stream', 'pname', 'params', api='gl')
def glGetVideoCaptureStreamdvNV(video_capture_slot, stream, pname, params):
	pass


@params('video_capture_slot', 'sequence_num', 'capture_time', api='gl')
def glVideoCaptureNV(video_capture_slot, sequence_num, capture_time):
	pass


@params('video_capture_slot', 'stream', 'pname', 'params', api='gl')
def glVideoCaptureStreamParameterivNV(video_capture_slot, stream, pname, params):
	pass


@params('video_capture_slot', 'stream', 'pname', 'params', api='gl')
def glVideoCaptureStreamParameterfvNV(video_capture_slot, stream, pname, params):
	pass


@params('video_capture_slot', 'stream', 'pname', 'params', api='gl')
def glVideoCaptureStreamParameterdvNV(video_capture_slot, stream, pname, params):
	pass


