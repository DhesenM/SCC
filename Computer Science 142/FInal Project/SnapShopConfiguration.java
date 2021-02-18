/**
 * Report
 * 
 * I'll make more filters after flying back to China.
 * 
 * All of the filter works.
 * 
 * I used "row < data.length" instead of "row < data.length - 1"
 * which cost me a lot of time to compile. 
 * Fortunately I found the error today.
 */

/**
 * A class to configure the SnapShop application
 *
 * @author (Haode_Meng)
 * @version (a version number or a date)
 */
public class SnapShopConfiguration
{
  /**
   * Method to configure the SnapShop.  Call methods like addFilter
   * and setDefaultFilename here.
   * @param theShop A pointer to the application
   */
  public static void configure(SnapShop theShop)
  {

    theShop.setDefaultFilename("billg.jpg");
    theShop.addFilter(new FlipHorizontalFilter(), "Flip Horizontal");
    theShop.addFilter(new FlipVerticalFilter(), "Flip Vertical");
    theShop.addFilter(new NegativeFilter(), "Negative");
    theShop.addFilter(new GaussianFilter(), "Gaussian");
    theShop.addFilter(new LaplacianFilter(), "Laplacian");
    theShop.addFilter(new UnsharpMaskingFilter(), "Unsharp Masking");
    theShop.addFilter(new EdgyFilter(), "Edgy");
    theShop.addFilter(new DarkenFilter(), "Darken");
  }
}