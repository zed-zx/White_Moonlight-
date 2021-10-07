import os
import re
import scan,coloar

def get_url():
    ff = open("urls.txt",'r+')
    temp = input("请导入文件：")
    f = open(temp,'r+')
    lines = f.readlines()
    pattern = re.compile(r'^(https|http)://')
    for line in lines:
        try:
            if not pattern.match(line.strip()):
                targeturl="http://"+line.strip()+'\n'
                ff.write(targeturl)
            else:
                targeturl=line.strip()+'\n'
                ff.write(targeturl)
        except Exception as e:
            print(e)
            pass
    f.close()
    coloar.printDarkWhite('---------------------------------url载入成功！--------------------------------------\n')
    coloar.printDarkWhite('[+]本次共载入'+str(len(lines))+'个url\n')


if __name__ == "__main__":
    coloar.printDarkWhite('''  
      
 _       ____    _ __            __  ___                  ___       __    __ 
| |     / / /_  (_) /____       /  |/  /___  ____  ____  / (_)___ _/ /_  / /_
| | /| / / __ \/ / __/ _ \     / /|_/ / __ \/ __ \/ __ \/ / / __ `/ __ \/ __/
| |/ |/ / / / / / /_/  __/    / /  / / /_/ / /_/ / / / / / / /_/ / / / / /_  
|__/|__/_/ /_/_/\__/\___/____/_/  /_/\____/\____/_/ /_/_/_/\__, /_/ /_/\__/  
                                                     /____/              
                                                     
                                                                            By:长相安                   
                                                                            Date:2021.10.6
                                                                            
            \n''')
    get_url()
    scan.start()



