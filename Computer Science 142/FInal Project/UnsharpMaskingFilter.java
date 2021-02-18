/**
 * Unsharp masking
 *                -1  -2  -1
 *                -2  28  -2
 *                -1  -2  -1
 *                
 * This transformation is created by multiplying the center pixel and 
 * subtracting the Gaussian weighted average. 
 * The result must be divided by 16 to scale it back down to the range 0 to 255.  
 */

public class UnsharpMaskingFilter implements Filter
{
	public void filter(PixelImage pi)
	{
		Pixel[][] data = pi.getData();
		int factor = 16;
		int diff = 0;
		
		int[][] UnsharpMasking = {{-1,  -2,  -1},
		                          {-2,  28,  -2},
		                          {-1,  -2,  -1}};
		
		pi.getAverage(data, UnsharpMasking, factor, diff);
	}
}