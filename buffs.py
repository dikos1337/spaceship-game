from sprites import SpriteHealthRecovery
from config import Config


class BuffHealthRecovery(SpriteHealthRecovery):
    """Баф который востанавливает здоровье кораблю"""
    speedy = 5  # Скорость движения

    def update(self):
        """Обновление анимации падения бафа"""
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.top > Config.HEIGHT:
            self.kill()