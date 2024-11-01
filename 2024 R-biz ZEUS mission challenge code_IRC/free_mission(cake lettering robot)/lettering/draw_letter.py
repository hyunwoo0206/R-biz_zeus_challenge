#!/usr/bin/python
# -*- coding: utf-8 -*-
def draw_letter_A(vec, x, y):
    line1 = vec.draw_diagonal_backward(
        x + 0.5 * vec.scale, y, 1, 2)  # Left diagonal
    line2 = vec.draw_diagonal_forward(
        x + 0.5 * vec.scale, y, 1, 2)   # Right diagonal
    line3 = vec.draw_Horizontal(
        x, y - vec.scale, 1)                  # Horizontal
    return [line1, line2, line3]


def draw_letter_B(vec, x, y):
    line1 = vec.draw_Vertical(x, y, 2)  # Main vertical line
    curve1 = vec.draw_curve(x + 0.5 * vec.scale, y - 0.5 *
                            vec.scale, 0.5 * vec.scale, 90, -90)  # Top curve
    curve2 = vec.draw_curve(x + 0.5 * vec.scale, y - 1.5 *
                            vec.scale, 0.5 * vec.scale, 90, -90)  # Bottom curve
    line2 = vec.draw_Horizontal(x, y, 0.5)  # Top small horizontal line
    # Middle small horizontal line
    line3 = vec.draw_Horizontal(x, y - vec.scale, 0.5)
    # Bottom small horizontal line
    line4 = vec.draw_Horizontal(x, y - 2 * vec.scale, 0.5)
    a = line4[0]
    b = line4[1]
    line4 = [b, a]
    return [line1, line2, curve1, line3, curve2,  line4]


def draw_letter_C(vec, x, y):
    curve = vec.draw_curve(x + 1 * vec.scale, y -
                           vec.scale, 1 * vec.scale, 90, 270)
    return [curve]


def draw_letter_D(vec, x, y):
    # D는 반원을 그리는 곡선과 수직선으로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    curve1 = vec.draw_curve(x, y -
                            1 * vec.scale, 1 * vec.scale, 90, -90)
    return [line1, curve1]


def draw_letter_E(vec, x, y):
    # E는 수직선과 수평선 3개로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    line2 = vec.draw_Horizontal(x, y, 1)
    line3 = vec.draw_Horizontal(x, y - vec.scale, 1)
    line4 = vec.draw_Horizontal(x, y - 2 * vec.scale, 1)
    return [line1, line2, line3, line4]


def draw_letter_F(vec, x, y):
    # F는 수직선과 수평선 2개로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    line2 = vec.draw_Horizontal(x, y, 1)
    line3 = vec.draw_Horizontal(x, y - vec.scale, 0.8)
    return [line1, line2, line3]


def draw_letter_G(vec, x, y):
    # G는 반원과 수평선으로 구성
    curve1 = vec.draw_curve(x + 0.5 * vec.scale, y -
                            vec.scale, 1 * vec.scale, 70, 290)
    line1 = vec.draw_Horizontal(x + 0.4 * vec.scale, y - 1.5 * vec.scale, 0.5)
    line2 = vec.draw_Vertical(x + 0.9*vec.scale, y - 1.5 * vec.scale, 0.5)
    return [curve1, line1, line2]


def draw_letter_H(vec, x, y):
    # H는 두 개의 수직선과 중간 수평선으로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    line2 = vec.draw_Vertical(x + vec.scale, y, 2)
    line3 = vec.draw_Horizontal(x, y - vec.scale, 1)
    return [line1, line2, line3]


def draw_letter_I(vec, x, y):
    # I는 하나의 수직선으로 구성
    line1 = vec.draw_Vertical(x + 0.5 * vec.scale, y, 2)
    return [line1]


def draw_letter_J(vec, x, y):
    # J는 수직선과 곡선으로 구성
    line1 = vec.draw_Vertical(x + vec.scale, y, 1.5)
    curve1 = vec.draw_curve(x + 0.5 * vec.scale, y -
                            1.5 * vec.scale, 0.5 * vec.scale, 180, 360)
    return [line1, curve1]


def draw_letter_K(vec, x, y):
    # K는 수직선과 두 개의 대각선으로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    diagonal1 = vec.draw_diagonal_forward(x, y - vec.scale, 1, 1)
    diagonal2 = vec.draw_diagonal_backward(x, y - vec.scale, -1, -1)
    return [line1, diagonal1, diagonal2]


def draw_letter_L(vec, x, y):
    # L은 수직선과 수평선으로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    line2 = vec.draw_Horizontal(x, y - 2 * vec.scale, 1)
    return [line1, line2]


def draw_letter_M(vec, x, y):
    # M은 두 개의 수직선과 두 개의 대각선으로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    diagonal1 = vec.draw_diagonal_forward(x, y, 0.8, 1)
    diagonal2 = vec.draw_diagonal_backward(
        diagonal1[1][0], diagonal1[1][1], -0.8, -1)
    line2 = vec.draw_Vertical(diagonal2[1][0], diagonal2[1][1], 2)
    return [line1, diagonal1, diagonal2, line2]


def draw_letter_N(vec, x, y):
    # N은 두 개의 수직선과 대각선으로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    diagonal = vec.draw_diagonal_forward(x, y, 1.5, 2)
    line2 = vec.draw_Vertical(diagonal[1][0], diagonal[1][1], -2)
    return [line1, diagonal, line2]


