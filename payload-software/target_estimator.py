class TargetEstimator:
    def __init__(self, config=None):
        config = config or {}
        self.history = []
        self.baseline_signal = config.get('baseline_signal', 2.5)
        self.max_history = config.get('history_size', 5)

    def estimate(self, signal_value, mode='both'):
        if signal_value is None:
            return {
                'label': 'no signal',
                'distance_m': None,
                'confidence': 0,
                'mode': mode,
            }

        self.history.append(float(signal_value))
        if len(self.history) > self.max_history:
            self.history.pop(0)

        recent = self.history[-3:]
        persistence = sum(1 for value in recent if value >= self.baseline_signal) / max(1, len(recent))

        if mode == 'rescue':
            if signal_value <= 2:
                target_score = 80 + (2 - signal_value) * 8 + persistence * 10
                distance_m = max(8, int(180 - signal_value * 25 + (1 - persistence) * 20))
                label = 'possible buried target'
            elif signal_value == 3:
                target_score = 70 + persistence * 10
                distance_m = max(12, int(140 - signal_value * 20))
                label = 'possible target zone'
            elif signal_value == 4:
                target_score = 55 + persistence * 5
                distance_m = max(15, int(110 - signal_value * 15))
                label = 'nearby signal'
            else:
                target_score = 35 + (5 - signal_value) * 8
                distance_m = max(20, int(90 - signal_value * 10))
                label = 'strong but likely not target'

        elif mode == 'normal':
            target_score = min(100, int(signal_value * 20))
            distance_m = max(5, int(90 - signal_value * 12))
            label = 'nearby regular signal' if signal_value >= 3 else 'weak distant signal'

        else:
            rescue_estimate = self.estimate(signal_value, mode='rescue')
            normal_estimate = self.estimate(signal_value, mode='normal')
            if rescue_estimate['confidence'] >= normal_estimate['confidence']:
                return rescue_estimate
            return normal_estimate

        confidence = max(40, min(95, int(target_score)))
        return {
            'label': label,
            'distance_m': distance_m,
            'confidence': confidence,
            'mode': mode,
        }
