class Solution:
    def rotate(self,times,l):
        for _ in range(times):
            x = l[len(l) - 1]
            for idx  in range(len(l) - 1,0,-1):
                l[idx] = l[idx - 1]
            l[0] = x
        return l
    def Encode(self,msg):
        k = ""
        lens = ""
        for m in msg:
            k += m
            lens += str(len(m))
        
        lens += str(2)
        k = self.rotate(2,[i for i in k])
        k = "".join(map(str,k)) 
        k = str(len(msg)) + k + lens  
        return k
    def Decode(self,msg_out):
        count = int(msg_out[0])
        offsets = msg_out[-count-1:]
        rot_amount = int(offsets[-1])
        offsets = offsets[:-1]
        msg_out = msg_out[1:-count-1]

        msg_out = self.rotate(len(msg_out) - rot_amount,[i for i in msg_out])
        out = []
        for offset in offsets:
            k = "".join(msg_out[:int(offset)])
            msg_out = msg_out[int(offset):]
            out.append(k) 
        return out

# rotate string 2 times
# save len of every string
# save number of rotations = 2
# put it in string at start and end
# return encoded msg
# decoding is just string parsing 


# yes i can skip rotating.

a = Solution().Encode(["we", "say", ":;", "yes"])
print(Solution().Decode(a))