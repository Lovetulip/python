"""

#判断密码强弱

"""
class FileTool:

    def __init__(self,filepath):

        self.filepath = filepath

    def write_tool(self,line):

        f = open(self.filepath,"w")

        f.write(line)

        f.close 

    def read_tool(self):

        f = open(self.filepath,"r")

        contect = f.readlines()

        f.close 

        return contect



class PasswdTool:

    def __init__(self,passwd):

        self.passwd = passwd 

        self.passwd_power = 0

        


    def check_letter(self,passwd):



        has_letter = False

        for c in passwd:

            if c.isnumeric():

                has_letter = True

                break

        return has_letter

    def check_num(self,passwd):



        has_num = False

        for c in passwd:

            if c.isalpha():

                has_num = True

                break

        return has_num
    
    def process_passwd(self,passwd):
    
        if len(self.passwd) <  8:

            print("密码长度小于8")

        else:
            
            self.passwd_power += 1

        if self.check_letter(self.passwd) :


            self.passwd_power += 1 

        else:

            print("密码要求包含数字")

        if self.check_num(passwd):

            self.passwd_power += 1


        else :
           
            print("密码要求包含字母")
            
            

              

               
def main():

    try_time = 5

    filepath = "passwd_6.0.txt"
    

    File_tool = FileTool(filepath)

    while  try_time > 0:    
            
        passwd = input("请输入密码(包含数字,字母,不少于8位)") 

        Passwd_tool = PasswdTool(passwd)

        Passwd_tool.process_passwd(passwd)
        
        File_tool.write_tool

        contect = "密码{},强度{}\n".format(passwd,Passwd_tool.passwd_power)
        
        File_tool.write_tool(contect)

        lines = File_tool.read_tool()

        print(lines)
#        f = open("passwd_5.0","a")
#
#        f.write("密码{},强度{}\n".format(passwd,Passwd_tool.passwd_power))
#
#        f.close()

        if Passwd_tool.passwd_power != 3:

            print("密码强度不够")

            try_time -= 1

        else:

            print("密码合格")

            break




if __name__ == "__main__":
    main()

else:
    print("error")
