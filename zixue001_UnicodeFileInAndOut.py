#!usr/bin/python
#encoding:utf-8
'''
此测试文件用于unicode（带有0xfeff标志，非utf8）文件的读、写操作；
输入：zixue001_in.txt
输出: zixue001_out.txt
注：请注意所在目录无中文
'''
import sys
import io

def main():
    if len(sys.argv) != 3:
        print "Please input: .py in.txt out.txt\n"
        #return 0
        exit()

    #tmpfp = open('tmpout1.txt', 'w')
    #j = 12
    #pj = str(j)
    #tmpfp.write(pj)
    #tmpfp.close()

    (pypro, intxt, outxt) = sys.argv
    fpout = io.open(outxt, 'w', encoding = 'utf-16')

    fpin = io.open(intxt, 'r', encoding = 'utf-16')
    lsLines = fpin.readlines()
    fpin.close()

    i = 0
    for perLine in lsLines:
        i = i + 1

        si=str(i)
        sj = unicode(si, 'utf-8')
        fpout.write(sj)
        fpout.write(u':')

        lleng = len(perLine)
        perLine1 = perLine[:lleng-1]

        fpout.write(perLine1)
        fpout.write(u'\n')

        #测试输入一行是什么东东:自动去除0xfeff，换行只剩下0x000a（000d自动删除）
        for cc in perLine:
            dd = ord(cc)
            print '~%04x~' % dd

    fpout.close()

if __name__ == '__main__':
    main()

