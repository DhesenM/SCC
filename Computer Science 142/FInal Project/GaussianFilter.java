/**
 * Gaussian
 * 
 *         1  2  1
 *         2  4  2
 *         1  2  1
 *         
 *  After computing the weighted sum, 
 *  the result must be divided by 16 to scale the numbers back down to the range 0 to 255. 
 *  The effect is to blur the image.
 */

public class GaussianFilter implements Filter
{
	public void filter(PixelImage pi)
	{
		Pixel[][] data = pi.getData();
		int factor = 16;
		int diff = 0;
		
		int[][] Gaussian = {{1,  2,  1},
		                    {2,  4,  2},
		                    {1,  2,  1}};
		
		pi.getAverage(data, Gaussian, factor, diff);
	}
}
