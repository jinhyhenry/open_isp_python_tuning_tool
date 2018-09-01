import sys

sys.path.append("/Users/henry/work/code/image_algo_own/own/open_isp_python/raw_reader/rawreader")
from rawreader import raw_obj

raw_file_path = "/Users/henry/work/code/image_algo_own/own/open_isp_python/raw_reader/raw_img/blk/IMG_20180202_052800.raw"
out_path = "blk.jpg"

#tune area
filter_type = 1 #1 -- means  2 -- med  3 -- k-means

def get_blk(buf):
	lens = len(buf)
	sum = 0
	for i in buf:
		sum = sum + i
	return (sum/lens)

if __name__ == '__main__':
	raw0 = raw_obj(4608,3456,0,raw_file_path,out_path)
	raw0.convert_to_normal()
	raw0.img_creater(1)
	print('r blk %d' %(get_blk(raw0.r_buf)))
	print('g blk %d' %(get_blk(raw0.g_buf)))
	print('b blk %d' %(get_blk(raw0.b_buf)))


