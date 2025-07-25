import serial
import time
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.setup(width = 640, height = 480)

# 전역 변수 설정
connection = None
current_distance = 0

def connect_sensor(port = 'COM3'):
    global connection
    try:
        connection = serial.Serial(port, 9600)
        time.sleep(2)
        print("연결 성공")
        return True
    except:
        print("연결 실패")
        return False
    
def read_distance():
    global connection, current_distance
    if connection and connection.in_waiting > 0:
        data = connection.readline().decode().strip()
        try:
            distance = float(data)
            current_distance = distance
            return distance
        except:
            pass
    return None

def main():
    if connect_sensor():
        while True:
            dist = read_distance()
            if dist > 10.0:
                print(f"거리: {dist}cm")
                t.forward(5)
                time.sleep(0.1)
            else:
                print(f"{dist}cm 앞에서 장애물 감지")
                return
                
if __name__ == "__main__":
    main()