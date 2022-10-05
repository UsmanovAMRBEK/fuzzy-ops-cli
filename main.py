import sys
import utils
import docs
import calc


def head():
    ########################################
    ##          Welcome Page              ##
    ########################################
    print()
    utils.pcolor.prCyan(utils.print_centre("Fuzzy Logic Operations"))

    utils.pcolor.prPurple("Menu:")

    ##############################
    ##      1)Documentation     ##
    ##############################
    utils.pcolor.prGreen("1) Documentation of fuzzy Logic 📄")

    ##################################
    ##   2) Fuzzy Sets Calculator   ##
    ##################################
    utils.pcolor.prLightPurple("2) Fuzzy Sets Calculator 🧮")
    
    ##################################
    ##   3) Classic Sets Calculator ##
    ##################################
    utils.pcolor.prLightGray("3) Classic Sets Calculator 📅")

    ######################
    ##      4) Exit     ##
    ######################
    utils.pcolor.prRed("4) Exit💥")



##############################
##      Select Document     ##
##############################
def doc():
    utils.clear_screen()
    print()
    print("\033[01mDocuments: ")
    utils.pcolor.prReset("1) Fuzzy Sets")
    utils.pcolor.prYellow("2) Classic Sets")
    utils.pcolor.prRed("3) 👈 Orqaga")
    while True:
        line = input("👉 Select Document Index: >>> ")
        if line=="":
            arg='!!!'
            print(utils.print_centre(f"\033[91m{arg}\033[00m" + f"\033[34mIltimos buyruqlar bandini kiriting\033[00m"+f"\033[91m{ arg}\033[00m"))
        elif line=='1':
            docs.open_fuzzy()
            print("Yana davom eting: 👇")
        elif line=='2':
            docs.open_classic()
            print("Yana davom eting: 👇")
        elif line=='3':
            menu()
            break
        else:
            utils.pcolor.prRed("Buyruqlar bandi noto`g'ri kiritildi.....")

##############################
##      calculator heads    ##
##############################
# def fuzzy_calc_head():
#     utils.clear_screen()
#     print()
#     utils.pcolor.prYellow("Bandlar: ")
#     utils.pcolor.prPurple("1) Faqat 2 ta to`plam ustidagi amallar")
#     utils.pcolor.prLightGray("2) 2 va undan ortiq to`plamlar ustidagi amallar")
#     utils.pcolor.prCyan("3)👈 Orqaga")

# def classic_calc_head():
#     utils.clear_screen()
#     print()
#     utils.pcolor.prYellow("Bandlar: ")
#     utils.pcolor.prCyan("3)👈 Orqaga")

##############################
##      Define calculators  ##
##############################

##############################
##        Fuzzy Calc        ##
##############################
def fuzzy_calc():
    # fuzzy_calc_head()
    calc.Fuzzy.head()
    # select menu items
    while True:
        line = input("👉 Menu bandini tanlang: >>> ")
        if line=='':
            arg='!!!'
            print(utils.print_centre(f"\033[91m{arg}\033[00m" + f"\033[34mIltimos buyruqlar bandini kiriting\033[00m"+f"\033[91m{ arg}\033[00m"))
        elif line in ['1','2','3']:
            if line=='3':
                menu()
                break
            else:
                calc.Fuzzy.optimize(line)
        else:
            utils.pcolor.prRed("Buyruqlar bandi noto`g'ri kiritildi.....")


#############################
##      Classic calc       ##
#############################
def classic_calc():
    calc.Classic.head()
    # select menu items
    while True:
        line = input("👉 Menu bandini tanlang: >>> ")
        if line=='':
            arg='!!!'
            print(utils.print_centre(f"\033[91m{arg}\033[00m" + f"\033[34mIltimos buyruqlar bandini kiriting\033[00m"+f"\033[91m{ arg}\033[00m"))
        elif line in ['1','2','3','4','5']:
            if line=='5':
                menu()
                break
            else:
                calc.Classic.optimize(line)
        else:
            utils.pcolor.prRed("Buyruqlar bandi noto`g'ri kiritildi.....")



##############################
##      Select menu         ##
##############################
def menu():
    utils.clear_screen()
    head()
    while True:
        comm = input("👉 Select the desired menu item: >>> ")
        if comm=='':
            arg='!!!'
            print(utils.print_centre(f"\033[91m{arg}\033[00m" + f"\033[34mIltimos buyruqlar bandini kiriting\033[00m"+f"\033[91m{ arg}\033[00m"))
        
        elif comm=='1':
            doc()
            break
            # print("Yana davom eting: 👇")
        elif comm=='2': # Fuzzy Set Calc
            fuzzy_calc()
            #pass ## changing ...
        elif comm=='3':  # Classic Set Calc
            classic_calc()
        elif comm=='4':
            print("😏 Dastur yakunlandi.")
            sys.exit()
            # break

        else:
            utils.pcolor.prRed("Buyruqlar bandi noto`g'ri kiritildi.....")

if __name__=="__main__":
    menu()