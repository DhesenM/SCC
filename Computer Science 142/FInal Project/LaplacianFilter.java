/**
 * Laplacian
 * 
 *          -1  -1  -1
 *          -1   8  -1
 *          -1  -1  -1
 *          
 * The neighboring pixel values are subtracted from 8 times the center one, 
 * so no scaling is needed. 
 */

public class LaplacianFilter implements Filter
{
	public void filter(PixelImage pi)
	{
		Pixel[][] data = pi.getData();
		int factor = 1;
		int diff = 0;
		
		int[][] Laplacian = {{-1,  -1,  -1},
                             {-1,   8,  -1},
                             {-1,  -1,  -1}};	
		
		pi.getAverage(data, Laplacian, factor, diff);
	}

}
