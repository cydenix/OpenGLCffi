xcb_connection_t *XGetXCBConnection(Display *dpy);
enum XEventQueueOwner { XlibOwnsEventQueue = 0, XCBOwnsEventQueue };
void XSetEventQueueOwner(Display *dpy, enum XEventQueueOwner owner);