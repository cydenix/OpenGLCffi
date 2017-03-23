
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
typedef ... GLbitfield;
typedef ... GLboolean;
typedef ... GLenum;
typedef ... GLfloat;
typedef ... GLint;
typedef ... GLintptr;
typedef ... GLsizei;
typedef ... GLsizeiptr;
typedef ... GLubyte;
typedef ... GLuint;
typedef ... DMbuffer;
typedef ... DMparams;
typedef ... VLNode;
typedef ... VLPath;
typedef ... VLServer;

typedef XID GLXFBConfigID;
typedef struct __GLXFBConfigRec *GLXFBConfig;
typedef XID GLXContextID;
typedef struct __GLXcontextRec *GLXContext;
typedef XID GLXPixmap;
typedef XID GLXDrawable;
typedef XID GLXWindow;
typedef XID GLXPbuffer;
typedef void (__GLXextFuncPtr)(void);
typedef XID GLXVideoCaptureDeviceNV;
typedef unsigned int GLXVideoDeviceNV;
typedef XID GLXVideoSourceSGIX;
typedef XID GLXFBConfigIDSGIX;
typedef struct __GLXFBConfigRec *GLXFBConfigSGIX;
typedef XID GLXPbufferSGIX;
typedef struct {
    int event_type;             /* GLX_DAMAGED or GLX_SAVED */
    int draw_type;              /* GLX_WINDOW or GLX_PBUFFER */
    unsigned long serial;       /* # of last request processed by server */
    Bool send_event;            /* true if this came for SendEvent request */
    Display *display;           /* display the event was read from */
    GLXDrawable drawable;       /* XID of Drawable */
    unsigned int buffer_mask;   /* mask indicating which buffers are affected */
    unsigned int aux_buffer;    /* which aux buffer was affected */
    int x, y;
    int width, height;
    int count;                  /* if nonzero, at least this many more */
} GLXPbufferClobberEvent;
typedef struct {
    int type;
    unsigned long serial;       /* # of last request processed by server */
    Bool send_event;            /* true if this came from a SendEvent request */
    Display *display;           /* Display the event was read from */
    GLXDrawable drawable;       /* drawable on which event was requested in event mask */
    int event_type;
    int64_t ust;
    int64_t msc;
    int64_t sbc;
} GLXBufferSwapComplete;
typedef union __GLXEvent {
    GLXPbufferClobberEvent glxpbufferclobber;
    GLXBufferSwapComplete glxbufferswapcomplete;
    long pad[24];
} GLXEvent;
typedef struct {
    int type;
    unsigned long serial;
    Bool send_event;
    Display *display;
    int extension;
    int evtype;
    GLXDrawable window;
    Bool stereo_tree;
} GLXStereoNotifyEventEXT;
typedef struct {
    int type;
    unsigned long serial;   /* # of last request processed by server */
    Bool send_event;        /* true if this came for SendEvent request */
    Display *display;       /* display the event was read from */
    GLXDrawable drawable;   /* i.d. of Drawable */
    int event_type;         /* GLX_DAMAGED_SGIX or GLX_SAVED_SGIX */
    int draw_type;          /* GLX_WINDOW_SGIX or GLX_PBUFFER_SGIX */
    unsigned int mask;      /* mask indicating which buffers are affected*/
    int x, y;
    int width, height;
    int count;              /* if nonzero, at least this many more */
} GLXBufferClobberEventSGIX;
typedef struct {
    char    pipeName[80]; /* Should be [GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX] */
    int     networkId;
} GLXHyperpipeNetworkSGIX;
typedef struct {
    char    pipeName[80]; /* Should be [GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX] */
    int     channel;
    unsigned int participationType;
    int     timeSlice;
} GLXHyperpipeConfigSGIX;
typedef struct {
    char pipeName[80]; /* Should be [GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX] */
    int srcXOrigin, srcYOrigin, srcWidth, srcHeight;
    int destXOrigin, destYOrigin, destWidth, destHeight;
} GLXPipeRect;
typedef struct {
    char pipeName[80]; /* Should be [GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX] */
    int XOrigin, YOrigin, maxHeight, maxWidth;
} GLXPipeRectLimits;

