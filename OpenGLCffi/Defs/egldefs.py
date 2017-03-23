
DEF = '''
typedef int32_t                khronos_int32_t;
typedef uint32_t               khronos_uint32_t;
typedef int64_t                khronos_int64_t;
typedef uint64_t               khronos_uint64_t;
typedef signed   char          khronos_int8_t;
typedef unsigned char          khronos_uint8_t;
typedef signed   short int     khronos_int16_t;
typedef unsigned short int     khronos_uint16_t;
typedef signed   long  int     khronos_intptr_t;
typedef unsigned long  int     khronos_uintptr_t;
typedef signed   long  int     khronos_ssize_t;
typedef unsigned long  int     khronos_usize_t;
typedef          float         khronos_float_t;
typedef khronos_uint64_t       khronos_utime_nanoseconds_t;
typedef khronos_int64_t        khronos_stime_nanoseconds_t;
typedef ... Display;
typedef ... XExtData;
typedef int Bool;
typedef unsigned long Font;
typedef unsigned long Screen;
typedef unsigned long Status;
typedef unsigned long Window;
typedef unsigned long Pixmap;
typedef unsigned long Colormap;
typedef unsigned long VisualID;
typedef unsigned long XID;

typedef struct {
  XExtData *ext_data;
  VisualID visualid;
  int class;
  unsigned long red_mask, green_mask, blue_mask;
  int bits_per_rgb;
  int map_entries;
} Visual;

typedef struct {
  Visual *visual;
  VisualID visualid;
  int screen;
  int depth;
  int class;
  unsigned long red_mask;
  unsigned long green_mask;
  unsigned long blue_mask;
  int colormap_size;
  int bits_per_rgb;
} XVisualInfo;


extern Display *XOpenDisplay(const char*);


xcb_connection_t *XGetXCBConnection(Display *dpy);
enum XEventQueueOwner { XlibOwnsEventQueue = 0, XCBOwnsEventQueue };
void XSetEventQueueOwner(Display *dpy, enum XEventQueueOwner owner);
typedef Display *EGLNativeDisplayType;
typedef Pixmap   EGLNativePixmapType;
typedef Window   EGLNativeWindowType;
typedef khronos_int32_t EGLint;
typedef unsigned int EGLBoolean;
typedef unsigned int EGLenum;
typedef intptr_t EGLAttribKHR;
typedef intptr_t EGLAttrib;
typedef void *EGLClientBuffer;
typedef void *EGLConfig;
typedef void *EGLContext;
typedef void *EGLDeviceEXT;
typedef void *EGLDisplay;
typedef void *EGLImage;
typedef void *EGLImageKHR;
typedef void *EGLLabelKHR;
typedef void *EGLObjectKHR;
typedef void *EGLOutputLayerEXT;
typedef void *EGLOutputPortEXT;
typedef void *EGLStreamKHR;
typedef void *EGLSurface;
typedef void *EGLSync;
typedef void *EGLSyncKHR;
typedef void *EGLSyncNV;
typedef void (*__eglMustCastToProperFunctionPointerType)(void);
typedef khronos_utime_nanoseconds_t EGLTimeKHR;
typedef khronos_utime_nanoseconds_t EGLTime;
typedef khronos_utime_nanoseconds_t EGLTimeNV;
typedef khronos_utime_nanoseconds_t EGLuint64NV;
typedef khronos_uint64_t EGLuint64KHR;
typedef khronos_stime_nanoseconds_t EGLnsecsANDROID;
typedef int EGLNativeFileDescriptorKHR;
typedef khronos_ssize_t EGLsizeiANDROID;
typedef void (*EGLSetBlobFuncANDROID) (const void *key, EGLsizeiANDROID keySize, const void *value, EGLsizeiANDROID valueSize);
typedef EGLsizeiANDROID (*EGLGetBlobFuncANDROID) (const void *key, EGLsizeiANDROID keySize, void *value, EGLsizeiANDROID valueSize);
struct EGLClientPixmapHI {
    void  *pData;
    EGLint iWidth;
    EGLint iHeight;
    EGLint iStride;
};
typedef void (EGLDEBUGPROCKHR)(EGLenum error,const char *command,EGLint messageType,EGLLabelKHR threadLabel,EGLLabelKHR objectLabel,const char* message);

EGLint  eglDupNativeFenceFDANDROID(EGLDisplay dpy, EGLSyncKHR sync);
EGLBoolean  eglStreamAttribKHR(EGLDisplay dpy, EGLStreamKHR stream, EGLenum attribute, EGLint value);
EGLBoolean  eglQueryStreamMetadataNV(EGLDisplay dpy, EGLStreamKHR stream, EGLenum name, EGLint n, EGLint offset, EGLint size, void *data);
const char * eglQueryOutputLayerStringEXT(EGLDisplay dpy, EGLOutputLayerEXT layer, EGLint name);
EGLBoolean  eglExportDRMImageMESA(EGLDisplay dpy, EGLImageKHR image, EGLint *name, EGLint *handle, EGLint *stride);
EGLSurface  eglGetCurrentSurface(EGLint readdraw);
EGLBoolean  eglPostSubBufferNV(EGLDisplay dpy, EGLSurface surface, EGLint x, EGLint y, EGLint width, EGLint height);
EGLBoolean  eglBindTexImage(EGLDisplay dpy, EGLSurface surface, EGLint buffer);
EGLBoolean  eglSetDamageRegionKHR(EGLDisplay dpy, EGLSurface surface, EGLint *rects, EGLint n_rects);
EGLint  eglDebugMessageControlKHR(EGLDEBUGPROCKHR callback, const EGLAttrib *attrib_list);
EGLBoolean  eglExportDMABUFImageQueryMESA(EGLDisplay dpy, EGLImageKHR image, int *fourcc, int *num_planes, EGLuint64KHR *modifiers);
EGLint  eglGetError();
EGLBoolean  eglSwapBuffersWithDamageKHR(EGLDisplay dpy, EGLSurface surface, EGLint *rects, EGLint n_rects);
EGLContext  eglCreateContext(EGLDisplay dpy, EGLConfig config, EGLContext share_context, const EGLint *attrib_list);
EGLBoolean  eglWaitGL();
EGLint  eglClientWaitSyncKHR(EGLDisplay dpy, EGLSyncKHR sync, EGLint flags, EGLTimeKHR timeout);
EGLint  eglClientWaitSyncNV(EGLSyncNV sync, EGLint flags, EGLTimeNV timeout);
EGLBoolean  eglBindAPI(EGLenum api);
EGLDisplay  eglGetPlatformDisplayEXT(EGLenum platform, void *native_display, const EGLint *attrib_list);
EGLBoolean  eglQueryDisplayAttribNV(EGLDisplay dpy, EGLint attribute, EGLAttrib *value);
EGLBoolean  eglReleaseThread();
EGLBoolean  eglOutputPortAttribEXT(EGLDisplay dpy, EGLOutputPortEXT port, EGLint attribute, EGLAttrib value);
EGLBoolean  eglQueryDisplayAttribEXT(EGLDisplay dpy, EGLint attribute, EGLAttrib *value);
EGLBoolean  eglQuerySurfacePointerANGLE(EGLDisplay dpy, EGLSurface surface, EGLint attribute, void **value);
EGLBoolean  eglTerminate(EGLDisplay dpy);
EGLBoolean  eglQueryDevicesEXT(EGLint max_devices, EGLDeviceEXT *devices, EGLint *num_devices);
EGLImage  eglCreateImage(EGLDisplay dpy, EGLContext ctx, EGLenum target, EGLClientBuffer buffer, const EGLAttrib *attrib_list);
EGLNativeFileDescriptorKHR  eglGetStreamFileDescriptorKHR(EGLDisplay dpy, EGLStreamKHR stream);
EGLBoolean  eglQueryDmaBufFormatsEXT(EGLDisplay dpy, EGLint max_formats, EGLint *formats, EGLint *num_formats);
EGLSyncKHR  eglCreateSync64KHR(EGLDisplay dpy, EGLenum type, const EGLAttribKHR *attrib_list);
EGLBoolean  eglSurfaceAttrib(EGLDisplay dpy, EGLSurface surface, EGLint attribute, EGLint value);
EGLBoolean  eglSwapInterval(EGLDisplay dpy, EGLint interval);
EGLSyncKHR  eglCreateStreamSyncNV(EGLDisplay dpy, EGLStreamKHR stream, EGLenum type, const EGLint *attrib_list);
const char * eglQueryDeviceStringEXT(EGLDeviceEXT device, EGLint name);
EGLBoolean  eglGetSyncAttrib(EGLDisplay dpy, EGLSync sync, EGLint attribute, EGLAttrib *value);
EGLBoolean  eglQueryStreamAttribKHR(EGLDisplay dpy, EGLStreamKHR stream, EGLenum attribute, EGLAttrib *value);
EGLSurface  eglCreatePlatformPixmapSurfaceEXT(EGLDisplay dpy, EGLConfig config, void *native_pixmap, const EGLint *attrib_list);
EGLSurface  eglCreatePlatformWindowSurface(EGLDisplay dpy, EGLConfig config, void *native_window, const EGLAttrib *attrib_list);
EGLContext  eglGetCurrentContext();
const char * eglQueryString(EGLDisplay dpy, EGLint name);
EGLBoolean  eglWaitSync(EGLDisplay dpy, EGLSync sync, EGLint flags);
EGLuint64NV  eglGetSystemTimeNV();
const char * eglQueryOutputPortStringEXT(EGLDisplay dpy, EGLOutputPortEXT port, EGLint name);
EGLBoolean  eglQueryDebugKHR(EGLint attribute, EGLAttrib *value);
EGLBoolean  eglWaitClient();
__eglMustCastToProperFunctionPointerType  eglGetProcAddress(const char *procname);
EGLuint64NV  eglGetSystemTimeFrequencyNV();
EGLBoolean  eglQueryStreamTimeKHR(EGLDisplay dpy, EGLStreamKHR stream, EGLenum attribute, EGLTimeKHR *value);
EGLSurface  eglCreateStreamProducerSurfaceKHR(EGLDisplay dpy, EGLConfig config, EGLStreamKHR stream, const EGLint *attrib_list);
EGLBoolean  eglExportDMABUFImageMESA(EGLDisplay dpy, EGLImageKHR image, int *fds, EGLint *strides, EGLint *offsets);
EGLBoolean  eglGetSyncAttribKHR(EGLDisplay dpy, EGLSyncKHR sync, EGLint attribute, EGLint *value);
EGLStreamKHR  eglCreateStreamFromFileDescriptorKHR(EGLDisplay dpy, EGLNativeFileDescriptorKHR file_descriptor);
EGLBoolean  eglSignalSyncNV(EGLSyncNV sync, EGLenum mode);
EGLBoolean  eglQueryNativeWindowNV(EGLDisplay dpy, EGLSurface surf, EGLNativeWindowType *window);
EGLSyncKHR  eglCreateSyncKHR(EGLDisplay dpy, EGLenum type, const EGLint *attrib_list);
EGLStreamKHR  eglCreateStreamKHR(EGLDisplay dpy, const EGLint *attrib_list);
EGLBoolean  eglInitialize(EGLDisplay dpy, EGLint *major, EGLint *minor);
EGLBoolean  eglGetSyncAttribNV(EGLSyncNV sync, EGLint attribute, EGLint *value);
EGLDisplay  eglGetPlatformDisplay(EGLenum platform, void *native_display, const EGLAttrib *attrib_list);
EGLImageKHR  eglCreateImageKHR(EGLDisplay dpy, EGLContext ctx, EGLenum target, EGLClientBuffer buffer, const EGLint *attrib_list);
EGLBoolean  eglQueryContext(EGLDisplay dpy, EGLContext ctx, EGLint attribute, EGLint *value);
EGLBoolean  eglQueryDeviceAttribEXT(EGLDeviceEXT device, EGLint attribute, EGLAttrib *value);
EGLBoolean  eglStreamConsumerReleaseKHR(EGLDisplay dpy, EGLStreamKHR stream);
EGLint  eglLabelObjectKHR(EGLDisplay display, EGLenum objectType, EGLObjectKHR object, EGLLabelKHR label);
EGLSurface  eglCreatePbufferFromClientBuffer(EGLDisplay dpy, EGLenum buftype, EGLClientBuffer buffer, EGLConfig config, const EGLint *attrib_list);
EGLBoolean  eglChooseConfig(EGLDisplay dpy, const EGLint *attrib_list, EGLConfig *configs, EGLint config_size, EGLint *num_config);
EGLBoolean  eglWaitNative(EGLint engine);
EGLBoolean  eglQuerySurface(EGLDisplay dpy, EGLSurface surface, EGLint attribute, EGLint *value);
EGLSurface  eglCreatePlatformPixmapSurface(EGLDisplay dpy, EGLConfig config, void *native_pixmap, const EGLAttrib *attrib_list);
EGLSyncNV  eglCreateFenceSyncNV(EGLDisplay dpy, EGLenum condition, const EGLint *attrib_list);
EGLBoolean  eglGetConfigAttrib(EGLDisplay dpy, EGLConfig config, EGLint attribute, EGLint *value);
EGLBoolean  eglLockSurfaceKHR(EGLDisplay dpy, EGLSurface surface, const EGLint *attrib_list);
EGLBoolean  eglSetStreamAttribKHR(EGLDisplay dpy, EGLStreamKHR stream, EGLenum attribute, EGLAttrib value);
EGLBoolean  eglResetStreamNV(EGLDisplay dpy, EGLStreamKHR stream);
EGLBoolean  eglQuerySurface64KHR(EGLDisplay dpy, EGLSurface surface, EGLint attribute, EGLAttribKHR *value);
EGLBoolean  eglDestroySyncKHR(EGLDisplay dpy, EGLSyncKHR sync);
EGLint  eglClientWaitSync(EGLDisplay dpy, EGLSync sync, EGLint flags, EGLTime timeout);
EGLBoolean  eglDestroyImageKHR(EGLDisplay dpy, EGLImageKHR image);
EGLBoolean  eglDestroyContext(EGLDisplay dpy, EGLContext ctx);
EGLBoolean  eglStreamConsumerAcquireAttribKHR(EGLDisplay dpy, EGLStreamKHR stream, const EGLAttrib *attrib_list);
EGLBoolean  eglReleaseTexImage(EGLDisplay dpy, EGLSurface surface, EGLint buffer);
EGLBoolean  eglQueryDmaBufModifiersEXT(EGLDisplay dpy, EGLint format, EGLint max_modifiers, EGLuint64KHR *modifiers, EGLBoolean *external_only, EGLint *num_modifiers);
EGLBoolean  eglStreamConsumerGLTextureExternalKHR(EGLDisplay dpy, EGLStreamKHR stream);
EGLBoolean  eglQueryOutputLayerAttribEXT(EGLDisplay dpy, EGLOutputLayerEXT layer, EGLint attribute, EGLAttrib *value);
EGLBoolean  eglSignalSyncKHR(EGLDisplay dpy, EGLSyncKHR sync, EGLenum mode);
EGLSurface  eglCreateWindowSurface(EGLDisplay dpy, EGLConfig config, EGLNativeWindowType win, const EGLint *attrib_list);
EGLBoolean  eglSetStreamMetadataNV(EGLDisplay dpy, EGLStreamKHR stream, EGLint n, EGLint offset, EGLint size, const void *data);
EGLBoolean  eglQueryStreamu64KHR(EGLDisplay dpy, EGLStreamKHR stream, EGLenum attribute, EGLuint64KHR *value);
void  eglSetBlobCacheFuncsANDROID(EGLDisplay dpy, EGLSetBlobFuncANDROID set, EGLGetBlobFuncANDROID get);
EGLBoolean  eglQueryNativePixmapNV(EGLDisplay dpy, EGLSurface surf, EGLNativePixmapType *pixmap);
EGLBoolean  eglQueryStreamKHR(EGLDisplay dpy, EGLStreamKHR stream, EGLenum attribute, EGLint *value);
EGLSync  eglCreateSync(EGLDisplay dpy, EGLenum type, const EGLAttrib *attrib_list);
EGLBoolean  eglStreamConsumerAcquireKHR(EGLDisplay dpy, EGLStreamKHR stream);
EGLBoolean  eglGetConfigs(EGLDisplay dpy, EGLConfig *configs, EGLint config_size, EGLint *num_config);
EGLBoolean  eglGetOutputLayersEXT(EGLDisplay dpy, const EGLAttrib *attrib_list, EGLOutputLayerEXT *layers, EGLint max_layers, EGLint *num_layers);
EGLSurface  eglCreatePlatformWindowSurfaceEXT(EGLDisplay dpy, EGLConfig config, void *native_window, const EGLint *attrib_list);
EGLBoolean  eglCopyBuffers(EGLDisplay dpy, EGLSurface surface, EGLNativePixmapType target);
EGLBoolean  eglDestroySyncNV(EGLSyncNV sync);
EGLBoolean  eglSwapBuffers(EGLDisplay dpy, EGLSurface surface);
EGLSurface  eglCreatePixmapSurfaceHI(EGLDisplay dpy, EGLConfig config, struct EGLClientPixmapHI *pixmap);
EGLBoolean  eglStreamConsumerOutputEXT(EGLDisplay dpy, EGLStreamKHR stream, EGLOutputLayerEXT layer);
EGLBoolean  eglSwapBuffersRegion2NOK(EGLDisplay dpy, EGLSurface surface, EGLint numRects, const EGLint *rects);
EGLSurface  eglCreatePixmapSurface(EGLDisplay dpy, EGLConfig config, EGLNativePixmapType pixmap, const EGLint *attrib_list);
EGLBoolean  eglMakeCurrent(EGLDisplay dpy, EGLSurface draw, EGLSurface read, EGLContext ctx);
EGLBoolean  eglDestroyImage(EGLDisplay dpy, EGLImage image);
EGLBoolean  eglOutputLayerAttribEXT(EGLDisplay dpy, EGLOutputLayerEXT layer, EGLint attribute, EGLAttrib value);
EGLBoolean  eglDestroySync(EGLDisplay dpy, EGLSync sync);
EGLClientBuffer  eglCreateNativeClientBufferANDROID(const EGLint *attrib_list);
EGLBoolean  eglStreamConsumerGLTextureExternalAttribsNV(EGLDisplay dpy, EGLStreamKHR stream, EGLAttrib *attrib_list);
EGLint  eglWaitSyncKHR(EGLDisplay dpy, EGLSyncKHR sync, EGLint flags);
EGLSurface  eglCreatePbufferSurface(EGLDisplay dpy, EGLConfig config, const EGLint *attrib_list);
EGLBoolean  eglDestroySurface(EGLDisplay dpy, EGLSurface surface);
EGLBoolean  eglUnlockSurfaceKHR(EGLDisplay dpy, EGLSurface surface);
EGLBoolean  eglPresentationTimeANDROID(EGLDisplay dpy, EGLSurface surface, EGLnsecsANDROID time);
EGLImageKHR  eglCreateDRMImageMESA(EGLDisplay dpy, const EGLint *attrib_list);
EGLStreamKHR  eglCreateStreamAttribKHR(EGLDisplay dpy, const EGLAttrib *attrib_list);
EGLBoolean  eglGetOutputPortsEXT(EGLDisplay dpy, const EGLAttrib *attrib_list, EGLOutputPortEXT *ports, EGLint max_ports, EGLint *num_ports);
EGLBoolean  eglFenceNV(EGLSyncNV sync);
EGLBoolean  eglStreamConsumerReleaseAttribKHR(EGLDisplay dpy, EGLStreamKHR stream, const EGLAttrib *attrib_list);
EGLBoolean  eglQueryOutputPortAttribEXT(EGLDisplay dpy, EGLOutputPortEXT port, EGLint attribute, EGLAttrib *value);
EGLBoolean  eglSwapBuffersWithDamageEXT(EGLDisplay dpy, EGLSurface surface, EGLint *rects, EGLint n_rects);
EGLenum  eglQueryAPI();
EGLBoolean  eglDestroyStreamKHR(EGLDisplay dpy, EGLStreamKHR stream);
EGLBoolean  eglSwapBuffersRegionNOK(EGLDisplay dpy, EGLSurface surface, EGLint numRects, const EGLint *rects);
EGLDisplay  eglGetCurrentDisplay();
EGLDisplay  eglGetDisplay(EGLNativeDisplayType display_id);
EGLBoolean  eglQueryNativeDisplayNV(EGLDisplay dpy, EGLNativeDisplayType *display_id);
'''
