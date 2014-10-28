package main

import (
	"log"

	cvhist "./lib"
	opencv "github.com/lazywei/go-opencv/opencv"
)

func main() {
	img := opencv.LoadImage("snow_leopard.jpg")
	if img == nil {
		log.Fatal("LoadImage failed")
	}
	defer img.Release()

	cvhist.Calc()
}