GLXContextID  glXGetContextIDEXT(const GLXContext context);
Bool  glXBindSwapBarrierNV(Display *dpy, GLuint group, GLuint barrier);
int  glXBindVideoCaptureDeviceNV(Display *dpy, unsigned int video_capture_slot, GLXVideoCaptureDeviceNV device);
void  glXLockVideoCaptureDeviceNV(Display *dpy, GLXVideoCaptureDeviceNV device);
GLXContext  glXCreateContext(Display *dpy, XVisualInfo *vis, GLXContext shareList, Bool direct);
GLXPixmap  glXCreateGLXPixmap(Display *dpy, XVisualInfo *visual, Pixmap pixmap);
int  glXSendPbufferToVideoNV(Display *dpy, GLXPbuffer pbuf, int iBufferType, unsigned long *pulCounterPbuffer, GLboolean bBlock);
int  glXBindVideoImageNV(Display *dpy, GLXVideoDeviceNV VideoDevice, GLXPbuffer pbuf, int iVideoBuffer);
void  glXReleaseTexImageEXT(Display *dpy, GLXDrawable drawable, int buffer);
Bool  glXJoinSwapGroupNV(Display *dpy, GLXDrawable drawable, GLuint group);
GLXContext  glXCreateAssociatedContextAMD(unsigned int id, GLXContext share_list);
__GLXextFuncPtr  glXGetProcAddress(const GLubyte *procName);
int  glXSwapIntervalSGI(int interval);
int  glXReleaseVideoImageNV(Display *dpy, GLXPbuffer pbuf);
void  glXDestroyWindow(Display *dpy, GLXWindow win);
int  glXBindHyperpipeSGIX(Display *dpy, int hpId);
void  glXQueryDrawable(Display *dpy, GLXDrawable draw, int attribute, unsigned int *value);
Bool  glXResetFrameCountNV(Display *dpy, int screen);
int  glXBindChannelToWindowSGIX(Display *display, int screen, int channel, Window window);
void  glXSwapBuffers(Display *dpy, GLXDrawable drawable);
Display * glXGetCurrentDisplay();
GLXPixmap  glXCreateGLXPixmapWithConfigSGIX(Display *dpy, GLXFBConfigSGIX config, Pixmap pixmap);
XVisualInfo * glXChooseVisual(Display *dpy, int screen, int *attribList);
int  glXQueryContextInfoEXT(Display *dpy, GLXContext context, int attribute, int *value);
GLXFBConfigSGIX * glXChooseFBConfigSGIX(Display *dpy, int screen, int *attrib_list, int *nelements);
Bool  glXQueryCurrentRendererIntegerMESA(int attribute, unsigned int *value);
void  glXDestroyPbuffer(Display *dpy, GLXPbuffer pbuf);
Bool  glXWaitForSbcOML(Display *dpy, GLXDrawable drawable, int64_t target_sbc, int64_t *ust, int64_t *msc, int64_t *sbc);
GLXContext  glXCreateAssociatedContextAttribsAMD(unsigned int id, GLXContext share_context, const int *attribList);
GLXHyperpipeConfigSGIX * glXQueryHyperpipeConfigSGIX(Display *dpy, int hpId, int *npipes);
void  glXCushionSGI(Display *dpy, Window window, float cushion);
GLXPixmap  glXCreatePixmap(Display *dpy, GLXFBConfig config, Pixmap pixmap, const int *attrib_list);
void  glXSelectEvent(Display *dpy, GLXDrawable draw, unsigned long event_mask);
void  glXGetSelectedEvent(Display *dpy, GLXDrawable draw, unsigned long *event_mask);
void  glXSwapIntervalEXT(Display *dpy, GLXDrawable drawable, int interval);
Bool  glXQueryExtension(Display *dpy, int *errorb, int *event);
Bool  glXMakeCurrent(Display *dpy, GLXDrawable drawable, GLXContext ctx);
Bool  glXQueryMaxSwapGroupsNV(Display *dpy, int screen, GLuint *maxGroups, GLuint *maxBarriers);
int  glXQueryHyperpipeAttribSGIX(Display *dpy, int timeSlice, int attrib, int size, void *returnAttribList);
Bool  glXQueryRendererIntegerMESA(Display *dpy, int screen, int renderer, int attribute, unsigned int *value);
Bool  glXQueryMaxSwapBarriersSGIX(Display *dpy, int screen, int *max);
void  glXGetSelectedEventSGIX(Display *dpy, GLXDrawable drawable, unsigned long *mask);
XVisualInfo * glXGetVisualFromFBConfigSGIX(Display *dpy, GLXFBConfigSGIX config);
int  glXHyperpipeConfigSGIX(Display *dpy, int networkId, int npipes, GLXHyperpipeConfigSGIX *cfg, int *hpId);
GLXContext  glXCreateContextAttribsARB(Display *dpy, GLXFBConfig config, GLXContext share_context, Bool direct, const int *attrib_list);
const char * glXQueryRendererStringMESA(Display *dpy, int screen, int renderer, int attribute);
int  glXChannelRectSyncSGIX(Display *display, int screen, int channel, GLenum synctype);
int  glXWaitVideoSyncSGI(int divisor, int remainder, unsigned int *count);
GLXPbuffer  glXCreatePbuffer(Display *dpy, GLXFBConfig config, const int *attrib_list);
void  glXSelectEventSGIX(Display *dpy, GLXDrawable drawable, unsigned long mask);
Bool  glXDelayBeforeSwapNV(Display *dpy, GLXDrawable drawable, GLfloat seconds);
GLXContext  glXImportContextEXT(Display *dpy, GLXContextID contextID);
int  glXQueryChannelRectSGIX(Display *display, int screen, int channel, int *dx, int *dy, int *dw, int *dh);
unsigned int  glXGetContextGPUIDAMD(GLXContext ctx);
void  glXJoinSwapGroupSGIX(Display *dpy, GLXDrawable drawable, GLXDrawable member);
void  glXDestroyGLXPixmap(Display *dpy, GLXPixmap pixmap);
Bool  glXAssociateDMPbufferSGIX(Display *dpy, GLXPbufferSGIX pbuffer, DMparams *params, DMbuffer dmbuffer);
int  glXGetVideoInfoNV(Display *dpy, int screen, GLXVideoDeviceNV VideoDevice, unsigned long *pulCounterOutputPbuffer, unsigned long *pulCounterOutputVideo);
GLXFBConfig * glXChooseFBConfig(Display *dpy, int screen, const int *attrib_list, int *nelements);
GLXContext  glXGetCurrentAssociatedContextAMD();
int  glXGetConfig(Display *dpy, XVisualInfo *visual, int attrib, int *value);
Bool  glXGetSyncValuesOML(Display *dpy, GLXDrawable drawable, int64_t *ust, int64_t *msc, int64_t *sbc);
void  glXBlitContextFramebufferAMD(GLXContext dstCtx, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter);
void  glXWaitX();
GLXContext  glXGetCurrentContext();
Bool  glXQueryFrameCountNV(Display *dpy, int screen, GLuint *count);
Bool  glXDeleteAssociatedContextAMD(GLXContext ctx);
void  glXWaitGL();
GLXVideoSourceSGIX  glXCreateGLXVideoSourceSGIX(Display *display, int screen, VLServer server, VLPath path, int nodeClass, VLNode drainNode);
Display * glXGetCurrentDisplayEXT();
Bool  glXSet3DfxModeMESA(int mode);
Bool  glXQueryVersion(Display *dpy, int *maj, int *min);
GLXVideoCaptureDeviceNV * glXEnumerateVideoCaptureDevicesNV(Display *dpy, int screen, int *nelements);
int64_t  glXSwapBuffersMscOML(Display *dpy, GLXDrawable drawable, int64_t target_msc, int64_t divisor, int64_t remainder);
int  glXGetFBConfigAttribSGIX(Display *dpy, GLXFBConfigSGIX config, int attribute, int *value);
int  glXQueryChannelDeltasSGIX(Display *display, int screen, int channel, int *x, int *y, int *w, int *h);
GLXPbufferSGIX  glXCreateGLXPbufferSGIX(Display *dpy, GLXFBConfigSGIX config, unsigned int width, unsigned int height, int *attrib_list);
void  glXDestroyPixmap(Display *dpy, GLXPixmap pixmap);
GLXContext  glXCreateContextWithConfigSGIX(Display *dpy, GLXFBConfigSGIX config, int render_type, GLXContext share_list, Bool direct);
int  glXQueryVideoCaptureDeviceNV(Display *dpy, GLXVideoCaptureDeviceNV device, int attribute, int *value);
void  glXNamedCopyBufferSubDataNV(Display *dpy, GLXContext readCtx, GLXContext writeCtx, GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size);
unsigned int  glXGetGPUIDsAMD(unsigned int maxCount, unsigned int *ids);
int  glXGetGPUInfoAMD(unsigned int id, int property, GLenum dataType, unsigned int size, void *data);
Bool  glXIsDirect(Display *dpy, GLXContext ctx);
int  glXGetVideoSyncSGI(unsigned int *count);
int  glXBindVideoDeviceNV(Display *dpy, unsigned int video_slot, unsigned int video_device, const int *attrib_list);
void  glXBindTexImageEXT(Display *dpy, GLXDrawable drawable, int buffer, const int *attrib_list);
int  glXHyperpipeAttribSGIX(Display *dpy, int timeSlice, int attrib, int size, void *attribList);
GLXPixmap  glXCreateGLXPixmapMESA(Display *dpy, XVisualInfo *visual, Pixmap pixmap, Colormap cmap);
void  glXDestroyContext(Display *dpy, GLXContext ctx);
void  glXReleaseVideoCaptureDeviceNV(Display *dpy, GLXVideoCaptureDeviceNV device);
int  glXReleaseVideoDeviceNV(Display *dpy, int screen, GLXVideoDeviceNV VideoDevice);
void  glXDestroyGLXPbufferSGIX(Display *dpy, GLXPbufferSGIX pbuf);
GLXContext  glXCreateNewContext(Display *dpy, GLXFBConfig config, int render_type, GLXContext share_list, Bool direct);
const char * glXQueryCurrentRendererStringMESA(int attribute);
Bool  glXMakeCurrentReadSGI(Display *dpy, GLXDrawable draw, GLXDrawable read, GLXContext ctx);
unsigned int  glXGetAGPOffsetMESA(const void *pointer);
Bool  glXQuerySwapGroupNV(Display *dpy, GLXDrawable drawable, GLuint *group, GLuint *barrier);
const char * glXGetClientString(Display *dpy, int name);
void  glXBindSwapBarrierSGIX(Display *dpy, GLXDrawable drawable, int barrier);
__GLXextFuncPtr  glXGetProcAddressARB(const GLubyte *procName);
void  glXDestroyGLXVideoSourceSGIX(Display *dpy, GLXVideoSourceSGIX glxvideosource);
void  glXCopySubBufferMESA(Display *dpy, GLXDrawable drawable, int x, int y, int width, int height);
void  glXCopyBufferSubDataNV(Display *dpy, GLXContext readCtx, GLXContext writeCtx, GLenum readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size);
XVisualInfo * glXGetVisualFromFBConfig(Display *dpy, GLXFBConfig config);
int  glXChannelRectSGIX(Display *display, int screen, int channel, int x, int y, int w, int h);
GLXFBConfig * glXGetFBConfigs(Display *dpy, int screen, int *nelements);
void  glXFreeContextEXT(Display *dpy, GLXContext context);
GLXDrawable  glXGetCurrentReadDrawable();
int  glXQueryContext(Display *dpy, GLXContext ctx, int attribute, int *value);
GLXWindow  glXCreateWindow(Display *dpy, GLXFBConfig config, Window win, const int *attrib_list);
void  glXCopyContext(Display *dpy, GLXContext src, GLXContext dst, unsigned long mask);
int  glXQueryHyperpipeBestAttribSGIX(Display *dpy, int timeSlice, int attrib, int size, void *attribList, void *returnAttribList);
Bool  glXWaitForMscOML(Display *dpy, GLXDrawable drawable, int64_t target_msc, int64_t divisor, int64_t remainder, int64_t *ust, int64_t *msc, int64_t *sbc);
Status  glXGetTransparentIndexSUN(Display *dpy, Window overlay, Window underlay, long *pTransparentIndex);
unsigned int * glXEnumerateVideoDevicesNV(Display *dpy, int screen, int *nelements);
Bool  glXMakeAssociatedContextCurrentAMD(GLXContext ctx);
Bool  glXGetMscRateOML(Display *dpy, GLXDrawable drawable, int32_t *numerator, int32_t *denominator);
const char * glXQueryServerString(Display *dpy, int screen, int name);
GLXDrawable  glXGetCurrentReadDrawableSGI();
Bool  glXReleaseBuffersMESA(Display *dpy, GLXDrawable drawable);
int  glXGetFBConfigAttrib(Display *dpy, GLXFBConfig config, int attribute, int *value);
void  glXUseXFont(Font font, int first, int count, int list);
void  glXCopyImageSubDataNV(Display *dpy, GLXContext srcCtx, GLuint srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLXContext dstCtx, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY, GLint dstZ, GLsizei width, GLsizei height, GLsizei depth);
Bool  glXMakeContextCurrent(Display *dpy, GLXDrawable draw, GLXDrawable read, GLXContext ctx);
GLXDrawable  glXGetCurrentDrawable();
GLXHyperpipeNetworkSGIX * glXQueryHyperpipeNetworkSGIX(Display *dpy, int *npipes);
int  glXGetVideoDeviceNV(Display *dpy, int screen, int numVideoDevices, GLXVideoDeviceNV *pVideoDevice);
int  glXDestroyHyperpipeConfigSGIX(Display *dpy, int hpId);
const char * glXQueryExtensionsString(Display *dpy, int screen);
GLXFBConfigSGIX  glXGetFBConfigFromVisualSGIX(Display *dpy, XVisualInfo *vis);
int  glXQueryGLXPbufferSGIX(Display *dpy, GLXPbufferSGIX pbuf, int attribute, unsigned int *value);
'''
