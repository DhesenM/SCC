/**
 * Edgy
 *     -1  -1  -1
 *     -1   9  -1
 *     -1  -1  -1
 *     
 * This adds the Laplacian weighted average to the original pixel, 
 * which sharpens the edges in the image. 
 */

public class EdgyFilter implements Filter
{
	public void filter(PixelImage pi)
	{
		Pixel[][] data = pi.getData();
		int factor = 1;
		int diff = 0;
		
		int[][] Edgy = {{-1,  -1,  -1},
                        {-1,   9,  -1},
                        {-1,  -1,  -1}};	
		
		pi.getAverage(data, Edgy, factor, diff);
	}

}