

import config  # 加载配置
from config import pasteFullFileName
import global_variable as glv
from input_process import inputParameters, isIceEnable
# from excel import *
from multiProcess import *
from logPrint import *
from analysis import *

def main():
    ## icecream & input
    args=inputParameters()
    isIceEnable(args.debug)

    taskList = glv._get("taskList")
    processBeginTime=timeBeginPrint("multiple taskList")

    # Step1: manual compile all exe before run-sniper phase
    errorPrint("-----------------------------------STEP1----------------------------------------")
    
    
    errorPrint("-----------------------------------STEP2.1----------------------------------------")
    # Step2: run-sniper phase
    # Step2.1: parallel run single cpu mode
    parallelTask( taskList, singleCpuMode)
    errorPrint("-----------------------------------STEP2.2----------------------------------------")
    
    # Step2.2: consecutive run multi pim-cores mode
    multiCorePIMMode(taskList, 32)

    errorPrint("-----------------------------------STEP3----------------------------------------")
    # Step3: run modified PIMProf result
    parallelTask(taskList, pimprof, coreCount=32 ) # 
    
    # Step4: build excel & graphics to analyse results
    analyseResults(taskList, coreCount=32 )

    #     # addData2Excel(wb,taskName,isFirstSheet,dataDict)

    #     isFirstSheet=0
    #     timeEndPrint(taskName,processBeginTime)
    # excelGraphBuild(wb,processBeginTime)
    timeEndPrint("multiple taskList",processBeginTime)
if __name__ == "__main__":
    main()