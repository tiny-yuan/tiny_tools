from time import sleep
from ERP.erp import ERP
# 函数调用
if __name__=="__main__":
    erp1 = ERP("tiny")
    erp1.data()
    sleep(5)
    print("生成sql语句完成！")
    erp1.mysql()