class myclass(object):

    def __del__(self):
        """
        析构函数
        :return:
        """
        return
    def say(self):
        print("this is mysql -> say")
        return
    def say2(self,txt):
        print("this is mysql -> say2:"+txt)
        return

class myclass2:
    def say(self):
        print("this is mysql -> say3")
        return
    def say2(self,txt):
        print("this is mysql -> say4:"+txt)
        return