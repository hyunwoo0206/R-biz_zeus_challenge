#!/usr/bin/python
# -*- coding: utf-8 -*-
## 1. 초기 설정① #######################################
# 라이브러리 가져오기
## 1．초기 설정 ①　모듈 가져오기 ######################
from i611_MCS import *
from teachdata import *
from i611_extend import *
from rbsys import *
from i611_common import *
from i611_io import *
from i611shm import * 
from zeusteach import *

def main():
    ## 1. 초기 설정② ####################################
    # i611 로봇 생성자
    rb = i611Robot()
    # 좌표계의 정의
    _BASE = Base()
    # 로봇과 연결 시작 초기화
    rb.open()
    # I/O 입출력 기능의 초기화 
    IOinit( rb )
    # 2.교시 데이터 생성
    zt             = ZeusTeach()       #ZEUS Teaching data     
    Joint_Start    = zt.TJoint(5)      # Start Joint  
    # Target Pickup 
    # 각 변수에 대한 좌표는 티칭 펜던트를 활용하여 직접 설정
    Pickup_A       = zt.TPosition(2)   # 물병 집는 위치 2개 생성
    BasePlace      = zt.TPosition(1)   # 시작점 위치 1개 생성
    PlaceA         = zt.TPosition(1)   # 던지는 동작시 이동할 지점 생성
    PlaceB         = zt.TPosition(1)
    PlaceC         = zt.TPosition(1)
    PlaceD         = zt.TPosition(1)
    for x in range(10):
        m = MotionParam( jnt_speed=30, lin_speed=30) #jnt_speed : Move함수 동작 시 속도설정 파라미터 / 단위 : %
                                                 #lin_speed : line함수 동작 시 속도설정 파라미터 / 단위 : mm/s                                                         
        #MotionParam 형으로 동작 조건 설정
        rb.motionparam( m )
        rb.set_mdo(mdoid = 2, portno=48, value=0, kind = 2, distance=230)
        rb.set_mdo(mdoid = 1, portno=50, value=1, kind = 2, distance=230)
        
        dout(48,'000') #ready
        rb.sleep(0.2)
        ##dout(48,'100') #ready
        rb.sleep(0.2)
        dout(48,'000') #ready
        rb.sleep(0.2)
        # Move Home 위치 이동
        rb.home()
        # Pickup_A[0] 위치로 이동
        rb.move( Pickup_A[0] ) # move() : PTP 동작을 실행하는 함수 => 관절이 목적지까지의 궤적이 곡선을 그리며 이동하는 동작
        rb.line( Pickup_A[1] ) # line() : 직선 보간 동작을 실행하는 함수 => 목적지까지의 궤적이 직선이 되도록 이동하는 동작
        dout(48,'001') # 그리퍼 잡는 동작
        rb.sleep(0.5) 
        rb.line( Pickup_A[0] )
        # BasePlace[0] 위치로 이동
        rb.move( BasePlace[0] )
        rb.sleep(5)
        m = MotionParam( jnt_speed=70.00, lin_speed=70.00, acctime = 0.05 , dacctime = 0.05) #jnt_speed : Move함수 동작 시 속도설정 파라미터 / 단위 : %
                                                    #lin_speed : line함수 동작 시 속도설정 파라미터 / 단위 : mm/s                                                         
        #MotionParam 형으로 동작 조건 설정
        rb.motionparam( m )
        rb.asyncm(1)

        # PlaceA~C[0] 위치로 이동
        rb.move( PlaceA[0] )
        #rb.move( PlaceB[0] )
        dout(48,'000') #ready
        rb.enable_mdo(2)
        rb.enable_mdo(1)
        # m = MotionParam( jnt_speed=57.45, lin_speed=57.45, acctime = 0.05 , dacctime = 0.05 ) # 동작 속도 증가
        # # acctime : 가속시간 설정 파라미터 => lin_speed , jnt_speed에서 설정한 속도에 도달하는 시간을 설정한다. 단위 : s
        # # dacctime : 감속 시간 설정 파라미터 => lin_speed , jnt_speed에서 설정한 속도에서 감속 정지할 때까지의 시간을 설정한다. 단위 : s
        # rb.motionparam( m )
        rb.move( PlaceC[0] )
        rb.move( PlaceD[0] )
        m = MotionParam( jnt_speed=20, lin_speed=20) # 동작 속도 증가
        rb.motionparam( m )
        rb.disable_mdo(3)
        rb.asyncm(2)
        #dout(48,'000')
        rb.home()
        rb.sleep(5)
    
 
    
    #MotionParam 형으로 동작 조건 설정         
if __name__ == '__main__':
    main()