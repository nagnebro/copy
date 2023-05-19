from ursina import *


class Inventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.015),
            texture = 'white_cube',
            texture_scale = (5,1),
            scale = (1, .1),
            origin = (-.5, .5),
            position = (-.5,-.35, 7),
            color = color.color(0,0,.1,.9)
            )

        for key, value in kwargs.items():
            setattr(self, key, value)


    def find_free_spot(self):
        for y in range(8):
            for x in range(1):
                grid_positions = [(int(e.x*self.texture_scale[0]), int(e.y*self.texture_scale[1])) for e in self.children]
                print(grid_positions)

                if not (x,-y) in grid_positions:
                    print('found free spot:', x, y)
                    return x, y


    def append(self, item):
        print('add item:', item)

        if len(self.children) >= 5*1:
            print('inventory full')
            error_message = Text('<red>Inventory is full!', origin=(0,-1.5), x=-.5, scale=2)
            destroy(error_message, delay=1)
            return

        item.tooltip = Tooltip(item.name)
        item.tooltip.background.color = color.color(0,0,0,.8)

        def drag():
            item.org_pos = (item.x, item.y)
            item.z -= .01   # ensure the dragged item overlaps the rest

        def drop():
            ix, iy = self.find_free_spot()
            item.x = ix * 1 / self.texture_scale[0],
            item.y = -iy * 1 / self.texture_scale[1],

            if 1 >= item.x >= -1 and 1 > item.y > -1:
                item.x = int((item.x + (item.scale_x/2)) * 5) / 5
                item.y = int((item.y - (item.scale_y/2)) * 1) / 1
                item.z += .6

            # if outside, return to original position
            # if item.x < 0 or item.x >= 1 or item.y > 0 or item.y <= -1:
            #     item.position = (item.org_pos)
            #     return

            # if the spot is taken, swap positions
            for c in self.children:
                if c == item:
                    continue

                if c.x == item.x and c.y == item.y:
                    print('swap positions')
                    c.position = item.org_pos


        item.drag = drag
        item.drop = drop