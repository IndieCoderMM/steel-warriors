from arcade import FadeParticle


class Expolsion(FadeParticle):
    def __init__(self, img_path, x, y, lifetime):
        super().__init__(img_path, change_xy=(0, 0), center_xy=(x, y), lifetime=lifetime)

    def update(self):
        super().update()
        if self.can_reap():
            self.remove_from_sprite_lists()
