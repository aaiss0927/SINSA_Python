from dataset import Dataset
from model import LinearRegression
from train import Trainer

def inference():
    # 데이터 로드
    dataset = Dataset('data.txt')
    x_data, y_data = dataset.get_data()
    
    # Todo

if __name__ == "__main__":
    inference()