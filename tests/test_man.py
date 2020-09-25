from entities.man import Man
from entity_parameters import EntityParameters as EP
import config as cfg
from position.position import Position
from logical_world import LogicalWorld
from draw import Draw


class MiniLogicalWorld(LogicalWorld):
    def __init__(self):
        pass


logical_world = MiniLogicalWorld()
man = Man(parameters={EP.POSITION: Position(left=0, right=cfg.CANVAS_WIDTH, top=0, bottom=cfg.CANVAS_HEIGHT)})
logical_world.entities = [man]
print(logical_world)
logical_world._create_parts_of_entities()

print(logical_world)


for e in logical_world.entities:
    e.parts = []

print(logical_world)

draw = Draw(logical_world)
draw.draw(save=True)