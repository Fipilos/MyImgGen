from entities.head import Head
import config as cfg
from entity_parameters import EntityParameters as EP
from position.position import Position
from logical_world import LogicalWorld
from draw import Draw


head = Head(parameters={EP.POSITION: Position(left=0, top=0, right=cfg.CANVAS_WIDTH, bottom=cfg.CANVAS_HEIGHT),
                        EP.TYPE: 'woman'})
print('head',head)

class MiniLogicalWorld(LogicalWorld):
    def __init__(self):
        pass


logical_world = MiniLogicalWorld()

logical_world.entities = [head]
print(logical_world)
logical_world._create_parts_of_entities()

draw = Draw(logical_world)
draw.draw(save=True)