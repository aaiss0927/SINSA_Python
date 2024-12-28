import re

class Dataset:
    """학생의 점수와 학점 데이터를 분석하는 클래스입니다.

    텍스트 파일에서 학생 성적 데이터를 로드하고, 표시하며, 분석하는 기능을 제공합니다.
    점수-학점 관계의 시각화와 통계 분석을 지원합니다.

    속성:
        data (list): (이름, 점수, 학점)을 포함하는 튜플의 리스트
        x_data (list): 학생들의 점수 리스트
        y_data (list): 학생들의 학점 리스트
    """

    def __init__(self, file_path: str) -> None:
        """지정된 파일의 데이터로 Dataset을 초기화합니다.

        Args:
            file_path (str): 학생 정보가 포함된 데이터 파일 경로
        """
        self.data = []
        self.x_data = []
        self.y_data = []
        self._load_data(file_path)
    
    def _load_data(self, file_path : str):
        """지정된 파일에서 데이터를 로드하고 처리합니다.

        파일에서 학생 데이터를 읽어오며, 헤더 라인과 '*'로 시작하는 이름은 건너뜁니다.
        처리된 데이터는 클래스 속성에 저장됩니다.

        Args:
            file_path (str): 데이터 파일 경로

        참고:
            예상되는 파일 형식: 이름 점수 학점
            각 필드는 공백으로 구분되어야 합니다
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            # 헤더 건너뛰기
            next(f)
            for line in f:
                name, score, grade = line.strip().split()

                if re.match(r'^\*', name):
                    continue

                self.data.append((name, float(score), float(grade)))
                self.x_data.append(float(score))
                self.y_data.append(float(grade))

    def display_data_table(self, num_rows: int = 5) -> None:
        """학생 데이터를 형식화된 표로 표시합니다.

        Args:
            num_rows (int, optional): 표시할 행의 수. 기본값은 5입니다.

        예시:
            >>> dataset.display_data_table(3)
            Name      Score     Grade    
            ---------------------------
            홍길동     85.00     4.00
            김철수     92.50     4.30
            이영희     78.00     3.70
        """
        print(f"{'Name':<10} {'Score':<10} {'Grade':<10}")
        print("-" * 27)
        for i, (name, score, grade) in enumerate(self.data[:num_rows]):
            print(f"{name:<7} {score:<10.2f} {grade:<.2f}")

    def get_data(self):
        """점수와 학점 데이터를 반환합니다.

        Returns:
            tuple: (x_data, y_data)를 포함하는 튜플
                  x_data는 점수 리스트이고, y_data는 학점 리스트입니다
        """
        return self.x_data, self.y_data

if __name__ == "__main__":
    dataset = Dataset('data.txt')
    x_data, y_data = dataset.get_data()

    dataset.display_data_table(len(x_data))
    print(f"데이터 수: {len(x_data)}")