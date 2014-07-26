package main

import (
	opencv "github.com/lazywei/go-opencv/opencv"
	"os"
)

func main() {
	im := opencv.LoadImage("pitrain.png")
	if im == nil {
		panic("Loading image failed")
	}
	defer im.Release()

	w := im.Width()
	h := im.Height()

	gray := opencv.CreateImage(w, h, opencv.IPL_DEPTH_8U, 1)
	defer gray.Release()

	opencv.CvtColor(im, gray, opencv.CV_BGR2GRAY)

	win := opencv.NewWindow("Gray")
	defer win.Destroy()

	win.ShowImage(gray)

	for {
		key := opencv.WaitKey(20)
		if key == 27 {
			os.Exit(0)
		}
	}
}
