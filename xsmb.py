import random

abcxyz = True
tkc = 10000

while True:
    #db
    db_1 = random.randint(100, 999)
    kq_de_db = random.randint(10, 99)

#################################
    #g1
    g_1 = random.randint(100, 999)
    kq_de_g1 = random.randint(10, 99)
#################################
    #g2
    g_2_1 = random.randint(100, 999)
    kq_de_g2_1 = random.randint(10, 99)

    g_2_2 = random.randint(100, 999)
    kq_de_g2_2 = random.randint(10, 99)
#################################

    #g3
    g_3_1 = random.randint(100, 999)
    kq_de_g3_1 = random.randint(10, 99)

    g_3_2 = random.randint(100, 999)
    kq_de_g3_2 = random.randint(10, 99)

    g_3_3 = random.randint(100, 999)
    kq_de_g3_3 = random.randint(10, 99)

    g_3_4 = random.randint(100, 999)
    kq_de_g3_4 = random.randint(10, 99)

    g_3_5 = random.randint(100, 999)
    kq_de_g3_5 = random.randint(10, 99)

    g_3_6 = random.randint(100, 999)
    kq_de_g3_6 = random.randint(10, 99)

#################################

    #g4
    g_4_1 = random.randint(10, 99)
    kq_de_g4_1 = random.randint(10, 99)

    g_4_2 = random.randint(10, 99)
    kq_de_g4_2 = random.randint(10, 99)
    
    g_4_3 = random.randint(10, 99)
    kq_de_g4_3 = random.randint(10, 99)
    
    g_4_4 = random.randint(10, 99)
    kq_de_g4_4 = random.randint(10, 99)
    
#################################

    #g5
    g_5_1 = random.randint(10, 99)
    kq_de_g5_1 = random.randint(10, 99)

    g_5_2 = random.randint(10, 99)
    kq_de_g5_2 = random.randint(10, 99)

    g_5_3 = random.randint(10, 99)
    kq_de_g5_3 = random.randint(10, 99)

    g_5_4 = random.randint(10, 99)
    kq_de_g5_4 = random.randint(10, 99)

    g_5_5 = random.randint(10, 99)
    kq_de_g5_5 = random.randint(10, 99)

    g_5_6 = random.randint(10, 99)
    kq_de_g5_6 = random.randint(10, 99)

