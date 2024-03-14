import sys
sys._excepthook = sys.excepthook
def my_exeption_hook(exctype,value,traceback):

    print(exctype,value,traceback)

    sys._excepthook(exctype,value,traceback)
    sys.exit(1)

sys.excepthook = my_exeption_hook