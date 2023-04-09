# Image_Processing
Image_Processing_with_OpenCV

###########################################################################################################

Detect the Color with the Largest Contour

In this code, we will create an algorithm that finds the color which has the largest contour in the image.
Firstly, we will set the scale for the color that we want to recognize. After that, we send this scale of 
the color to the contour algorithm. These contours will be sorted by this algorithm and then we will determine 
the area of the contours. In this example, we will use 500 px for the area. Areas larger than 500 pixels will be 
extracted using the condition that we set. Finally, we will take the center coordinates of the area.


![111](https://user-images.githubusercontent.com/109924168/230763793-b0860d57-6f68-471e-a962-47232e4f462e.png)

Red color with the largest contour area detected

![2222](https://user-images.githubusercontent.com/109924168/230763799-fcdc6ff9-6f7f-41dc-a958-171e5b1ee543.png)

Center coordinates of the detected area


###########################################################################################################

Find the HSV Color Scale by Click to the Pixel

In this blog, we will find the hsv color scale by click to the Pixel. When we click on a pixel in the frame, 
the selected pixel is shown with an hsv color scale. There are two things that we make. Click two pixels in the image. 
These clicks will make a rectangle and the algorithm will give a scale of this color which is in this rectangle.


![bbbbbbbbb](https://user-images.githubusercontent.com/109924168/230764331-197a75f8-09fc-46bb-8c2e-afbd2735573b.png)

First Click of the Pixel

![bbbbbbb1](https://user-images.githubusercontent.com/109924168/230764346-b49a7f76-ad9a-4784-bcb8-be4b97d0ff89.png)

Second Click of the Pixel

![bbbbbbbbbb2](https://user-images.githubusercontent.com/109924168/230764361-2074f37e-937c-44f6-a070-545b4c9a1fb9.png)

And Now, We Found the HSV Scale of the Color

###########################################################################################################


Color recognition algorithm using colors for precision landing

In this code, the red algorithm will first search for the red region in the image. Once the red zone is detected 
and determined to be large enough (which may be more useful for setting up precision landing algorithms for drones), 
it will stop searching for the red zone and look for the blue zone.

![cccccccccccc1](https://user-images.githubusercontent.com/109924168/230764451-e6f6979a-e7f6-486f-9f4e-621a3f11366f.png)

First, the algorithm doesn’t detect the blue area until the red area is large enough


![ccccccc2](https://user-images.githubusercontent.com/109924168/230764455-cd148230-8549-4d23-8092-e87be75d4275.png)

When the red area is big enough, it searches for the blue area


###########################################################################################################

Identifying the Shapes of Detected Colors

We will predict the shapes of the colors detected in this algorithm. First we will determine the color.
We will determine the contour borders of the color we have detected. Next, we will make shape estimation using these bounds.


![tri](https://user-images.githubusercontent.com/109924168/230764481-5417ac49-24e5-4732-83af-71fd949f3945.png)

![circle](https://user-images.githubusercontent.com/109924168/230764490-fc3d019c-7bb5-46cb-978e-3a4169308bdf.png)

