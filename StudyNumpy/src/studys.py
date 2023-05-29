'''
Created on 2023/05/29

@author: Keroichi.T
'''

import numpy as np

def main():
    print( np.__version__ )
    print( np.sqrt(2) )
    
    arr_1 = np.zeros(10, dtype=np.int16 )
    print(arr_1)
    

if __name__ == '__main__':
    main()