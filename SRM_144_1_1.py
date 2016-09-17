__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=1704

# Encrypt a binary string by adding to each digit the sum of its adjacent digits.
# If P is the original string, and Q is the encrypted string, then Q[i] = P[i-1] + P[i] + P[i+1] for all digit positions i.
# Characters off the left and right edges of the string are treated as zeroes.
# Given an encrypted string, return the possible original string.

# There are two ways to decrypt the string, by assumming either 0 or 1 as the first digit of the original string.
# Starting from the second digit, digit P[i] can be calculated by P[i]=Q[i-1]-P[i-1]-P[i-2].
# Propagate in this way until the whole string is calculated, verify that
#   - each digit in P is either 0 or 1
#   - the last digit Q[n] equals to P[n-1]+P[n]
# Return decrypted string if it is valid.
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
