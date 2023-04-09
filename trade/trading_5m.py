import sys
import os
import time
import pythoncom
from datetime import datetime, timedelta
from multiprocessing import Process
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from stocklab.agent.ebest import EBest


ebest_demo = EBest("DEMO")
ebest_demo.login()


if __name__ == '__main__':
    print("시작")
    
    # my_stock_info = ebest_demo.get_account_stock_info()
    
    test = ebest_demo.remove_real()
    print("끝", test)
    # print("내 주식:")
    # for i in my_stock_info:
    #     mycode = i['종목번호']
    #     print(">>>>>>>>>>>>>>>>>>>>", mycode)
        
        
    
    # ebest_demo.search_condition()
    
    
    
        
        
    
    
