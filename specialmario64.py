from ursina import *

class MarioController(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.color = color.red
        self.scale_y = 2
        self.speed = 5
        self.jump_height = 2
        self.gravity = 0.5  # Adjust gravity for realistic effect
        self.y_speed = 0
        self.grounded = False

    def update(self):
        self.apply_gravity()
        self.movement()

    def movement(self):
        self.x += held_keys['d'] * self.speed * time.dt
        self.x -= held_keys['a'] * self.speed * time.dt
        self.z += held_keys['w'] * self.speed * time.dt
        self.z -= held_keys['s'] * self.speed * time.dt

    def apply_gravity(self):
        if not self.grounded:
            self.y_speed -= self.gravity * time.dt
            self.y += self.y_speed * time.dt

            # Check if Mario is on the ground
            if self.y <= 0:
                self.y = 0
                self.y_speed = 0
                self.grounded = True

    def input(self, key):
        if key == 'space' and self.grounded:
            # Apply jump force
            self.y_speed = self.jump_height
            self.grounded = False

app = Ursina()

# 3D setup
camera.orthographic = False
camera.position = (0, 5, -10)  # Adjusted camera position
camera.rotation = (30, 0, 0)   # Rotated camera to face the level

sky = Entity(model='sphere', color=color.cyan, scale=50)
ground = Entity(model='plane', texture='white_cube', color=color.green.tint(-0.4), scale=(200, 200), collider='box')

platforms = [
    Entity(model='cube', texture='white_cube', position=(3,1,3), scale=(3,1,3), collider='box'),
    Entity(model='cube', texture='white_cube', position=(0,2,-5), scale=(3,1,3), collider='box'),
    Entity(model='cube', texture='white_cube', position=(5,3,-8), scale=(3,1,3), collider='box'),
]

goal = Entity(model='cube', color=color.yellow, position=(8,4,-12), scale=(2,2,2), collider='box')

mario = MarioController()

def update():
    mario.x += held_keys['d'] * mario.speed * time.dt
    mario.x -= held_keys['a'] * mario.speed * time.dt
    mario.z += held_keys['w'] * mario.speed * time.dt
    mario.z -= held_keys['s'] * mario.speed * time.dt

    if held_keys['space'] and mario.grounded:
        mario.input('space')

    camera.rotation_y += mouse.velocity[0] * 0.1
    camera.rotation_x -= mouse.velocity[1] * 0.1

app.run()
