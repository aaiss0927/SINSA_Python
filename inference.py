from dataset import Dataset
from model import LinearRegression
from train import Trainer

def inference():
    # 데이터 로드
    dataset = Dataset('data.txt')
    x_data, y_data = dataset.get_data()
    
    # Todo
    model = LinearRegression()

    # 모델 학습
    trainer = Trainer(model)
    trainer.train(x_data, y_data)

    # 학습된 모델을 사용하여 예측
    predictions = model.predict(x_data)

    # 예측 결과 출력
    print("Predictions:", predictions)

if __name__ == "__main__":
    inference()