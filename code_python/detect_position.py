from scipy.spatial import distance

x_coord = (
0.80625, 0.721875, 0.634375, 0.55, 0.4671875, 0.3875, 0.3046875, 0.221875, 0.140625, 0.05625
)

y_coord = (
0.94375, 0.83125, 0.7125, 0.6, 0.49166666666666664,
0.37916666666666665, 0.275, 0.1625, 0.058333333333333334
)

A1 = (x_coord[0], y_coord[0])
A2 = (x_coord[1], y_coord[0])
A3 = (x_coord[2], y_coord[0])
A4 = (x_coord[3], y_coord[0])
A5 = (x_coord[4], y_coord[0])
A6 = (x_coord[5], y_coord[0])
A7 = (x_coord[6], y_coord[0])
A8 = (x_coord[7], y_coord[0])
A9 = (x_coord[8], y_coord[0])
A10 = (x_coord[9], y_coord[0])
A = (A1, A2, A3, A4, A5, A6, A7, A8, A9, A10)

B1 = (x_coord[0], y_coord[1])
B2 = (x_coord[1], y_coord[1])
B3 = (x_coord[2], y_coord[1])
B4 = (x_coord[3], y_coord[1])
B5 = (x_coord[4], y_coord[1])
B6 = (x_coord[5], y_coord[1])
B7 = (x_coord[6], y_coord[1])
B8 = (x_coord[7], y_coord[1])
B9 = (x_coord[8], y_coord[1])
B10 = (x_coord[9], y_coord[1])
B = (B1, B2, B3, B4, B5, B6, B7, B8, B9, B10)

C1 = (x_coord[0], y_coord[2])
C2 = (x_coord[1], y_coord[2])
C3 = (x_coord[2], y_coord[2])
C4 = (x_coord[3], y_coord[2])
C5 = (x_coord[4], y_coord[2])
C6 = (x_coord[5], y_coord[2])
C7 = (x_coord[6], y_coord[2])
C8 = (x_coord[7], y_coord[2])
C9 = (x_coord[8], y_coord[2])
C10 = (x_coord[9], y_coord[2])
C = (C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)

D1 = (x_coord[0], y_coord[3])
D2 = (x_coord[1], y_coord[3])
D3 = (x_coord[2], y_coord[3])
D4 = (x_coord[3], y_coord[3])
D5 = (x_coord[4], y_coord[3])
D6 = (x_coord[5], y_coord[3])
D7 = (x_coord[6], y_coord[3])
D8 = (x_coord[7], y_coord[3])
D9 = (x_coord[8], y_coord[3])
D10 = (x_coord[9], y_coord[3])
D = (D1, D2, D3, D4, D5, D6, D7, D8, D9, D10)

E1 = (x_coord[0], y_coord[4])
E2 = (x_coord[1], y_coord[4])
E3 = (x_coord[2], y_coord[4])
E4 = (x_coord[3], y_coord[4])
E5 = (x_coord[4], y_coord[4])
E6 = (x_coord[5], y_coord[4])
E7 = (x_coord[6], y_coord[4])
E8 = (x_coord[7], y_coord[4])
E9 = (x_coord[8], y_coord[4])
E10 = (x_coord[9], y_coord[4])
E = (E1, E2, E3, E4, E5, E6, E7, E8, E9, E10)

F1 = (x_coord[0], y_coord[5])
F2 = (x_coord[1], y_coord[5])
F3 = (x_coord[2], y_coord[5])
F4 = (x_coord[3], y_coord[5])
F5 = (x_coord[4], y_coord[5])
F6 = (x_coord[5], y_coord[5])
F7 = (x_coord[6], y_coord[5])
F8 = (x_coord[7], y_coord[5])
F9 = (x_coord[8], y_coord[5])
F10 = (x_coord[9], y_coord[5])
F = (F1, F2, F3, F4, F5, F6, F7, F8, F9, F10)

G1 = (x_coord[0], y_coord[6])
G2 = (x_coord[1], y_coord[6])
G3 = (x_coord[2], y_coord[6])
G4 = (x_coord[3], y_coord[6])
G5 = (x_coord[4], y_coord[6])
G6 = (x_coord[5], y_coord[6])
G7 = (x_coord[6], y_coord[6])
G8 = (x_coord[7], y_coord[6])
G9 = (x_coord[8], y_coord[6])
G10 = (x_coord[9], y_coord[6])
G = (G1, G2, G3, G4, G5, G6, G7, G8, G9, G10)

H1 = (x_coord[0], y_coord[7])
H2 = (x_coord[1], y_coord[7])
H3 = (x_coord[2], y_coord[7])
H4 = (x_coord[3], y_coord[7])
H5 = (x_coord[4], y_coord[7])
H6 = (x_coord[5], y_coord[7])
H7 = (x_coord[6], y_coord[7])
H8 = (x_coord[7], y_coord[7])
H9 = (x_coord[8], y_coord[7])
H10 = (x_coord[9], y_coord[7])
H = (H1, H2, H3, H4, H5, H6, H7, H8, H9, H10)

I1 = (x_coord[0], y_coord[8])
I2 = (x_coord[1], y_coord[8])
I3 = (x_coord[2], y_coord[8])
I4 = (x_coord[3], y_coord[8])
I5 = (x_coord[4], y_coord[8])
I6 = (x_coord[5], y_coord[8])
I7 = (x_coord[6], y_coord[8])
I8 = (x_coord[7], y_coord[8])
I9 = (x_coord[8], y_coord[8])
I10 = (x_coord[9], y_coord[8])
I = (I1, I2, I3, I4, I5, I6, I7, I8, I9, I10)

pos = (A, B, C, D, E, F, G, H, I)

piece_classes = (
'black_bishop', 'black_cannon', 'black_guard', 'black_king',
'black_knight', 'black_pawn', 'black_rook', 'red_bishop',
'red_cannon', 'red_guard', 'red_king', 'red_knight', 'red_pawn', 'red_rook'
)

def detect_position(path):
    with open(path, 'r') as f:
        l_strip = [s.strip() for s in f.readlines()]
        # print(l_strip[0].split())
        res = []
        for line in l_strip:
            data = line.split()
            piece = piece_classes[int(data[0])]
            #print(piece)
            x_center = float(data[1])
            y_center = float(data[2])
            center = (x_center, y_center)
            x_value = float(data[3])
            y_value = float(data[4])
            min_dis = distance.euclidean(center, pos[0][0])
            x_min_index = 0
            y_min_index = 0
            for i in range(0, 9):
                for j in range(0, 10):
                    dis = distance.euclidean(center, pos[i][j])
                    if dis < min_dis:
                        min_dis = dis
                        x_min_index = i
                        y_min_index = j
            res.append(piece + ' ' + chr(ord('A') + x_min_index) + str(y_min_index + 1))
            # res.append(piece + ' ' + chr(ord('A') + x_min_index) + chr(ord('A') + y_min_index))
        return res

def detect_move(path_last, path_new):
    list1 = detect_position(path_last)
    list2 = detect_position(path_new)
    res1 = list(set(list1) - set(list2))
    res2 = list(set(list2) - set(list1))
    # print(res1)
    # print(res2)
    term1 = res1[0].split(' ')
    term1_ = res1[-1].split(' ')
    term2 = res2[0].split(' ')
    if term1[1] == term2[1]:
        pos_start = term1_[1]
        pos_end = term2[1]
    else:
        pos_start = term1[1]
        pos_end = term2[1]
    # print(pos_start, pos_end)
    is_exist = False#co an quan hay khong
    if term1 != term1_:
        is_exist = True
    return pos_start, pos_end, is_exist








