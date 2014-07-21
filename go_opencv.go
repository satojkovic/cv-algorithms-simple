package main

import opencv "github.com/lazywei/go-opencv/opencv"

func main() {
	filename := "snow_leopard.jpg"
	srcImg := opencv.LoadImage(filename)
	if srcImg == nil {
		panic("Loading image failed")
	}
	defer srcImg.Release()
	resized1 := opencv.Resize(srcImg, 200, 200, 2)
	opencv.SaveImage("resize1.jpg", resized1, 0)
}
