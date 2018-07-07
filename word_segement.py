
import sys
import jieba
from jieba import analyse

def segment(input, output):
    input_file = open(input, "r")
    output_file = open(output, "w")
    jieba.load_userdict('./db/dictionary.json')
    while True:
        line = input_file.readline()
        if line:
            # mes = line.strip()[0]
            line = line.strip()
            seg_list = jieba.cut(line)
            # print(seg_list)
            segments = ""
            for str in seg_list:
                # print(str)
                segments = segments + str+ "/"
            segments = "M " + segments + "\n"
            output_file.write(segments)
        else:
            break
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    if 3 != len(sys.argv):
        print("Usage: ", sys.argv[0], "input output")
        sys.exit(-1)
    segment(sys.argv[1], sys.argv[2])