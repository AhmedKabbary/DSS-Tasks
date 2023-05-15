from joblib import load


class GenderPredictor:
    def __init__(self):
        self.model = load('model.joblib')

    def predict(self, info) -> str:
        result = self.model.predict([info])
        return result[0]

