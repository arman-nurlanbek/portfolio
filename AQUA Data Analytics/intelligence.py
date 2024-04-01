# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import numpy as np
from PIL import Image


def find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """ The purpose of the function is to find all red pixels in map_filename and output an image with all red pixels.
    The functions returns an image with all red pixels from map_filename.
    The function uses PIL to read map_filename, create new map with red pixels. Also it uses convert() to change
    image property from 'RGBA' to 'RGB' and numpy to create an array.
    Example of input: find_red_pixels('map.png')
    Example of output: 'map-red-pixels.jpg'
    """
    
    # Read map_filename using PIL
    im = Image.open(map_filename)
    # Load each pixel of map_filename to 'pixel' 
    pixel = im.load()
    # Property of map_filename
    mode = im.mode
    # Width of map_filename
    width = im.width
    # Height of map_filename
    height = im.height
    # Create new_image with properties of map_filename
    new_image = Image.new(mode, (width, height))
    # Load each pixel of new_image to 'new_pixel' 
    new_pixel = new_image.load()
    
    # The loop iterates over pixels and finds red pixels of input image.
    
    # Iterate over x axis
    for x in range(width):
        # Iterate over y axis
        for y in range(height):
            # Check if each pixel is red
            if pixel[x,y][0] > upper_threshold and pixel[x,y][1] < lower_threshold and pixel[x,y][2] < lower_threshold:
                # Apply the red pixel to the pixel in new_image
                new_pixel[x,y] = pixel[x,y]
                # Change the red pixel in new_image to white color.
                new_pixel[x,y] = (255,255,255)
    
    # Convert from 'RGBA' to 'RGB' and assign to new_image_rgb
    new_image_rgb = new_image.convert('RGB')
    # Create 'map-red-pixel.jpg' and apply pixels from new_image_rgb to it
    new_image_rgb.save('map-red-pixels.jpg')
    # Array with pixels from new_image_rgb using numpy
    array = np.array(new_image_rgb)
    # Returns the array
    return array



def find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """ The purpose of the function is to find all cyan pixels in map_filename and output an image with all cyan pixels.
    The functions returns an image with all cyan pixels from map_filename.
    The function uses PIL to read map_filename, create new map with cyan pixels. Also it uses convert() to change 
    image property from 'RGBA' to 'RGB'
    Example of input: find_cyan_pixels('map.png')
    Example of output: 'map-cyan-pixels.jpg'
    """
    
    # Read map_filename using PIL
    im = Image.open(map_filename)
    # Load each pixel of map_filename to 'pixel'
    pixel = im.load()
    # Property of map_filename
    mode = im.mode
    # Width of map_filename
    width = im.width
    # Height of map_filename
    height = im.height
    # Create new_image with properties of map_filename
    new_image = Image.new(mode, (width, height))
    # Load each pixel of new_image to 'new_pixel'
    new_pixel = new_image.load()
 
    # The loop iterates over pixels and finds cyan pixels of input image.
    # Iterate over x axis
    for x in range(width):
        # Iterate over y axis
        for y in range(height):
            # Check if each pixel is cyan
            if pixel[x,y][0] < lower_threshold and pixel[x,y][1] > upper_threshold and pixel[x,y][2] > upper_threshold:
                # Apply the red pixel to the pixel in new_image
                new_pixel[x,y] = pixel[x,y]
                # Change the red pixel in new_image to white color.
                new_pixel[x,y] = (255,255,255)
    
    # Convert from 'RGBA' to 'RGB' and assign to new_image_rgb
    new_image_rgb = new_image.convert('RGB')
    # Create 'map-red-pixel.jpg' and apply pixels from new_image_rgb to it
    new_image_rgb.save('map-cyan-pixels.jpg')
    

def detect_connected_components(*args, **kwargs):
    """ The purpose of this function is to find all the 8-connected components from previous function implementing the given algorithm. 
    The function outputs txt file with all connected componenets and their total amount.
    The function uses numpy to create 2D array and empty queue-liked ndarray.
    Example of input: detect_connected_components('map.png', upper_threshold=100, lower_threshold=50)
    Example of output: cc-output-2a.txt
    """
    
    # Array with new_image pixels from find_red_pixels() function
    p = find_red_pixels(*args, **kwargs)
    # Create empty array using numpy
    Q = np.array([])
    # Create 2D array using numpy
    MARK = np.zeros_like(p[:,:,:1])
    
    # List of components
    components = []
    # Variable that is used to count a component's number
    number = 0
    # Variable that is used to count an amount of pixels each component contains
    pixels = 0
    
    # Iterate over pixels in x - axis
    for x in range(p.shape[0]):
        # Iterate over pixels in y - axis
        for y in range(p.shape[1]):
            # Check if a pixel is a pavement pixel and check if MARK pixel is unvisited.
            if p[x][y][0] == 255 and MARK[x][y] == 0:
                # Set the MARK pixel as visited
                MARK[x][y] = 1
                # Count number of pixels
                pixels +=1
                # Append the pixel to numpy array Q
                Q = np.append(Q, [x,y])
    
                while len(Q) != 0:
                    # Set a shape for Q numpy array
                    Q.shape = (-1,2)
                    # Set pixel "m" corresponding to Q pixel
                    m = Q[0][0]
                    # Set pixel "n" corresponding to Q pixel
                    n = Q[0][1]
                    # Delete first element from Q numpy array
                    Q = np.delete(Q, 0, axis = 0)
                    
                    # Iterate around m pixel
                    for s in range(int(m-1), int(m+2)):
                        # Iterate around n pixel
                        for t in range(int(n-1), int(n+2)):
                            # Not every component has 8-connected component therefore IndexError appears
                            try:
                                # Check if a pixel is pavement pixel and MARK pixel is unvisited
                                if p[s][t][0] == 255 and MARK[s][t] == 0:
                                    # Set the MARK pixel to visited
                                    MARK[s][t] = 1
                                    # Count number of pixels
                                    pixels +=1
                                    # Add the pixel to Q numpy array
                                    Q = np.append(Q, [s,t])
                                    s = s - 1
                                    t = t -1
                            except IndexError:
                                continue    

                number += 1
                # Append a string with information of a connected component to the list
                components.append('Connected Component ' + str(number) + ', number of pixels = ' + str(pixels)+'\n')
                pixels = 0
     
    # Create a delimeter between lines
    delimeter = '\n'
    # Write element in components separated by delimeter
    with open('cc-output-2a.txt', 'w') as file:
        line = delimeter.join(components)
        file.write(line)
        # Write total number of connected components
        file.write('Total number of connected components = ' + str(number))
        
    # Return connected components
    return MARK

#detect_connected_components('map.png')
#def detect_connected_components_sorted(*args,**kwargs):
    
#detect_connected_components_sorted('map.png')