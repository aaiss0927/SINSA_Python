from dataset import Dataset
from model import LinearRegression
from train import Trainer

def inference():
    # 데이터 로드
    dataset = Dataset('data.txt')
    x_data, y_data = dataset.get_data()
    
    # 모델 생성 및 학습
    model = LinearRegression()
    trainer = Trainer(model)
    trainer.train(x_data, y_data)
    
    score = float(input())
    predicted_grade = model.predict(score)
    print(predicted_grade)

if __name__ == "__main__":
    inference()