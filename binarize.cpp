#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

int main(int argc, char *argv[]) {
  cv::Mat gray_img = cv::imread("cvHist/snow_leopard.jpg", 0);
  if (!gray_img.data) return -1;

  cv::Mat bin_img;
  cv::threshold(gray_img, bin_img, 0, 255, cv::THRESH_BINARY|cv::THRESH_OTSU);

  cv::namedWindow("Binary");
  cv::imshow("Binary", bin_img);

  cv::waitKey(0);

  return 0;
}










