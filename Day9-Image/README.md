# README 

Image processing techniques.

## colorspace.py
- To change colorspaces from one to another 
## Steps:
1) Take image
2) convert bgr to hsv
3) Threshold hsv for any color
4) Extract that color and do whatever you want
5) Save image

## tranformation.py
1) Scaling
- for shrinking use cv2.INTER_AREA
- for zooming use cv2.INTER_LINEAR
2) Translation
- If shift is of tx,ty
- M = [1,0,tx;0,1,ty]
3) Rotation
- For an angle theta, transformation matrix
M = [cosT, -sinT;sinT,cosT]
4) Affine transformation
- All parallel lines will still be parallel in the output
- Three points from input and their corresponding locations in the output is req.
5) Perspective transform
- Straight lines remain straight
- 4 points of which 3 should not be collinear

## thresholding.py
1) Normal
- If a pixel value is greater than a threshold value, it is assigned another value
- Source image should be grayscale
- Types are:
THRESH_BINARY
THRESH_BINARY_INV
THRESH_TRUNC
THRESH_TOZERO
THRESH_TOZERO_INV

2) Adaptive
ADAPTIVE_THRESH_MEAN_C : thresh value is mean of neighborhood area
ADAPTIVE_THRESH_GAUSSIAN_C: weighted sum of neighborhood values where weights are gaussian
Note: - Block size: size of neighborhood area, C - constant subtracted from the mean or weighted mean calculated.

3) Otsu
- Automatically selects a threshold value

## canny.py
- Edge detection
1) Noise reduction:
- remove noise
- 5x5 Gaussian filter 
2) Finding intensity gradient of image
- Sobel kernel in both horizontal and vertical direction. Gx,Gy
- Edge gradient: G = sqrt(Gx^2+Gy^2)
- Angle theta = tan^-1(Gy/Gx)
3) Non - maximum suppression
- Full image is scanned: to remove any unwanted pixels
- Each pixel is checked and if local max in its neighborhoods in the direction in the gradiet
- binary image with thin edges
4) Hysterisis thresholding
- Min and Max values
- below Min is not an edge and is discarded
- Above Max is edge for sure

## gradients.py
1) Sobel and scharr derivatives
- Joint Gaussian smoothing plus differentiation operation
- More resistant to noise
2) Laplacian Derivatives
- kernel used is : [0,1,0;1,-4,1;0,1,0]

## smoothing.py
1) 2D convolution
- low pass, high pass filters
- LPF: removing noise, blurring image
- HPF: finding edges
- Kernel: 1/25*np.ones((5,5))

2) Image blurring/Smoothing
2.1) Averaging
- avg of all pixels under kernel area and replaces central element with the avg.
- K = 1/9*np.ones((3,3))

3) Gaussian Filtering 
- box filter with equal filter coeff
- width and height of kernel is req.
- highly effective in removing Gaussian noise from image

4) Median Filtering 
- Median of all pixels under the kernel window
- Central part is replaced with median value
- Removes salt and pepper noise
- Kernel size is a positive odd integer

5) Bilateral Filtering 
- Earlier filters tend to blur edges
- Pixels which are spatial neighbors are considered 
- Preserves edges
- Texture goes, Edges are preserved.
