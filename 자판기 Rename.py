class machine:
    global Selection
    Selection = {
        1000 : "물",
        1500 : "코카콜라",
        1800 : "펩시콜라",
        2000 : "환타",
        2500 : "포카리스웨트",
        3000 : "스프라이트",
        3100 : "칠성사이다",
        3200 : "솔의 눈",
    }

    def Activate(Money, Time):
        times = 0 # 몇개의 음료수를 고를건지
        Selects = [] # 선택한 음료수들

        print("-"*15)

        while times < Time: # 살 음료수들을 선택
            Select = input("\n음료수를 고르세요: \n")

            if(Select in Selection.keys()):
                Selects.append(Select)
            
            else:
                print("해당 음료수가 없습니다\n 다시 선택해주세요")
                continue

            times += 1

        print("-"*15)

        for l in Selects: # 살 음료수들을 결제하고, 거스름돈이 나오는
            Less_Money = 0 
            if(Money > Selection[l]):
                Money = Money - Selection[l] # 받은 돈에서 결제함
                print("{0} 음료수가 나왔습니다".format(l))

            else:
                print("주문하신 음료수가 없거나 돈이 적습니다")

            Less_Money += Money
        
        print("-"*15)

        print("거스름돈 : {0}".format(Less_Money))
    
machine.Activate(10000, 2)