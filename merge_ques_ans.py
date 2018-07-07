
import sys

def merge_two(input1, input2, output):
    input_file1 = open(input1, "r")
    input_file2 = open(input2, "r")
    output_file = open(output, "w")

    while True:
        line1 = input_file1.readline()
        line2 = input_file2.readline()
        if line1 and line2:
            segments = line1 + line2 + "E " + '\n'
            output_file.write(segments)
        else:
            break
    input_file1.close()
    input_file2.close()
    output_file.close()

if __name__ == '__main__':
    if 4 != len(sys.argv):
        print("Usage: ", sys.argv[0], "input1 input2 output")
        sys.exit(-1)
    merge_two(sys.argv[1], sys.argv[2], sys.argv[3])