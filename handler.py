

def new_process():
    print("I am new process...")

def main():
    ##fromlist means you can find the child function of src
    ##1.import the .py file below src
    function_01 = __import__("src.func_01",fromlist=True)
    ##determine whether the func_01.py is loaded.
    print(function_01)
    ##2.determine whether func_01.py has class FUNC01
    if hasattr(function_01,"FUNC01"):
        print("It has class Funct01")
        ##3.create a instance object of FUNC01,equal to class_func01 = FUNC01()
        ins_01 = getattr(function_01,"FUNC01")
        ##4. whether there is a function named process
        if hasattr(ins_01,"process"):
            ##5. get funtion of process
            func_process = getattr(ins_01,"process")
            func_process(ins_01)
        else:
            print("There are no function named process!")
        ##6.add a function named new_process
        setattr(ins_01,"new_process",new_process)
        ##7. whether the function has already add to the instance
        if hasattr(ins_01,"new_process"):
            print("it's new_process")
            func_new = getattr(ins_01,"new_process")
            func_new()
        delattr(ins_01,"new_process")

    else:
        print("There are no class named FUNC01")    


if __name__ == "__main__":
    main()


