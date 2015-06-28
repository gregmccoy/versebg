from os.path import join as pj
import yourpackage
 
def get_data(filename):
    packagedir = yourpackage.__path__[0]
    dirname = pj(os.path.dirname(packagedir), '..', 'share','data')
    fullname = os.path.join(dirname, filename)
    return fullname