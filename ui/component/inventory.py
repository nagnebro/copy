from ursina import *


class Inventory(Entity):
    def __init__(self, player_data, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='white_cube',
            texture_scale=(4, 6),
            scale=(.4, .6),
            origin=(-.5, .5),
            position=(-.8, .4),
            color=color.color(0, 0, .1, .9),
        )

        for item in player_data.inventory:
            self.append(item)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def find_free_spot(self):
        for y in range(8):
            for x in range(4):
                grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1])) for e in
                                  self.children]
                print(grid_positions)

                if not (x, -y) in grid_positions:
                    print('found free spot:', x, y)
                    return x, y

    def append(self, item, x=0, y=0):
        print('add item:', item)

        if len(self.children) >= 4 * 6:
            print('inventory full')
            error_message = Text('<red>Inventory is full!', origin=(0, -1.5), x=-.5, scale=2)
            destroy(error_message, delay=1)
            return

        x, y = self.find_free_spot()

        icon = Draggable(
            parent=self,
            model='quad',
            texture=item,
            color=color.white,
            scale_x=1 / self.texture_scale[0],
            scale_y=1 / self.texture_scale[1],
            origin=(-.5, .5),
            x=x * 1 / self.texture_scale[0],
            y=-y * 1 / self.texture_scale[1],
            z=-.5,
        )

        icon.tooltip = Tooltip(item)
        icon.tooltip.background.color = color.color(0, 0, 0, .8)

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01  # ensure the dragged item overlaps the rest

        def drop():
            icon.x = int((icon.x + (icon.scale_x / 2)) * 4) / 4
            icon.y = int((icon.y - (icon.scale_y / 2)) * 6) / 6
            icon.z += .01

            # if outside, return to original position
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                self.parent.append(item)
                return

            # if the spot is taken, swap positions
            for c in self.children:
                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    print('swap positions')
                    c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop


if __name__ == '__main__':
    app = Ursina()
    inventory = Inventory()
    window.borderless = False


    def add_item():
        inventory.append(random.choice(('bag', 'bow_arrow', 'gem', 'orb', 'sword')))


    add_item()
    add_item()
    add_item_button = Button(
        scale=(.1, .1),
        x=-.5,
        color=color.lime.tint(-.25),
        text='+',
        tooltip=Tooltip('Add random item'),
        on_click=add_item
    )
    bg = Entity(parent=camera.ui, model='quad', texture='shore', scale_x=camera.aspect_ratio, z=1)
    Cursor(texture='cursor', scale=.1)
    mouse.visible = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False
    app.run()
