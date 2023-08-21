import re,fire,sys

class LogParser():
        
    def parse_access_log(log_path=""):
        file = open(log_path,"r")
        total = 0
        outputs = []
        for line in file.readlines():
            parts = re.split('\"',line)
            byte_c = re.split('\s',parts[2])
            if parts[2][1:2]=='4':
                out = re.split('\s',parts[1])
                outputs.append(out[1])
            total += int(byte_c[2])

        print(total)
        for i in range(len(outputs)):
            print(outputs[i])
        
if __name__ == '__main__':
    LogParser.parse_access_log(log_path=sys.argv[1])
    