def draw_letter_O(vec, x, y):
    # O는 원으로 구성
    curve1 = vec.draw_curve(x + 0.5 * vec.scale, y -
                            vec.scale, 1 * vec.scale, 0, 360)
    return [curve1]


def draw_letter_P(vec, x, y):
    # P는 수직선과 반원으로 구성
    line1 = vec.draw_Vertical(x, y, 2)
    line2 = vec.draw_Horizontal(x, y, 0.5)
    curve1 = vec.draw_curve(line2[1][0], line2[1][1]-0.5 * vec.scale, 0.5 * vec.scale, 90, -90)
    line3 = vec.draw_Horizontal(curve1[-1][0], curve1[-1][1], -0.5)
    return [line1, line2, curve1, line3]


def draw_letter_Q(vec, x, y):
    # Q는 원과 대각선으로 구성
    curve1 = vec.draw_curve(x + 0.5 * vec.scale, y -
                            vec.scale, 1 * vec.scale, 0, 360)
    diagonal = vec.draw_diagonal_forward(
        x + 0.75 * vec.scale, y - 1.65 * vec.scale, 0.5, 0.5)
    return [curve1, diagonal]


def draw_letter_R(vec, x, y):
    # R은 P에서 대각선을 추가
    lines = draw_letter_P(vec, x, y)
    diagonal = vec.draw_diagonal_backward(
        lines[-1][0][0], lines[-1][0][1], -0.5, 1)
    
    lines.append(diagonal)
    return lines


def draw_letter_S(vec, x, y):
    # S는 위쪽 반원과 아래쪽 반원으로 구성
    curve1 = vec.draw_curve(x + 0.5 * vec.scale, y -
                            0.5 * vec.scale, 0.5 * vec.scale, 50, 270)  # 위쪽 반원
    curve2 = vec.draw_curve(x + 0.5 * vec.scale, y - 1.5 * vec.scale,
                            0.5 * vec.scale, 90, -130)  # 아래쪽 반원 (오른쪽으로 약간 이동)
    return [curve1, curve2]


def draw_letter_T(vec, x, y):
    # T는 수직선과 수평선으로 구성
    line1 = vec.draw_Vertical(x + 0.5 * vec.scale, y, 2)
    line2 = vec.draw_Horizontal(x, y, 1)
    return [line1, line2]


def draw_letter_U(vec, x, y):
    # 수직선 사이의 간격을 넓히고 반원의 크기를 조정
    line1 = vec.draw_Vertical(x, y, 1.5)  # 왼쪽 수직선
    curve1 = vec.draw_curve(x + vec.scale, y - 1.5 *
                            vec.scale, vec.scale, 180, 360)  # 아래쪽 반원
    line2 = vec.draw_Vertical(x + 2 * vec.scale, y, 1.5)  # 오른쪽 수직선
    return [line1, line2, curve1]


def draw_letter_V(vec, x, y):
    # V는 두 개의 대각선으로 구성
    diagonal1 = vec.draw_diagonal_backward(x, y, -1, 2)
    diagonal2 = vec.draw_diagonal_forward(
        diagonal1[1][0], diagonal1[1][1], 1, -2)
    return [diagonal1, diagonal2]


def draw_letter_W(vec, x, y):
    # W는 V와 같은 구조로 대각선을 4개 사용
    diagonal1 = vec.draw_diagonal_backward(x, y, -0.5, 2)
    diagonal2 = vec.draw_diagonal_forward(
        diagonal1[1][0], diagonal1[1][1], 0.5, -2)
    diagonal3 = vec.draw_diagonal_backward(
        diagonal2[1][0], diagonal2[1][1], -0.5, 2)
    diagonal4 = vec.draw_diagonal_forward(
        diagonal3[1][0], diagonal3[1][1], 0.5, -2)
    return [diagonal1, diagonal2, diagonal3, diagonal4]


def draw_letter_X(vec, x, y):
    # X는 두 개의 대각선으로 구성
    diagonal1 = vec.draw_diagonal_forward(x, y, 1, 2)  # 좌상에서 우하로 향하는 대각선
    diagonal2 = vec.draw_diagonal_backward(
        x + vec.scale, y, 1, 2)  # 우상에서 좌하로 향하는 대각선
    return [diagonal1, diagonal2]


def draw_letter_Y(vec, x, y):
    # Y는 두 개의 대각선과 하나의 수직선으로 구성
    diagonal1 = vec.draw_diagonal_backward(x, y, -0.5, 1)
    diagonal2 = vec.draw_diagonal_forward(x + vec.scale, y, -0.5, 1)
    line1 = vec.draw_Vertical(x + 0.5 * vec.scale, y - vec.scale, 1)
    return [diagonal1, diagonal2, line1]


def draw_letter_Z(vec, x, y):
    # Z는 두 개의 수평선과 하나의 대각선으로 구성
    line1 = vec.draw_Horizontal(x, y, 1)
    diagonal = vec.draw_diagonal_forward(line1[1][0], line1[1][1], -1, 2)
    line2 = vec.draw_Horizontal(diagonal[1][0], diagonal[1][1], 1)
    return [line1, diagonal, line2]
