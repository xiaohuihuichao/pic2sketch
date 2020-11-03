import cv2


def sketch(img_path, ksize=15, sigma=50):
    gray = cv2.imread(img_path)
    if gray.shape[2] == 3:
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)
    res = cv2.divide(gray, 255-blur, scale=255)
    return res


def sketch_1(img_path, ksize=15, sigma=50):
    gray = cv2.imread(img_path)
    if gray.shape[2] == 3:
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)
    res = cv2.divide(gray, blur, scale=255)
    return res

def imshow(win_name, img, t=0):
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.imshow(win_name, img)
    cv2.waitKey(t)


if __name__ == "__main__":
    img_path = "3.jpg"
    k = 21
    res1 = sketch(img_path, k)
    res2 = sketch_1(img_path, k)
    print(k)
    imshow("1", res1, 1)
    imshow("2", res2)
    