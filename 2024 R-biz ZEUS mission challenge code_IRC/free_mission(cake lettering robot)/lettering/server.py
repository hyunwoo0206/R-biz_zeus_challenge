from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import socket
import json
import math
import matplotlib
matplotlib.use('Agg')  # GUI 백엔드 대신 Agg 백엔드 사용

import matplotlib.pyplot as plt

import os

app = Flask(__name__)
CORS(app)  # 모든 출처에서의 접근을 허용합니다.

# 이미지 서빙을 위한 라우트 추가
@app.route('/images/<filename>')
def get_image(filename):
    image_folder = r'C:\Users\seunga\Desktop\제우스\ZEUS Flask\coordinate_img'
    return send_from_directory(image_folder, filename)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 좌표 데이터를 최적 경로로 정렬하는 함수
def sort_coordinates(coordinate_data, start_x=0, start_y=0):
    sorted_data = []
    current_x, current_y = start_x, start_y

    while coordinate_data:
        nearest_point = min(coordinate_data, key=lambda point: calculate_distance(
            current_x, current_y, point['x'], point['y']))
        sorted_data.append(nearest_point)
        coordinate_data.remove(nearest_point)
        current_x, current_y = nearest_point['x'], nearest_point['y']

    return sorted_data

# 받은 좌표 데이터를 플롯하고 이미지를 저장하는 함수
def plot_coordinates(sorted_data):
    # print(sorted_data[0]['x'])
    x_coords = [point['x'] for point in sorted_data]
    y_coords = [point['y'] for point in sorted_data]
    characters = [point['character'] for point in sorted_data]
    colors = [point['color'] for point in sorted_data]

    # 색상 이름 매핑 (HEX 코드 기반)
    # color_names = {
    #     'rgb(252, 90, 141)': 'Strawberry',  # 딸기색
    #     'rgb(198, 142, 23)': 'Caramel',     # 카라멜색
    #     'rgb(139, 69, 19)': 'Choco'         # 초코색
    # }

    # 플롯을 설정하고 좌표 그리기
    plt.figure(figsize=(6, 6))
    plt.scatter(x_coords, y_coords, color='blue', s=100, zorder=4)

 # 각 좌표에 대응하는 문자를 플롯 위에 표시
    for i, character in enumerate(characters):
        # color_name = color_names.get(colors[i], 'Unknown')
        color_name = colors[i]
        plt.text(x_coords[i], y_coords[i], f"{character}, {color_name}",
                 fontsize=12, ha='center', color='red')

    # 케이크 원의 경계를 그리기
    cake_radius = 100
    circle = plt.Circle((-400, 200), cake_radius,
                        color='orange', fill=False, linestyle='--')
    plt.gca().add_artist(circle)

    # 플롯의 범위와 스타일 설정
    plt.xlim(-520, -270)
    plt.ylim(80, 320)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.title("Robot Path Plot on Cake Coordinates")
    # plt.show()

    # 지정된 경로에 이미지 저장
    image_folder = r'C:\Users\seunga\Desktop\제우스\ZEUS Flask\coordinate_img'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # 이미지 파일로 저장
    image_path = os.path.join(image_folder, 'coordinates_plot.png')
    plt.savefig(image_path)
    plt.close()
# 소켓 통신을 통해 로봇에게 전체 좌표 데이터를 한 번에 전송하는 함수


def start_socket_server(sorted_data):
    # 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.50', 5000))  # 서버 IP와 포트 설정
    server_socket.listen(1)  # 연결 대기
    print("Waiting for robot connection...")

    client_socket, addr = server_socket.accept()  # 연결 수락
    print(f"Connected to {addr}")

    try:
        # 정렬된 전체 좌표 배열을 JSON 형식으로 변환하여 한 번에 전송
        message = json.dumps({"coordinates": sorted_data})
        client_socket.sendall(message.encode('utf-8'))  # 전체 데이터 전송
        print(f"Sent to robot: {message}")

        # 로봇으로부터 응답 받기
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Response from robot: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        server_socket.close()

# 기본 라우트


@app.route('/')
def home():
    return render_template('index.html')

# 데이터 처리 및 소켓 서버 실행


@app.route('/sendData', methods=['POST'])
def receive_data():
    data = request.get_json()
    # print("Received data:", data)  # 받은 데이터를 출력하여 확인

    # 각 딕셔너리 단위로 처리하기
    for item in data:
        print("-------------------")
        print(f"Character: {item['character']}")
        print(f"Color: {item['color']}")
        print(f"X: {item['x']}")
        print(f"Y: {item['y']}")
        
    print("-------------------")

    if isinstance(data, list):
        # 좌표를 (0, 0)에서 시작하여 정렬
        sorted_data = sort_coordinates(data, start_x=-520, start_y=80)

        # # 정렬된 전체 데이터를 소켓 서버로 전송
        start_socket_server(sorted_data)

        # 정렬된 좌표를 플롯하여 이미지로 저장
        # plot_coordinates(sorted_data)
        image_url = '/images/coordinates_plot.png'
        return jsonify({"status": "success", "image_url": image_url}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data format"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
