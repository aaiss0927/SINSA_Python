class LinearRegression:
    """단순 선형 회귀 모델을 구현한 클래스입니다.

    이 클래스는 한 개의 입력 변수에 대한 선형 회귀를 수행합니다.
    예측값은 0.0에서 4.5 사이로 제한됩니다.

    속성:
        w (float): 가중치(weight) 파라미터
        b (float): 편향(bias) 파라미터
    """

    def __init__(self):
        """LinearRegression 모델을 초기화합니다.

        가중치(w)와 편향(b)을 0으로 초기화합니다.
        """
        self.w = 0
        self.b = 0
    
    def predict(self, x):
        """주어진 입력값에 대한 예측을 수행합니다.

        선형 방정식 (w * x + b)을 사용하여 예측을 수행하고,
        결과값을 0.0에서 4.5 사이로 제한합니다.

        Args:
            x (float): 입력값

        Returns:
            float: 0.0에서 4.5 사이의 예측값

        예시:
            >>> model = LinearRegression()
            >>> model.w = 0.5
            >>> model.b = 1.0
            >>> model.predict(2.0)
            2.0
        """
        result = self.w * x + self.b
        return max(0.0, min(4.5, result)) 
    
    def loss(self, x, y):
        """평균 제곱 오차(MSE) 손실을 계산합니다.

        Args:
            x (list): 입력값들의 리스트
            y (list): 실제 정답값들의 리스트

        Returns:
            float: 평균 제곱 오차 값

        참고:
            MSE = (1/n) * Σ(예측값 - 실제값)²
        """        
        n = len(x)
        total_error = 0
        
        for i in range(n):
            actual = y[i]
            predicted = self.predict(x[i])
            total_error += (actual - predicted) ** 2

        return total_error / n
    
    def gradient(self, x, y):
        """가중치와 편향에 대한 기울기를 계산합니다.

        MSE 손실 함수에 대한 가중치(w)와 편향(b)의 편미분을 계산합니다.

        Args:
            x (list): 입력값들의 리스트
            y (list): 실제 정답값들의 리스트

        Returns:
            tuple: (w_gradient, b_gradient)
                  - w_gradient (float): 가중치에 대한 기울기
                  - b_gradient (float): 편향에 대한 기울기

        참고:
            ∂MSE/∂w = (2/n) * Σ(예측값 - 실제값) * x
            ∂MSE/∂b = (2/n) * Σ(예측값 - 실제값)
        """
        n = len(x)
        w_grad = 0
        b_grad = 0
        
        for i in range(n):
            pred = self.predict(x[i])
            error = pred - y[i]
            w_grad += error * x[i]
            b_grad += error
        
        w_grad = w_grad * (2/n)
        b_grad = b_grad * (2/n)
        
        return w_grad, b_grad
