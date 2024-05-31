import unittest
import getdepth
import cv2


class TestCalc(unittest.TestCase):
    def test_getdepth(self):
        test_img_path = 'src/test_img.png'
        test_img = cv2.imread(test_img_path)
        test_depth_path = getdepth.GetDepth(test_img_path)
        test_depth = cv2.imread(test_depth_path)
        self.assertNotEqual(type(test_depth), None)
        self.assertEqual(test_depth.shape, test_img.shape)

if __name__ == '__main__':
    a = TestCalc()
    a.test_getdepth()