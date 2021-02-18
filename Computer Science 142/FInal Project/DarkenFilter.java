/**
 * Darken
 *       1  1  1
 *       1  1  1
 *       1  1  1
 *     
 * This darken the image 
 */

public class DarkenFilter implements Filter
{
	public void filter(PixelImage pi)
	{
		Pixel[][] data = pi.getData();
		int factor = 9;
		int diff = 20;
		
		int[][] Edgy = {{1,  1,  1},
                        {1,  1,  1},
                        {1,  1,  1}};	
		
		pi.getAverage(data, Edgy, factor, diff);
	}

}