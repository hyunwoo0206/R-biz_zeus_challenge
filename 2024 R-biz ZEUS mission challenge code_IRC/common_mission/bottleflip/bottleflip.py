import cv2
import numpy as np

def process_largest_circle(circles, image, circle_color, flag):
    if circles is not None:
        flag[0] = 1  # 원이 검출되면 flag를 1로 설정
        largest_circle = circles[0]  # 가장 큰 원 초기화
        largest_radius = circles[0][2]

        # 가장 큰 원 찾기
        for circle in circles[1:]:
            radius = circle[2]
            if radius > largest_radius:
                largest_radius = radius
                largest_circle = circle

        # 가장 큰 원 그리기
        center = (int(largest_circle[0]), int(largest_circle[1]))
        radius = int(largest_circle[2])

        # 원을 그리고, 중심점과 반지름 정보 표시
        cv2.circle(image, center, radius, circle_color, 2)  # 가장 큰 원 그리기
        cv2.circle(image, center, 3, (0, 255, 0), -1)  # 중심점

        # 원을 포함하는 초록색 사각형 그리기
        bounding_box = (center[0] - radius, center[1] - radius, radius * 2, radius * 2)
        cv2.rectangle(image, (bounding_box[0], bounding_box[1]), (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), (0, 255, 0), 2)

        # 원의 중심 좌표 및 반지름 출력
        text = "Largest circle detected!"
        cv2.putText(image, text, (center[0] - 20, center[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, circle_color, 1, cv2.LINE_AA)
        
        return largest_radius

    return 0  # 원이 없는 경우 반지름 0 반환


def main():
    # 노란색 범위 설정 (HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # 웹캠 연결
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    flag = [0]  # flag를 리스트로 만들어 참조 가능하게 함
    largest_radius = 0

    while True:
        ret, frame = cap.read()  # 웹캠에서 프레임을 캡처
        if not ret:
            print("Error: Empty frame captured.")
            break

        # HSV 이미지로 변환
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 노란색 마스크 생성
        mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        # 가우시안 블러로 노이즈 제거
        blurred = cv2.GaussianBlur(mask_yellow, (9, 9), 2, 2)

        # 허프 변환을 사용하여 일정 크기의 원만 검출 (반지름 10 ~ 50 사이의 원만)
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=blurred.shape[0] / 8, param1=100, param2=30, minRadius=10, maxRadius=0)

        # 검출된 원 중 가장 큰 원만 표시
        radius = process_largest_circle(circles[0] if circles is not None else None, frame, (0, 255, 255), flag)

        # 처리된 이미지를 표시
        cv2.imshow("Processed Image", frame)

        # 원이 검출되었는지 확인 및 가장 큰 원의 반지름 출력
        if flag[0] == 1:
            print(f"Largest circle radius: {radius}")
        else:
            print("No circles detected.")

        # ESC 키로 종료
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
