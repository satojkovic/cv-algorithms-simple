package main

/*
#cgo pkg-config: opencv
#include <cv.h>
#include <highgui.h>
*/
import "C"
import "unsafe"

func main() {
	filename := C.CString("snow_leopard.jpg")
	defer C.free(unsafe.Pointer(filename))

	C.cvNamedWindow(filename, 1)

	img := unsafe.Pointer(C.cvLoadImage(filename, C.CV_LOAD_IMAGE_COLOR))
	C.cvShowImage(filename, img)
	C.cvWaitKey(0)
}
