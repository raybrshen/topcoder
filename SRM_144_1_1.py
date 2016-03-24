__author__ = 'ray'

class BinaryCode:
	def decode(self, message):
		ret_0_flag = True
		ret_1_flag = True
		msg_len = len(message)
		ret_0 = list('0'*msg_len)
		ret_1 = list('1'*msg_len)
		if msg_len==1:
			if message=='1':
				return ('NONE','1')
			elif message=='0':
				return ('0','NONE')
			else:
				return ('NONE','NONE')
		for i in range(1,msg_len):
			if i == 1:
				ret_0[i] = chr(ord(message[i-1])-ord(ret_0[i-1])+48)
				ret_1[i] = chr(ord(message[i-1])-ord(ret_1[i-1])+48)
			else:
				ret_0[i] = chr(ord(message[i-1])-ord(ret_0[i-1])-ord(ret_0[i-2])+48*2)
				ret_1[i] = chr(ord(message[i-1])-ord(ret_1[i-1])-ord(ret_1[i-2])+48*2)
			if ret_0[i]!='0' and ret_0[i]!='1':
				ret_0_flag = False
			if ret_1[i]!='0' and ret_1[i]!='1':
				ret_1_flag = False
		if (not ret_0_flag) or ord(ret_0[msg_len-1])+ord(ret_0[msg_len-2])-48!=ord(message[msg_len-1]):
			ret_0 = 'NONE'
		if (not ret_1_flag) or ord(ret_1[msg_len-1])+ord(ret_1[msg_len-2])-48!=ord(message[msg_len-1]):
			ret_1 = 'NONE'
		ret = (''.join(ret_0), ''.join(ret_1))
		return ret

if __name__ == '__main__':
	bc = BinaryCode()
	re = bc.decode('2')
	print re[0]
	print re[1]
