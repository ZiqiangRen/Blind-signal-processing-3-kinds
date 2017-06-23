import matplotlib
import scipy.io as sio  
import matplotlib.pyplot as plt
from pylab import *
import numpy as np  
import data_util as da
import os

def get_txt(folder_name,FS_value,FFT_value,unit_num):
    FS_name='FS'+str(FS_value)+'M'
    FFT_name='FFT'+str(FFT_value)
    if unit_num==0:
        unit_name='FULL'
    else:    
        unit_name='U'+str(unit_num)
    file=str(folder_name)+'_'+FS_name+'_'+FFT_name+'_'+unit_name
    #print(file)
    return file

def count_file():
    count = 0
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        print(files)
        fileLength = len(files)
        for i in range(0,fileLength):
            if 'txt' in files[i]:
                count=count+1
                folder=files[i][0]
    print(files[0])
    print("The number of .txt files under <%s> is: %d" %(path,count))
    return count,folder
    
    
if __name__ == '__main__':
    num,folder=count_file()
    to_save=list()
    length=list()
    for i in range(1,num):
        file_name=get_txt(folder,40,17,i)    
        my=np.loadtxt(file_name+'.txt', skiprows=0)
        my=da.get_sig(my)
        length.append(len(my))
#         plt.figure()
#         plt.plot(my)
#         plt.show()
        features=da.get_feature(my)
        #features.append(i)
        to_save.append(features)        
        #print(features)
    to_save=array(to_save)  
    #print(to_save)
    print(length)
    print(sum(length)-length[0])
    j=0
    file_name=get_txt(folder,40,17,j)    
    momsig=np.loadtxt(file_name+'.txt', skiprows=0)
    momsig=da.get_sig(momsig)
    print("features extraction done...\n\n")
    
    
    
#     plt.figure()
#     plt.plot(momsig,'b')
    for file_idx in range(1,num):
        cost=list()
        frame=length[file_idx-1]
        step=int(frame/10)
        file_name0=get_txt(folder,40,17,file_idx)    
        sonsig=np.loadtxt(file_name0+'.txt', skiprows=0)
        sonsig=da.get_sig(sonsig)        
        
        for ii in range(0,len(momsig)-frame,step):
            mom=array(da.get_feature(momsig[ii:ii+frame]))
            #print(mom)
            son=array(to_save[file_idx-1])
            #print(son)
            cost.append(np.linalg.norm(mom-son))
        #print(len(cost))
        minindex=cost.index(min(cost))
        nx=range(minindex*step,minindex*step+frame)
        print("the No.%d fragment sequence interval is [%d,%d]"%(file_idx,minindex*step,minindex*step+frame))
        plt.figure()
        plt.subplot(211)
        plt.plot(sonsig)
        plt.subplot(212)
        
        plt.plot(nx,momsig[minindex*step:minindex*step+frame],'r')
        plt.savefig(file_name0+'.pdf')
        
            
       
    
    
