# encoding=utf-8
import os
import argparse
import tqdm

def GetFiles(input,output):
    if not os.path.isdir(input):
        print("input dirs not exit")
        exit(-1)
    if not os.path.exists(output):os.mkdir(output)
    return filter(os.path.isfile,(input + '/' + _file for _file in os.listdir(input))),(output + '/' + _file for _file in os.listdir(input))
def Reg_Aladin(reg_aladin,alts,flo,result):
    if not os.path.exists(reg_aladin):
        print("please input reg_aladin location!")
        exit(-1)
    os.system("{0} -ref {1} -flo {2} -res {3}".format(reg_aladin,alts,flo,result))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-reg", "--reg_aladin", help="reg_aladin location")
    parser.add_argument("-ref","--reg_filename",help=" Reference image filename")
    parser.add_argument("-i", "--input_dirs", help="Input dirs")
    parser.add_argument("-o", "--output_dirs", help="Output dirs")
    agrs=parser.parse_args()
    if agrs.input_dirs==None:
        print("please use \"python registration.py -h \" for help")
        exit(-1)
    inputs,outputs=GetFiles(agrs.input_dirs,agrs.output_dirs)
    pbar=tqdm.tqdm(zip(inputs,outputs))
    for i in pbar:
        Reg_Aladin(agrs.reg_aladin,agrs.reg_filename,i[0],i[-1])


