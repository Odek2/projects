def announce(f):
    
    def wrapping():
        print("About to perform the function")
        f()
    

        print("Done performing the function ")
    return wrapping()    

@announce
def hello():
    print("Hello World!")  

    def hello_2():
        print("Second Greetings ")

    return hello_2

       # def hello_3():

           # print("Third Greetings ")  
        #return hello_3    
 