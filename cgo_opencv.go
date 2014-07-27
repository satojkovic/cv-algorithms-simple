package main

import (
	opencv "github.com/lazywei/go-opencv/opencv"
	"unsafe"
)

// #cgo pkg-config: opencv
// #include <cv.h>
// #include <highgui.h>
import "C"

func main() {
	img := opencv.LoadImage("snow_leopard.jpg")
	if img == nil {
		panic("loading image failed")
	}
	defer img.Release()

	w := img.Width()
	h := img.Height()

	gray := opencv.CreateImage(w, h, opencv.IPL_DEPTH_8U, 1)
	defer gray.Release()

	opencv.CvtColor(img, gray, opencv.CV_BGR2GRAY)

	grayp := unsafe.Pointer(gray)
	C.cvSmooth(grayp, grayp, C.CV_GAUSSIAN, 11, 0, 0, 0)

	C.cvNamedWindow(C.CString("gaussian"), 1)
	C.cvShowImage(C.CString("gaussian"), grayp)
	C.cvWaitKey(0)
}
