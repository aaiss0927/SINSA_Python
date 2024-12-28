class Trainer:
    """모델 학습을 담당하는 클래스입니다.

    경사 하강법(Gradient Descent)을 사용하여 모델의 파라미터를 최적화합니다.
    학습 과정에서 주기적으로 손실(loss) 값을 출력합니다.

    속성:
        model: 학습할 모델 객체
        lr (float): 학습률(learning rate)
        epochs (int): 전체 데이터셋에 대한 학습 반복 횟수
    """

    def __init__(self, model, learning_rate=0.0001, epochs=1000):
        """Trainer를 초기화합니다.

        Args:
            model: 학습할 모델 객체
            learning_rate (float, optional): 학습률. 기본값은 0.0001입니다.
            epochs (int, optional): 학습 에포크 수. 기본값은 1000입니다.
        """
        self.model = model
        self.lr = learning_rate
        self.epochs = epochs
    
    def train(self, x_data, y_data):
        """모델을 학습시킵니다.

        경사 하강법을 사용하여 모델의 파라미터를 최적화하고,
        100 에포크마다 현재 손실 값을 출력합니다.

        Args:
            x_data (list): 입력 데이터 리스트
            y_data (list): 정답 데이터 리스트

        참고:
            파라미터 업데이트 규칙:
            w = w - learning_rate * w_gradient
            b = b - learning_rate * b_gradient
        """
        for epoch in range(self.epochs):
            # gradient 계산
            # Todo
            # w_grad, b_grad = 
            w_grad, b_grad = self.model.gradient(x_data, y_data)
            # w - f'(w), b - f'(b)
            # 파라미터 업데이트
            # Todo
            # self.model.w -= 
            # self.model.b -= 
            self.model.w -= self.lr * w_grad
            self.model.b -= self.lr * b_grad
            # 100 epoch마다 loss 출력
            if (epoch + 1) % 100 == 0:
                # Todo
                # loss = 
                # print(f"Epoch {epoch+1}/{self.epochs}, Loss: {loss:.4f}")
                 if (epoch + 1) % 100 == 0:
                    loss = self.model.loss(x_data, y_data)
                    print(f"Epoch {epoch+1}/{self.epochs}, Loss: {loss:.4f}")