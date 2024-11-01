#!/usr/bin/python
# -*- coding: utf-8 -*-
from i611_MCS import *
from teachdata import *
from i611_extend import *
from rbsys import *
from i611_common import *
from i611_io import *
from i611shm import *
from draw_letter import *
from VEC import VECTOR
import socket
import json


init_x = -402.294
init_y = 250.342
init_z = 440
init_rz = -90
init_ry = 0
init_rx = 180.000


def main():
    # 초기 설정
    rb = i611Robot()
    _BASE = Base()
    rb.open()
    IOinit(rb)

    # creamside1      = Position(-239.160, 372.946, 351.396, 138.775, 5.843, -150.164)
    # creamside2      = Position(-247.772, 373.072, 384.528, 138.704, 5.796, -150.169)   #
    # creamfloor1     = Position(-335.769, 187.646 ,451.370, 135.611, -0.000, 180.000)
    # creamfloor2     = Position(-408.289, 200.538, 451.370, 135.611, -0.000, 180.000)  #
    # knifeside       = Position(-314.938, 285.212, 622.967, 135.582, -0.359, 176.216)    #
    # knifefloor      = Position(-213.812, 94.597, 410.953, 137.376, 1.096, 173.250)

    # 글씨 크기 설정
    VEC = VECTOR(10)

    # 로봇 속도 설정
    rb.override(50)  # 속도 50%
    m = MotionParam(lin_speed=15, overlap=1)
    rb.motionparam(m)
    # rb.set_mdo(mdoid = 1, portno=24, value=0, kind = 2, distance=0.5)
    # rb.set_mdo(mdoid = 2, portno=25, value=0, kind = 2, distance=0.5)

    # 소켓 연결 (로봇에서 Flask 서버로부터 데이터 수신)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.50', 5000))

    # ---------------------------통신 성공-------------------------------

    # --------------------------- 여기에다 생크림 바르는 로봇 동작하는 코드 작성하면댐 -----------------------
    # jnt_speed : Move함수 동작 시 속도설정 파라미터 / 단위 : %
    # m = MotionParam(jnt_speed=10, lin_speed=10)
    # lin_speed : line함수 동작 시 속도설정 파라미터 / 단위 : mm/s
    # MotionParam 형으로 동작 조건 설정
    # rb.motionparam(m)

    # rb.asyncm(1)

    # rb.move(creamside1)
    # jnt_speed : Move함수 동작 시 속도설정 파라미터 / 단위 : %
    # m = MotionParam(jnt_speed=1, lin_speed=10)
    # rb.motionparam(m)

    # dout(24,'1')
    # rb.enable_mdo(1)
    # rb.move(creamside2)
    # rb.sleep(1)
    # rb.disable_mdo(1)

    # m = MotionParam( jnt_speed=10, lin_speed=10) #jnt_speed : Move함수 동작 시 속도설정 파라미터 / 단위 : %
    # rb.motionparam( m )
    # rb.move(knifeside) #
    # rb.sleep(8)
    # rb.move(creamfloor1)
    # m = MotionParam( jnt_speed=1, lin_speed=10) #jnt_speed : Move함수 동작 시 속도설정 파라미터 / 단위 : %
    # rb.motionparam( m )
    # dout(24,'1')
    # rb.enable_mdo(1)
    # rb.move(creamfloor2)
    # rb.sleep(1)
    # m = MotionParam( jnt_speed=10, lin_speed=10) #jnt_speed : Move함수 동작 시 속도설정 파라미터 / 단위 : %
    # rb.motionparam( m )
    # rb.disable_mdo(1)
    # rb.move(knifefloor)
    # rb.sleep(10)

    init_pos = Position(x=init_x, y=init_y, z=init_z,
                        rz=-90, ry=init_ry, rx=init_rx)
    rb.move(init_pos)
    rb.sleep(1)

    # init_pos = Position(x=init_x, y=init_y, z=init_z,
    #                     rz=-180, ry=init_ry, rx=init_rx)
    # rb.move(init_pos)
    # rb.sleep(1)

    # init_pos = Position(x=init_x, y=init_y, z=init_z,
    #                     rz=90, ry=init_ry, rx=init_rx)
    # rb.move(init_pos)
    # rb.sleep(1)

    # init_pos = Position(x=init_x, y=init_y, z=init_z,
    #                     rz=0, ry=init_ry, rx=init_rx)
    # rb.move(init_pos)
    # rb.sleep(1)

    # ------------------------------end----------------------------------------------------------
    try:
        while True:
            # Flask 서버로부터 데이터를 받음
            received_data = client_socket.recv(1024).decode('utf-8')
            if not received_data:
                break  # 연결이 끊어졌을 경우 종료

            data = json.loads(received_data)

            # --------------------- 문자열 처리 ex) A, B, C ... --------------------------------
            # 문자 크기 바꾸려면 여기서 바꾸면 댐  VEC = VECTOR(10) 여기서 10이 문자 크기 의미함
            # 크림 색 바꾸는거도 여기서 바꾸면댐

            for item in data['coordinates']:
                x = item["x"]
                y = item["y"]
                character = item["character"]
                Color = item['color']
                # print("x: {}, y: {}, character: {}".format(x, y, character))

                # 문자 크기 설정
                VEC = VECTOR(13.5)

                # 로봇에서 좌표에 따라 문자 그리기
                # process_character(character, x, y, rb, Color, VEC)

            # 완료 후 Flask 서버에 응답 전송
            client_socket.send(json.dumps(
                {"status": "success"}).encode('utf-8'))

    except Exception as e:
        print("Error: {}".format(e))
    finally:
        client_socket.close()
        rb.close()


