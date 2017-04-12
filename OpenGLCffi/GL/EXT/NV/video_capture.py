from OpenGLCffi.GL import params
@params(api='gl', prms=['video_capture_slot'])
def glBeginVideoCaptureNV(video_capture_slot):
	pass


@params(api='gl', prms=['video_capture_slot', 'stream', 'frame_region', 'offset'])
def glBindVideoCaptureStreamBufferNV(video_capture_slot, stream, frame_region, offset):
	pass


@params(api='gl', prms=['video_capture_slot', 'stream', 'frame_region', 'target', 'texture'])
def glBindVideoCaptureStreamTextureNV(video_capture_slot, stream, frame_region, target, texture):
	pass


@params(api='gl', prms=['video_capture_slot'])
def glEndVideoCaptureNV(video_capture_slot):
	pass


@params(api='gl', prms=['video_capture_slot', 'pname', 'params'])
def glGetVideoCaptureivNV(video_capture_slot, pname, params):
	pass


@params(api='gl', prms=['video_capture_slot', 'stream', 'pname', 'params'])
def glGetVideoCaptureStreamivNV(video_capture_slot, stream, pname, params):
	pass


@params(api='gl', prms=['video_capture_slot', 'stream', 'pname', 'params'])
def glGetVideoCaptureStreamfvNV(video_capture_slot, stream, pname, params):
	pass


@params(api='gl', prms=['video_capture_slot', 'stream', 'pname', 'params'])
def glGetVideoCaptureStreamdvNV(video_capture_slot, stream, pname, params):
	pass


@params(api='gl', prms=['video_capture_slot', 'sequence_num', 'capture_time'])
def glVideoCaptureNV(video_capture_slot, sequence_num, capture_time):
	pass


@params(api='gl', prms=['video_capture_slot', 'stream', 'pname', 'params'])
def glVideoCaptureStreamParameterivNV(video_capture_slot, stream, pname, params):
	pass


@params(api='gl', prms=['video_capture_slot', 'stream', 'pname', 'params'])
def glVideoCaptureStreamParameterfvNV(video_capture_slot, stream, pname, params):
	pass


@params(api='gl', prms=['video_capture_slot', 'stream', 'pname', 'params'])
def glVideoCaptureStreamParameterdvNV(video_capture_slot, stream, pname, params):
	pass


