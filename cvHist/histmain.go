package main

/*
#cgo pkg-config: opencv
#include <cv.h>
#include <highgui.h>
*/
import "C"
import "unsafe"

const (
	FileName = "snow_leopard.jpg"
)

type Hist struct {
	img unsafe.Pointer
}

func CalcHist(fn string) (*Hist, error) {
	filename := C.CString(fn)
	defer C.free(unsafe.Pointer(filename))

	img := unsafe.Pointer(C.cvLoadImage(filename, C.CV_LOAD_IMAGE_COLOR))
	return &Hist{img}, nil
}

func (h *Hist) ShowHist(wn string) {
	windowname := C.CString(wn)
	defer C.free(unsafe.Pointer(windowname))
	C.cvShowImage(windowname, h.img)
	C.cvWaitKey(0)
}

func main() {
	h, _ := CalcHist(FileName)
	h.ShowHist("Histogram")
}
