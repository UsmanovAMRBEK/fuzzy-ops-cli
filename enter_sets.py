# import json
import pcolor
import utils
import calc
import main
import fuzzy_menu


class classicSet:
    def enter_difference():
        print()
        utils.clear_screen()
        pcolor.prCyan(utils.print_centre("Difference of sets: "))
        print("To`plamlarni kiriting: ❗(Elementlar bo`sh joy bilan ajratilgan)❗")
        while True:
            try:
                line1 = input("Birinchi to`plam elementlarini kiriting >>> ").split()
                line2 = input("Ikkinchi to`plam elemntlarini kiriting >>> ").split()
                pcolor.prGreen(calc.Classic.diff(line1,line2))
            except:
                pcolor.prRed("Xatolik mavjud!!!!")
            finally:
                msg = input("Yana davom etasizmi ? (type no exit menu)>>> ")
                if msg.lower() == 'no':
                    utils.clear_screen()
                    main.classic_calc()
                    break
                else:
                    pass


    def enter_complement():
        print()
        utils.clear_screen()
        pcolor.prCyan(utils.print_centre("Complement of set: "))
        print("To`plamni kiriting: ❗(Elementlar bo`sh joy bilan ajratilgan)❗")
        while True:
            try:
                line1 = input("Universal to`plam elementlarini kiriting >>> ").split()
                line2 = input("To`plamni elementlarini kiriting >>> ").split()
                pcolor.prGreen(calc.Classic.compl(line1,line2))
            except:
                pcolor.prRed("Xatolik mavjud!!!!")
            finally:
                msg = input("Yana davom etasizmi ? (type no exit menu)>>> ")
                if msg.lower() == 'no':
                    utils.clear_screen()
                    main.classic_calc()
                    break
                else:
                    pass


    def enter_union():
        print()
        utils.clear_screen()
        pcolor.prCyan(utils.print_centre("Union of sets: "))
        print("To`plamlarni kiriting: ❗(Elementlar bo`sh joy bilan ajratilgan)❗")

        def calc_again():
            mem_set = []
            i = 1
            while True:
                line = input(f"{i} - to`plam elementlarini kiriting >>> ").split()
                i+=1
                try:
                    mem_set.append(set(line))
                except:
                    pcolor.prRed("Xatolik mavjud!!!!")
                finally:
                    msg = input("Yana to`plam kiritilsinmi ? (type no exit enter sets) >>> ")
                    if msg.lower()=='no':
                        break
                    else:
                        pass
            pcolor.prGreen(f"result: {calc.Classic.uni(*mem_set)}")
        
        while True:
            try:
                calc_again()
            except:
                pcolor.prRed("Xatolik mavjud!!!!")
            finally:
                msg = input("Yana davom etasizmi? (type no exit menu) >>> ")
                if msg.lower()=='no':
                    utils.clear_screen()
                    main.classic_calc()
                    break
                else:
                    pass

                
    def enter_intersection():
        print()
        utils.clear_screen()
        pcolor.prCyan(utils.print_centre("Intersection of sets: "))
        print("To`plamlarni kiriting: ❗(Elementlar bo`sh joy bilan ajratilgan)❗")

        def calc_again():
            mem_set = []
            i = 1
            while True:
                line = input(f"{i} - to`plam elementlarini kiriting >>> ").split()
                i+=1
                try:
                    mem_set.append(set(line))
                except:
                    pcolor.prRed("Xatolik mavjud!!!!")
                finally:
                    msg = input("Yana to`plam kiritilsinmi ? (type no exit enter sets) >>> ")
                    if msg.lower()=='no':
                        break
                    else:
                        pass
            pcolor.prGreen(f"result: {calc.Classic.inter(*mem_set)}")
        
        while True:
            try:
                calc_again()
            except:
                pcolor.prRed("Xatolik mavjud!!!!")
            finally:
                msg = input("Yana davom etasizmi? (type no exit menu) >>> ")
                if msg.lower()=='no':
                    utils.clear_screen()
                    main.classic_calc()
                    break
                else:
                    pass


class fuzzySet:
    ################################
    ## 1) 2 ta to`plam
    ## 2) 2 va undan ortiq
    class twoSets:
        def enter_union():
            print()
            utils.clear_screen()
            pcolor.prCyan(utils.print_centre("Union of sets: "))
            print('To`plamlarni kiriting: ❗({"key1": value1, "key2":value2, ...})❗')


            def calc_again():
                mem_set = []
                i = 1
                while True:
                    try:
                        line = eval(input(f"{i} - to`plam elementlarini kiriting >>> "))
                        i+=1
                        mem_set.append(line)
                    except:
                        pcolor.prRed("Kiritishda xatolik mavjud!!!!")
                    finally:
                        msg = input("Yana to`plam kiritilsinmi ? (type no exit enter sets) >>> ")
                        if msg.lower()=='no':
                            break
                        else:
                            pass
                pcolor.prGreen(f"result: {calc.Fuzzy.uni(mem_set)}")
            
            while True:
                try:
                    calc_again()
                except:
                    pcolor.prRed("Xatolik mavjud!!!!")
                finally:
                    msg = input("Yana davom etasizmi? (type no exit menu) >>> ")
                    if msg.lower()=='no':
                        utils.clear_screen()
                        fuzzy_menu.manySetsOperation.head()
                        break
                    else:
                        pass

        def enter_intersect():
            print()
            utils.clear_screen()
            pcolor.prCyan(utils.print_centre("Intersection of sets: "))
            print('To`plamlarni kiriting: ❗({"key1": value1, "key2":value2, ...})❗')


            def calc_again():
                mem_set = []
                i = 1
                while True:
                    try:
                        line = eval(input(f"{i} - to`plam elementlarini kiriting >>> "))
                        i+=1
                        mem_set.append(line)
                    except:
                        pcolor.prRed("Kiritishda xatolik mavjud!!!!")
                    finally:
                        msg = input("Yana to`plam kiritilsinmi ? (type no exit enter sets) >>> ")
                        if msg.lower()=='no':
                            break
                        else:
                            pass
                pcolor.prGreen(f"result: {calc.Fuzzy.inter(mem_set)}")
            
            while True:
                try:
                    calc_again()
                except:
                    pcolor.prRed("Xatolik mavjud!!!!")
                finally:
                    msg = input("Yana davom etasizmi? (type no exit menu) >>> ")
                    if msg.lower()=='no':
                        utils.clear_screen()
                        fuzzy_menu.manySetsOperation.head()
                        break
                    else:
                        pass