def div(a,b):
    print(a/b)


def smart_div(func):
    def div(a,b):
        if (a<b):
            a,b = b,a 
            print (a/b)
        return(a,b)
    return div

div = smart_div(div)
div(2,4)