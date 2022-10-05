import utils
import pcolor
import calc
import enter_sets


class twoSetsOperation:

    def head():
        utils.clear_screen()
        print()
        pcolor.prBlue(utils.print_centre("\033[01mTwo Sets Operations: "))
        utils.pcolor.prYellow("Bandlar: ")
        utils.pcolor.prPurple("1) Algebraik ko`paytma")
        utils.pcolor.prLightGray("2) Chekli ko`paytma")
        utils.pcolor.prCyan("4) Qat'iy ko`paytma")
        utils.pcolor.prLightPurple("5) Algebraik yig'indi")
        utils.pcolor.prReset("6) Chekli yig'indi")
        utils.pcolor.prYellow("7) Qat'iy yig'indi")
        utils.pcolor.prBlue("8) Chekli farqi")
        utils.pcolor.prCyan("9)👈 Orqaga")


    def optimize():
        pass


class manySetsOperation:

    def head():
        utils.clear_screen()
        print()
        pcolor.prBlue(utils.print_centre("\033[01mMany Sets Operations: "))
        utils.pcolor.prYellow("Bandlar: ")
        utils.pcolor.prPurple("1) Union (A,B, ...)")
        utils.pcolor.prLightGray("2) Intersection (A,B, ...)")
        utils.pcolor.prLightPurple("3) Complement (U,A)")
        utils.pcolor.prCyan("4)👈 Orqaga")

        while True:
            line = input("👉 Menu bandini kiriting: >>> ")
            if line=="":
                arg='!!!'
                print(utils.print_centre(f"\033[91m{arg}\033[00m" + f"\033[34mIltimos buyruqlar bandini kiriting\033[00m"+f"\033[91m{ arg}\033[00m"))
            elif line in ['1','2','3','4']:
                if line == '1':
                    enter_sets.fuzzySet.twoSets.enter_union()
                elif line == '2':
                    enter_sets.fuzzySet.twoSets.enter_intersect()
                elif line == '3':
                    pass
                else:
                    calc.Fuzzy.head()
                    break
            else:
                utils.pcolor.prRed("Buyruqlar bandi noto`g'ri kiritildi.....")


    def optimize():
        pass