# Question 1 [Paper 2 May/June 2022 9618/22]
'''A procedure LastLines() will:
• take the name of a text file as a parameter
• output the last three lines from that file, in the same order as they appear in the file.
 Note:
• Use local variables LineX, LineY and LineZ to store the three lines from the file.
• You may assume the file exists and contains at least three lines.
 Write Python code for the procedure LastLines().'''

def LastLines():
    
    f = open('TheTxtFile.txt', "r")

    LineX = ""
    LineY = ""
    LineZ = ""

    for line in f:
        LineX = LineY
        LineY = LineZ
        LineZ = line

    print(LineX)
    print(LineY)
    print(LineZ)

LastLines()
