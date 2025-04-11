import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("path_image", help="path to input image to be displayed")
parser.add_argument("path_image_output", help="path of the processed image to be saved")
args = parser.parse_args()
image = cv2.imread(args.path_image)
args = vars(parser.parse_args())
cv2.imwrite(args["path_image_output"], image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 加载图片的路径：path_image
# 输出图片的路径：path_image_output