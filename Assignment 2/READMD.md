# Assignment 2
1. Download Lena color image convert it to grayscale image and add salt and  pepper noise with noise quantity 0.1,0.2 upto 1 and generate 10 noisy images.
    1. Do average filtering ( by correlating with average filter ) of varying sizes for each image. Filter size can be 3*3, 5*5, 7*7. (In 3*3 filter all the values are 1/9, in 5*5 filter all the values are 1/25 and in 7*7 filter all the values are 1/49)
        
    2. Similarly, repeat the question 1.a by replacing the average filter by median filter.


2. Question 
    1. Consider the image the attached named as hdraw.png and crop each of the characters from the image and consider that as the sub-image. Find the location of the sub-image in the original by using correlation.

    2. Download Lena color image convert it to grayscale image and crop the left eye of Lena as sub-image and do the cross-correlation ( Normalized correlation) to find the location of the left eye in the original image.

3. Write a function to implement FFT for 1D signal.

4. Implement DFT function for an image using the FFT for 1D signal using question 3.

5. Consider the images of lena and dog images attached. Find phase and magnitude of the dog and lena images using DFT function implemented in question 4.

6. Swap phase of the dog image and magnitude of the lena image and display the output.

7. Swap phase of the lena image and magnitude of the dog image ad display the output

Note: For all the above questions write user-defined functions and compare with predefined (in-built) function.