#################################

    #g6
    g_6_1 = random.randint(1, 9)
    kq_de_g6_1 = random.randint(10, 99)

    g_6_2 = random.randint(1, 9)
    kq_de_g6_2 = random.randint(10, 99)

    g_6_3 = random.randint(1, 9)
    kq_de_g6_3 = random.randint(10, 99)
    chon_game = ""
    print("Tkc: ", tkc)
    print("""Chọn game:
             1 là Đề (1 ăn 90)
             2 là Lô (1 ăn 3)
             3 là Xiên hai (1 ăn 15)
             4 là Xiên ba (1 ăn 50)
             5 là Xiên bốn (1 ăn 120)
                         """)
    chon_game = int(input("Chọn: "))
    if chon_game == 1:
        print("Tkc: ", tkc)
        print("Bạn đang chọn đánh đề.")
        print("*LƯU Ý: Không được đặt số nhỏ 0 hoặc lớn hơn 99. Nếu không kết quả đặt sẽ không được tính và KHÔNG HOÀN TIỀN.")
        chon_so_de = int(input("Chọn số: "))
        tien_dat_de = int(input("Số tiền đặt: "))
        if tien_dat_de > tkc:
            print("Số dư không đủ.")
            break
        tkc -= tien_dat_de
        if chon_so_de == kq_de_db:
            tkc += tien_dat_de * 90
    
    if chon_game == 2:
        print("Tkc: ", tkc)
        print("Bạn đang chọn đánh lô.")
        print("*LƯU Ý: Không được đặt số nhỏ 0 hoặc lớn hơn 99. Nếu không kết quả đặt sẽ không được tính và KHÔNG HOÀN TIỀN.")
        chon_so_lo = int(input("Chọn số: "))
        tien_dat_lo = int(input("Số tiền đặt: "))
        if tien_dat_lo > tkc:
            print("Số dư không đủ.")
            break
        tkc -= tien_dat_lo
        if chon_so_lo == kq_de_db:
            tkc += tien_dat_lo * 3
        #g1
        if chon_so_lo == kq_de_g1:
            tkc += tien_dat_lo * 3
        #g2
        if chon_so_lo == kq_de_g2_1:
            tkc += tien_dat_lo * 3 
        if chon_so_lo == kq_de_g2_2:
            tkc += tien_dat_lo * 3 
        #g3
        if chon_so_lo == kq_de_g3_1:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g3_2:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g3_3:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g3_4:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g3_5:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g3_6:
            tkc += tien_dat_lo * 3
        #g4
        if chon_so_lo == kq_de_g4_1:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g4_2:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g4_3:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g4_4:
            tkc += tien_dat_lo * 3

        #g5
        if chon_so_lo == kq_de_g5_1:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g5_2:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g5_3:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g5_4:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g5_5:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g5_6:
            tkc += tien_dat_lo * 3

        #g6
        if chon_so_lo == kq_de_g6_1:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g6_2:
            tkc += tien_dat_lo * 3
        if chon_so_lo == kq_de_g6_3:
            tkc += tien_dat_lo * 3
        
        
    if chon_game == 3:
        print("Bạn đang chơi xiên hai.")
        print("*LƯU Ý: Không được đặt số nhỏ 0 hoặc lớn hơn 99. Nếu không kết quả đặt sẽ không được tính và KHÔNG HOÀN TIỀN.")
        chon_so_x2_1 = int(input("Chọn số lần 1: "))
        chon_so_x2_2 = int(input("Chọn số lần 2: "))
        tien_dat_x2 = int(input("Số tiền đặt: "))
        if tien_dat_x2 > tkc:
            print("Số dư không đủ.")
            break
        tkc -= tien_dat_x2

        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_db:
            tkc += tien_dat_x2 * 15
        #g1
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g1:
            tkc += tien_dat_x2 * 15
        #g2
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g2_1:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g2_2:
            tkc += tien_dat_x2 * 15
        
        #g3
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g3_1:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g3_2:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g3_3:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g3_4:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g3_5:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g3_6:
            tkc += tien_dat_x2 * 15
        
        #g4
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g4_1:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g4_2:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g4_3:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g4_4:
            tkc += tien_dat_x2 * 15
        
        #g5
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g5_1:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g5_2:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g5_3:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g5_4:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g5_5:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g5_6:
            tkc += tien_dat_x2 * 15
        
        #g6
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g6_1:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g6_2:
            tkc += tien_dat_x2 * 15
        if (chon_so_x2_1 and chon_so_x2_2) == kq_de_g6_3:
            tkc += tien_dat_x2 * 15
        
    if abcxyz == True:
        if chon_game == 4:
            print("Bạn đang chơi xiên ba.")
            print("*LƯU Ý: Không được đặt số nhỏ 0 hoặc lớn hơn 99. Nếu không kết quả đặt sẽ không được tính và KHÔNG HOÀN TIỀN.")
            chon_so_x3_1 = int(input("Chọn số thứ nhất: "))
            chon_so_x3_2 = int(input("Chọn số thứ hai: "))
            chon_so_x3_3 = int(input("Chọn số thứ ba: "))
            tien_dat_x3 = int(input("Nhập số tiền đặt: "))
            if tien_dat_x3 > tkc:
                print("Số dư không đủ.")
                break
            tkc -= tien_dat_x3

            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_db:
                tkc += tien_dat_x3 * 50
            
            #g1
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g1:
                tkc += tien_dat_x3 * 50
            
            #g2
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g2_1:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g2_2:
                tkc += tien_dat_x3 * 50
            
            #g3
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g3_1:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g3_2:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g3_3:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g3_4:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g3_5:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g3_6:
                tkc += tien_dat_x3 * 50
            
            #g4
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g4_1:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g4_2:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g4_3:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g4_4:
                tkc += tien_dat_x3 * 50
            
            #g5
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g5_1:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g5_2:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g5_3:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g5_4:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g5_5:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g5_6:
                tkc += tien_dat_x3 * 50
            
            #g6
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g6_1:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g6_2:
                tkc += tien_dat_x3 * 50
            if (chon_so_x3_1 and chon_so_x3_2 and chon_so_x3_3) == kq_de_g6_3:
                tkc += tien_dat_x3 * 50
    
    if chon_game == 5:
        print("Bạn đang chơi xiên bốn.")
        print("*LƯU Ý: Không được đặt số nhỏ 0 hoặc lớn hơn 99. Nếu không kết quả đặt sẽ không được tính và KHÔNG HOÀN TIỀN.")
        chon_so_x4_1 = int(input("Chọn số thứ nhất: "))
        chon_so_x4_2 = int(input("Chọn số thứ hai: "))
        chon_so_x4_3 = int(input("Chọn số thứ ba: "))
        chon_so_x4_4 = int(input("Nhập số thứ tư: "))
        tien_dat_x4 = int(input("Nhập số tiền đặt: "))
        if tien_dat_x4 > tkc:
            print("Số dư không đủ.")
            break
        tkc -= tien_dat_x4

        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_db:
            tkc += tien_dat_x4 * 125
        
        #g1
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g1:
            tkc += tien_dat_x4 * 125

        #g2
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g2_1:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g2_2:
            tkc += tien_dat_x4 * 125

        #g3
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g3_1:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g3_2:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g3_3:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g3_4:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g3_5:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g3_6:
            tkc += tien_dat_x4 * 125
        
        #g4
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g4_1:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g4_2:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g4_3:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g4_4:
            tkc += tien_dat_x4 * 125
        
        #g5
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g5_1:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g5_2:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g5_3:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g5_4:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g5_5:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g5_6:
            tkc += tien_dat_x4 * 125
        
        #g6
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g6_1:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g6_2:
            tkc += tien_dat_x4 * 125
        if (chon_so_x4_1 and chon_so_x4_2 and chon_so_x4_3 and chon_so_x4_4) == kq_de_g6_3:
            tkc += tien_dat_x4 * 125

    print("")
    print("G.ĐB:             ", db_1,kq_de_db, "   ")

    print("---.---.---.---.--.---.---.---.---.---")

    print("G.1:              ", g_1, kq_de_g1)

    print("---.---.---.---.--.---.---.---.---.---")

    print("G.2:       ",g_2_1,kq_de_g2_1, "     ",g_2_2,kq_de_g2_2)
    
    print("---.---.---.---.--.---.---.---.---.---")

    print("G.3: ",g_3_1,kq_de_g3_1, "     ", g_3_2, kq_de_g3_2, "     ", g_3_3,kq_de_g3_3)
    print("     ",g_3_4,kq_de_g3_4, "     ", g_3_5, kq_de_g3_5, "     ", g_3_6, kq_de_g3_6)

    print("---.---.---.---.--.---.---.---.---.---")

    print("G.4: ",g_4_1,kq_de_g4_1, "  ", g_4_2,kq_de_g4_2, "  ", g_4_3,kq_de_g4_3,"  ", g_4_4, kq_de_g4_4)

    print("---.---.---.---.--.---.---.---.---.---")

    print("G.5: ",g_5_1,kq_de_g5_1, "     ", g_5_2, kq_de_g5_2, "     ", g_5_3, kq_de_g5_3)
    print("     ",g_5_4,kq_de_g5_4, "     ", g_5_5, kq_de_g5_5, "     ", g_5_6, kq_de_g5_6)

    print("---.---.---.---.--.---.---.---.---.---")

    print("G.6: ", g_6_1, kq_de_g6_1, "       ", g_6_2, kq_de_g6_2, "       ", g_6_3, kq_de_g6_3)

    print("---.---.---.---.--.---.---.---.---.---")
    print("")

    input("Nhấn ENTER để tiếp tục.")
