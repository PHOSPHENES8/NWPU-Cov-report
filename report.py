#!/usr/bin/env python3
import json
import time
import requests

if __name__ == '__main__':

	# init
	s = requests.session()
	headers = {
	}

	# report
	cookies = {
		#'eai-sess':'', #使用cookies进行身份认证
		#'UUkey':''
        #'JSESSIONID':''
	}

	data = {
        'dqszwz':'2',
        'j15tsfqw':'1',
        'j15tjcg':'1',
        'j15tnjssfjc':'1',
        'jtdtwfw':'1',
        'nhjsywyszz':'1',
        'nhjsdqjkzt':'1',
        'nhjssfzzgl':'1'
	}
	r = s.post('http://yqtb.nwpu.edu.cn/', data=data, headers=headers, cookies=cookies)
	#print('【上报】' + json.loads(r.text)['m'])
	time.sleep(3)
