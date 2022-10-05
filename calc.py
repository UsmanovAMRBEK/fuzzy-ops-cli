import pcolor
import utils
import enter_sets
import fuzzy_menu

class Fuzzy:

    def head():
        utils.clear_screen()
        print()
        pcolor.prBlue(utils.print_centre("\033[01mFuzzy Sets Operations: "))
        utils.pcolor.prYellow("Bandlar: ")
        utils.pcolor.prPurple("1) Faqat 2 ta to`plam ustidagi amallar")
        utils.pcolor.prLightGray("2) 2 va undan ortiq to`plamlar ustidagi amallar")
        utils.pcolor.prCyan("3)👈 Orqaga")
    
    ######################
    ## 2 va undan ortiq ##
    ######################
    def uni(args):

        def uni_inside(a,b):
            """
            args: a:dict; b:dict
            return: a.union(b)
            """
            result = dict()
            for i in a.keys():
                for j in b.keys():
                    if i.lower()==j.lower():
                        result[i]=max(a[i],b[j])
                    else:
                        result[i]=a[i]
                        result[j]=b[j]

            def sort(data):
                r = dict()
                for i in data.keys():
                    if i.lower() not in r.keys():
                        r[i.lower()]=data[i]
                return r
            
            return sort(result)

        r = args[0]
        for i in range(1,len(args)):
            r = uni_inside(r,args[i])
        return r
        

    def inter(args):

        def inter_inside(a,b):
            """
            args: a:dict; b:dict
            return: a.union(b)
            """
            result = dict()
            for i in a.keys():
                for j in b.keys():
                    if i.lower()==j.lower():
                        result[i]=min(a[i],b[j])
                    else:
                        result[i]=a[i]
                        result[j]=b[j]

            def sort(data):
                r = dict()
                for i in data.keys():
                    if i.lower() not in r.keys():
                        r[i.lower()]=data[i]
                return r
            
            return sort(result)

        r = args[0]
        for i in range(1,len(args)):
            r = inter_inside(r,args[i])
        return r

    #################################
    ## Faqat 2 ta to`plamlar uchun ##
    #################################

    def diff(A,B):
        A=set(A)
        B=set(B)
        return A.difference(B)

    def compl(a,b):
        # checking universal set
        def scan(a,b):
            for i in b:
                if i not in a:
                    return False
            return True
        
        if scan(a,b):
            return f"result: {set(a).difference(set(b))}"
        else:
            return "Universal to`plam no`to`gri tanlangan."

    


    def optimize(line):
        match line:
            case '1':
                fuzzy_menu.twoSetsOperation.head()
            case '2':
                fuzzy_menu.manySetsOperation.head()









class Classic:
    # Classic sets operations:
    # 1) Union(Birlashma)
    # 2) Intersection(Kesishma)
    # 3) Difference(Ayirma)
    # 4) Complement of Set(To`ldiruvchi)


    def head():
        utils.clear_screen()
        print()
        pcolor.prBlue(utils.print_centre("\033[01mClassic Sets Operations: "))
        utils.pcolor.prYellow("Bandlar: ")
        pcolor.prCyan("1) Union (Birlashma | ) M: A = {1,2,3,4} B = {2,3,5} A v B={1,2,3,4,5}")
        pcolor.prGreen("2) Intersection (Kesishma &) M: A = {1,2,3,4} B = {2,3,5} A & B = {2,3}")
        pcolor.prLightGray("3) Difference (Ayirma) (-) M: A = {1,2,3,4} B = {2,3,5} A-B = {1,4} B-A = {5}")
        pcolor.prLightPurple("4) Complement of Sets (CA = U - A) M: U = {1,2,3,4,5} A = {1,2,3} CA = {4,5}")
        pcolor.prRed("5)👈 Orqaga")
    

    def uni(*args):
        r = args[0]
        for i in args:
            r = r.union(i)
        return r

    def inter(*args):
        r = args[0]
        for i in args:
            r = r.intersection(i)
        return r
    
    def diff(A,B):
        A=set(A)
        B=set(B)
        return A.difference(B)

    def compl(a,b):
        # checking universal set
        def scan(a,b):
            for i in b:
                if i not in a:
                    return False
            return True
        
        if scan(a,b):
            return f"result: {set(a).difference(set(b))}"
        else:
            return "Universal to`plam no`to`gri tanlangan."

    def optimize(line):
        match line:
            case '1':
                enter_sets.classicSet.enter_union()
            case '2':
                enter_sets.classicSet.enter_intersection()
            case '3':
                enter_sets.classicSet.enter_difference()
            case '4':
                enter_sets.classicSet.enter_complement()