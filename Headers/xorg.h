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