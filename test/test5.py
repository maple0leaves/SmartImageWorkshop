import cv2

# 定义全局变量
drawing = False  # 标记是否正在绘制
start_x, start_y = -1, -1  # 矩形框的起始坐标

# 鼠标回调函数
def draw_rectangle(event, x, y, flags, param):
    global drawing, start_x, start_y

    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下，开始绘制
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:  # 鼠标左键松开，绘制完成
        drawing = False
        end_x, end_y = x, y

        # 绘制矩形框
        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

        # 应用马赛克效果
        mosaic_image = apply_mosaic(image, start_x, start_y, end_x-start_x, end_y-start_y, block_size)

        # 显示结果图像
        cv2.imshow('Mosaic Effect', mosaic_image)

# 应用马赛克效果
def apply_mosaic(image, x, y, width, height, block_size):
    # 提取区域并缩小
    roi = image[y:y+height, x:x+width]
    small_roi = cv2.resize(roi, (block_size, block_size), interpolation=cv2.INTER_NEAREST)

    # 放大马赛克图像到原始大小
    mosaic = cv2.resize(small_roi, (width, height), interpolation=cv2.INTER_NEAREST)

    # 替换原始图像的指定区域
    image[y:y+height, x:x+width] = mosaic

    return image

# 读取图像
image = cv2.imread('../img_1.png')

# 创建窗口并绑定鼠标回调函数
cv2.namedWindow('Mosaic Effect')
cv2.setMouseCallback('Mosaic Effect', draw_rectangle)

# 定义马赛克块的大小
block_size = 10

while True:
    cv2.imshow('Mosaic Effect', image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # 按下 'q' 键退出循环
        break

cv2.destroyAllWindows()
