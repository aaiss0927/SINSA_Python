from dataset import Dataset
from model import LinearRegression
from train import Trainer

def inference():
    # 데이터 로드
    dataset = Dataset('data.txt')
    x_data, y_data = dataset.get_data()
    
    # 모델 초기화
    model = LinearRegression()
    
    # 학습된 파라미터 로드
    try:
        with open('model_weights.txt', 'r') as f:
            weights = f.read().split()
            model.w = float(weights[0])  # 가중치(w)
            model.b = float(weights[1])  # 편향(b)
    except FileNotFoundError:
        print("Error: 모델 가중치 파일을 찾을 수 없습니다. 학습을 먼저 수행하세요.")
        return

    # 사용자 입력값 받기
    while True:
        try:
            user_input = float(input("0에서 100 사이의 값을 입력해주세요: "))
            if 0 <= user_input <= 100:
                break
            else:
                print("100 초과 입력은 허용되지 않습니다. 다시 입력해주세요.")
        except ValueError:
            print("숫자만 입력해주세요.")

    # 예측 수행
    prediction = model.predict(user_input)

    # 결과 출력
    print(f"Input: {user_input:.2f}, Predicted: {prediction:.2f}")

if __name__ == "__main__":
        inference()
