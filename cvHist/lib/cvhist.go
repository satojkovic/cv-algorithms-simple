package cvhist

// #cgo pkg-config: opencv
// #include <cv.h>
// #include <highgui.h>
import "C"
import "fmt"

func Calc() {
	fmt.Println("cvhist package")
}