def process_character(character, x, y, rb, Color, VEC):
    # 문자에 따른 벡터 처리
    vecs = get_character_vectors(character, VEC, x, y)  # 기본 위치에서 글자 처리
    # 현재 로봇이 있는 위치 의미함

    new_rz = get_color(Color)
    init_rz = new_rz
    current_pos = Position(x, y, init_z, init_rz, init_ry, init_rx)
    rb.line(current_pos)
    print("rz: {}".format(init_rz))
    # 위의 current_pos 에서 p_next 위치로 움직임
    p_next = Position(x, y, init_z, init_rz, init_ry, init_rx)

    i = 0
    # ------------------- 문자열 한 획 처리 ex) 직선 또는 곡선 -----------------------
    for vec in vecs:
        # 현재 위치한 로봇의 좌표를 XY 좌표계로 불러옴 [x, y, z, rz, ry, rx]
        current = current_pos.pos2list()

        # 한 획을 그릴때의 시작 좌표 ex) 직선인경우 [1, 2] -> [3, 5]로 간다했을때 [1, 2]를 의미함
        start = vec[0]

        # ----------------로봇의 현재 위치와 획을 그리는 시작좌표랑 다른경우 --> 크림 짜는행동 멈추어야함 ------------
        if (current[0] != start[0]) or (current[1] != start[1]):

            # ---------------------여기에다가 크림짜는거 멈추는 코드 작성하면댐 ---------------------------
            dout(25, '0')
            rb.sleep(1.25)

            # current_pos = current_pos.replace(
            #     current[0], current[1], init_z+50, init_rz, init_ry, init_rx)
            # rb.move(current_pos)
            # current_pos = current_pos.replace(
            #     start[0], start[1], init_z+50, init_rz, init_ry, init_rx)

            # -------------------------------------- end -----------------------------------------------

        # 획 그리는 시작 위치로 이동

        p0 = Position(start[0], start[1], init_z, init_rz, init_ry, init_rx)
        rb.line(p0)

        # 비동기 시작
        dout(25, '1')
        rb.sleep(1.1)
        rb.asyncm(1)
        # 획 그리기 동작 실행 시작한 좌표 그 다음부터 실행하므로 인덱스 1부터 시작함
        for i in range(1, len(vec)):
            next_point = vec[i]
            p_next = Position(
                next_point[0], next_point[1], init_z, init_rz, init_ry, init_rx)
            rb.line(p_next)

        # 모든 행동 대기 후 비동기 해제
        rb.join()
        rb.asyncm(2)

        # 마지막 로봇 위치를 현재위치로 저장
        current_pos = p_next.copy()
        i += 1
    dout(25, '0')

# 생크림 = -90
# 카라멜 = -180
# 초코 = 90
# 딸기 = 0


def get_color(Color):
    if Color == 'Strawberry':
        return 0
    elif Color == 'Caramel':
        return -180
    elif Color == 'Choco':
        return 90


def get_character_vectors(char, VEC, x, y):
    if char == "A":
        return draw_letter_A(VEC, x, y)
    elif char == "B":
        return draw_letter_B(VEC, x, y)
    elif char == "C":
        return draw_letter_C(VEC, x, y)
    elif char == "D":
        return draw_letter_D(VEC, x, y)
    elif char == "E":
        return draw_letter_E(VEC, x, y)
    elif char == "F":
        return draw_letter_F(VEC, x, y)
    elif char == "G":
        return draw_letter_G(VEC, x, y)
    elif char == "H":
        return draw_letter_H(VEC, x, y)
    elif char == "I":
        return draw_letter_I(VEC, x, y)
    elif char == "J":
        return draw_letter_J(VEC, x, y)
    elif char == "K":
        return draw_letter_K(VEC, x, y)
    elif char == "L":
        return draw_letter_L(VEC, x, y)
    elif char == "M":
        return draw_letter_M(VEC, x, y)
    elif char == "N":
        return draw_letter_N(VEC, x, y)
    elif char == "O":
        return draw_letter_O(VEC, x, y)
    elif char == "P":
        return draw_letter_P(VEC, x, y)
    elif char == "Q":
        return draw_letter_Q(VEC, x, y)
    elif char == "R":
        return draw_letter_R(VEC, x, y)
    elif char == "S":
        return draw_letter_S(VEC, x, y)
    elif char == "T":
        return draw_letter_T(VEC, x, y)
    elif char == "U":
        return draw_letter_U(VEC, x, y)
    elif char == "V":
        return draw_letter_V(VEC, x, y)
    elif char == "W":
        return draw_letter_W(VEC, x, y)
    elif char == "X":
        return draw_letter_X(VEC, x, y)
    elif char == "Y":
        return draw_letter_Y(VEC, x, y)
    elif char == "Z":
        return draw_letter_Z(VEC, x, y)

    # Add similar conditions for other characters...
    else:
        return []


if __name__ == '__main__':
    main()
