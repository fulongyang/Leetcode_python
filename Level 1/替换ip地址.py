












class Solution:

    @classmethod
    def replaceIP01(self, ip) -> None:
        return ''.join(ip[:-1:])+str(int(ip[-1:])+1)

    @classmethod
    def replaceIP02(self, ip) -> None:
        f = lambda x: str(x.split('.')[0]) + ':' + str(x.split('.')[1]) + ':' + str(x.split('.')[2]) + ':' + str(int(x.split('.')[3]) + 1)
        alter_ip = f(ip)
        return alter_ip

    @classmethod
    def replaceIP03(self, ip) -> None:
        ip = ip.split('.')
        return '{}:{}:{}:{}'.format(ip[0],ip[1],ip[2],int(ip[3])+1)
    






if __name__ == "__main__":
    ip = '192.168.1.1'
    result01 = Solution.replaceIP01(ip)
    result02 = Solution.replaceIP02(ip)
    result03 = Solution.replaceIP03(ip)
    # print(result01)
    # print(result02)
    print(result03)



















