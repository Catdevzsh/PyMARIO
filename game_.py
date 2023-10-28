from ursina import *

class MarioController(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.color = color.red
        self.scale_y = 2
        self.speed = 5

app = Ursina()

sky = Entity(model='sphere', color=color.cyan, scale=50)
ground = Entity(model='plane', texture='white_cube', color=color.green.tint(-0.4), scale=(100,1,100), collider='box')

# Create Platforms
platforms = [
    Entity(model='cube', texture='white_cube', position=(3,1,3), scale=(3,1,3), collider='box'),
    Entity(model='cube', texture='white_cube', position=(0,2,-5), scale=(3,1,3), collider='box'),
    Entity(model='cube', texture='white_cube', position=(5,3,-8), scale=(3,1,3), collider='box'),
    # ... (add more platforms as needed)
]

# Create a Goal
goal = Entity(model='cube', color=color.yellow, position=(8,4,-12), scale=(2,2,2), collider='box')

# Initialize Mario
mario = MarioController()

# Set up a basic third-person camera
camera.parent = mario
camera.position = (0, 2, -5)

def update():
    mario.x += held_keys['d'] * .1 * time.dt
    mario.x -= held_keys['a'] * .1 * time.dt
    mario.z += held_keys['w'] * .1 * time.dt
    mario.z -= held_keys['s'] * .1 * time.dt

    if held_keys['space']:
        mario.y += 1 * time.dt  # simple jump, you can improve this

app.run()
from ursina import *

class MarioController(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.color = color.red
        self.scale_y = 2
        self.speed = 5

app = Ursina()

sky = Entity(model='sphere', color=color.cyan, scale=50)
ground = Entity(model='plane', texture='white_cube', color=color.green.tint(-0.4), scale=(100,1,100), collider='box')

# Create Platforms
platforms = [
    Entity(model='cube', texture='white_cube', position=(3,1,3), scale=(3,1,3), collider='box'),
    Entity(model='cube', texture='white_cube', position=(0,2,-5), scale=(3,1,3), collider='box'),
    Entity(model='cube', texture='white_cube', position=(5,3,-8), scale=(3,1,3), collider='box'),
    # ... (add more platforms as needed)
]

# Create a Goal
goal = Entity(model='cube', color=color.yellow, position=(8,4,-12), scale=(2,2,2), collider='box')

# Initialize Mario
mario = MarioController()

# Set up a basic third-person camera
camera.parent = mario
camera.position = (0, 2, -5)

def update():
    mario.x += held_keys['d'] * .1 * time.dt
    mario.x -= held_keys['a'] * .1 * time.dt
    mario.z += held_keys['w'] * .1 * time.dt
    mario.z -= held_keys['s'] * .1 * time.dt

    if held_keys['space']:
        mario.y += 1 * time.dt  # simple jump, you can improve this

app.run()
