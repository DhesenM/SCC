import java.awt.image.*;

/**
 * Provides an interface to a picture as an array of Pixels
 */
public class PixelImage
{
	private BufferedImage myImage;
	private int width;
    private int height;

    /**
     * Map this PixelImage to a real image
     * @param bi The image
     */
    public PixelImage(BufferedImage bi)
    {
    	// initialise instance variables
        this.myImage = bi;
        this.width = bi.getWidth();
        this.height = bi.getHeight();
        }
    /**
     * Return the width of the image
     */
    public int getWidth()
    {
    	return this.width;
    	}

    /**
     * Return the height of the image
     */
    public int getHeight()
    {
    	return this.height;
    	}
    
    /**
     * Return the BufferedImage of this PixelImage
     */
    public BufferedImage getImage()
    {
    	return this.myImage;
    	}

    /**
     * Return the image's pixel data as an array of Pixels.  The
     * first coordinate is the x-coordinate, so the size of the
     * array is [width][height], where width and height are the
     * dimensions of the array
     * @return The array of pixels
     */
    public Pixel[][] getData()
    {
    	Raster r = this.myImage.getRaster();
        Pixel[][] data = new Pixel[r.getHeight()][r.getWidth()];
        int[] samples = new int[3];

        for (int row = 0; row < r.getHeight(); row++)
        {
        	for (int col = 0; col < r.getWidth(); col++)
            {
        		samples = r.getPixel(col, row, samples);
                Pixel newPixel = new Pixel(samples[0], samples[1], samples[2]);
                data[row][col] = newPixel;
                }
        	}

        return data;
        }

    /**
     * Set the image's pixel data from an array.  This array matches
     * that returned by getData().  It is an error to pass in an
     * array that does not match the image's dimensions or that
     * has pixels with invalid values (not 0-255)
     * @param data The array to pull from
     */
    public void setData(Pixel[][] data) 
    {
    	int[] pixelValues = new int[3];     
    	// a temporary array to hold r,g,b values
    	WritableRaster wr = this.myImage.getRaster();
    	
    	if (data.length != wr.getHeight())
        {
    		throw new IllegalArgumentException("Array size does not match");
    		}
    	else if (data[0].length != wr.getWidth())
    	{
    		throw new IllegalArgumentException("Array size does not match");
    		}

    	for (int row = 0; row < wr.getHeight(); row++)
    	{
    		for (int col = 0; col < wr.getWidth(); col++)
    		{
    			pixelValues[0] = data[row][col].red;
    			pixelValues[1] = data[row][col].green;
    			pixelValues[2] = data[row][col].blue;
    			wr.setPixel(col, row, pixelValues);
    			}
    		}
    	}
  
    /**
     * Compute a new image given weighted averages
     * @return 
     */
    public void getAverage(Pixel[][] data, int[][] weight, int factor, int diff) 
    { 	
    	WritableRaster r = this.myImage.getRaster();
    	int[] colors = new int[3];
              
    	// use nested for loops to find the rgb values of the Pixel[][] data
    	for (int row = 1; row < data.length - 1; row++)
    	{
    		for (int col = 1; col < data[row].length - 1; col++)
    		{
    			// create int sum to calculate the weighted average later
    			int sumRed, sumGreen, sumBlue;
    		    sumRed = 0;
    		    sumGreen = 0;
    		    sumBlue = 0;
    		    
    			for (int a = -1; a < 2; a++)
    			{
    				for (int b = -1; b < 2; b++)
    				{
    					// calculate the weighted sum
    					// sum equals data * weight
    					sumRed += data[row + a][col + b].red * weight[1 + a][1 + b] - diff;
    					sumGreen += data[row + a][col + b].green * weight[1 + a][1 + b] - diff;
    					sumBlue += data[row + a][col + b].blue * weight[1 + a][1 + b] - diff;
    					}
    				}
    			
	  			// calculate the weighted average value
    			sumRed /= factor;
    			sumGreen /= factor;
    			sumBlue /= factor;
    			
    			// set the rgb value that < 0 to 0 
    		    // and the rgb value >255 to 255
    			colors[0] = setValue(sumRed);
    			colors[1] = setValue(sumGreen);
    			colors[2] = setValue(sumBlue);
    			
    			r.setPixel(col, row, colors);
    			
    			}
    		}
    	}
    
    /**
     * set the rgb value that < 0 to 0 
     * and the rgb value >255 to 255
     */
    public int setValue(int rgb)
    { 	
    	if (rgb < 0)
    	{
    		rgb = 0;
    	}
    	if (rgb > 255)
    	{
    		rgb = 255;
    	}
    	return rgb;
    }
    
}