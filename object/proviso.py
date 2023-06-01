from ursina import *
from prec.my_test.mybutton import MyButton
#


class Proviso(Entity):





    def __init__(self, player_data, **kwargs):
        super().__init__(parent=camera.ui, **kwargs)



        MyButton.player_data = player_data # Mybutton의 클래스 변수로 mapchapter에서 넘겨받은 player의 data를 넘겨준다.


        # 여기서 단서를 만들기 위해서 단서의 클래스 타입을 무멋으로 지정할 것이느냐도 중요한데 우선은
        # button 타입으로 하겠다. 왜냐하면 다른 객체에는 on_click이나 뭐 click이벤트를 감지할만한
        # 함수를 제공하고 있지 않고 있기 때문이다 -> 내가 잘못알고 있을수도, 추후 수정하자.

        # ?? Entity객체들의 화면위에 겹쳐지는 우선순위를 결정하는 방법
        # -> 뒤에 생성된놈들이 계속해서 위에 겹쳐지는 형태이다.

        # ?? mdoel 의 종류같은 거는 어디서 확인하는지

        # x,y좌표는 2차원 좌표평면을 기준으로한다 따라서 x,y가 양수면 1사분면, 즉 우측위쪽으로 이동한다.
        # parent 속성은 카메라 시점을 선택한다. camera.ui는 3d? 2.5d로 보여주고 default값은 scene이다 아마 2차원 평면인듯하다.
        # camera.aspect_ratio 는 camera, 즉 창에 꽉차게끔 객체를 집어넣는다.
        # texture는 객체에 대신 삽입할 이미지 따위를 설정할 수 있다.

        # m = Button()

        # if player


        # 1. 단서를 클릭했을 떄 inventory에 추가됨은 물론이고 현장에서 증거가 습득되면서 없어지게 만들기
        # -> 이렇게 만들면 어차피 중복 클릭했을 때 inventory에 증거있는지 검사하고 잇으면 안넣게끔 구ㅇ현하는 예외처리를 안해도됨.
        # 2. 단서를 수집하러 다시 방에 들어왔을 떄 내가 가지고 있는 단서는 단서 수집 장소에 없어야한다

        def compare_inventory(proviso_list): # 현재 유저의 인벤토리와 증거끼리 비교해서 인벤토리에 있는 증거라면 단서 수집 화면에서 disable처리함.
            for i in proviso_list:
                for j in player_data.inventory:
                    if (i.id == j.id):
                        i.disable()




        # proviso = 1의 속성은 각 용의자에 해당하는 단서의 아이디값으로 조합시에 이용하면 됨.
        if player_data.chapter == 1: # id값 말고 texture로 비교해도됨.
            background = Entity(parent=self, model='quad', texture='restroom', colr=color.white,
                                scale=(camera.aspect_ratio, 1))
            proviso1_1 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2,
                                  x=.3,
                                  y=.3, text='abcdefg', proviso=1 , id="1-1")
            proviso1_2 = MyButton(parent=self, model='quad', texture='blueprint', color=color.white, scale=.2,
                                  x=.2,
                                  y=.3, text='text2.', proviso=1, id= "1-2")
            proviso1_3 = MyButton(parent=self, model='quad', texture='glass', color=color.white, scale=.2,
                                  x=.0,
                                  y=.3, text='text3.', proviso=1, id="1-3")
            proviso1_4 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2,
                                  x=-.1,
                                  y=.3, text='text4.', proviso=1, id="1-4")
            proviso1_5 = MyButton(parent= self, model='quad', texture='glass.png', color=color.white, scale=.2,
                                  x=-.2,
                                  y=-.2, text='text5.', proviso=1, id="1-5")

            proviso_list1 = [proviso1_1,proviso1_2,proviso1_3,proviso1_4,proviso1_5]
            compare_inventory(proviso_list1)



            #
            # for i in player_data.inventory:
            #     print("player 인벤토리", player_data.inventory)
            #     print(i)
            #     if i.text :
            #         proviso_list1[proviso_list1.index(i)].disable()
            #         print(i.text)





        elif player_data.chapter == 2:
            print("chater2 실행")
            background = Entity(parent=self, model='quad', texture='inha_ware6_hall', colr=color.white,
                                scale=(camera.aspect_ratio, 1))

            proviso2_1 = MyButton(parent=self, model='quad', texture='paper.png', color=color.white, scale=.2, x=.3,
                                y=.3, text='ㅁㄴㄹㅁㄴㄹ', proviso = 2, id="2-1")
            proviso2_2 = MyButton(parent=self, model='quad', texture='poison', color=color.white, scale=.2, x=.2,
                                y=.3, text='text2.', proviso = 2, id="2-2")
            proviso2_3 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.0,
                                y=.3, text='text3.',proviso = 2, id="2-3")
            proviso2_4 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.1,
                                y=.3, text='text4.', proviso = 2, id="2-4")
            proviso2_5 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.2,
                                y=-.2, text='text5.', proviso = 2, id="2-5")

            proviso_list2 = [proviso2_1,proviso2_2,proviso2_3,proviso2_4,proviso2_5]
            compare_inventory(proviso_list2)

        # elif player_data.chapter == 3:
        #     background = Entity(parent=self, model='quad', texture='inha_ware6_hall', colr=color.white,
        #                         scale=(camera.aspect_ratio, 1))
        #
        #     proviso1 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.3,
        #                         y=.3, text='ㅁㄴㄹㅁㄴㄹ', proviso = 3)
        #     proviso2 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.2,
        #                         y=.3, text='text2.', proviso = 3)
        #     proviso3 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.0,
        #                         y=.3, text='text3.', proviso = 3)
        #     proviso4 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.1,
        #                         y=.3, text='text4.', proviso = 3)
        #     proviso5 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.2,
        #                         y=-.2, text='text5.', proviso = 3)
        #
        #
        #
        # elif player_data.chapter == 4:
        #     background = Entity(parent=self, model='quad', texture='inha_ware6_hall', colr=color.white,
        #                         scale=(camera.aspect_ratio, 1))
        #
        #     proviso1 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.3,
        #                         y=.3, text='ㅁㄴㄹㅁㄴㄹ',proviso = 4 )
        #     proviso2 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.2,
        #                         y=.3, text='text2.', proviso = 4)
        #     proviso3 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.0,
        #                         y=.3, text='text3.', proviso = 4)
        #     proviso4 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.1,
        #                         y=.3, text='text4.', proviso = 4)
        #     proviso5 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.2,
        #                         y=-.2, text='text5.', proviso = 4)
        #
        #
        # elif player_data.chapter == 5:
        #     background = Entity(parent=self, model='quad', texture='inha_ware6_hall', colr=color.white,
        #                         scale=(camera.aspect_ratio, 1))
        #
        #     proviso1 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.3,
        #                         y=.3, text='ㅁㄴㄹㅁㄴㄹ', proviso = 5)
        #     proviso2 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.2,
        #                         y=.3, text='text2.', proviso = 5)
        #     proviso3 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=.0,
        #                         y=.3, text='text3.', proviso = 5)
        #     proviso4 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.1,
        #                         y=.3, text='text4.', proviso = 5)
        #     proviso5 = MyButton(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.2,
        #                         y=-.2, text='text5.', proviso = 5)


        # 여기서 내가 만든 MyButton 클래스에서 매개변수로 **kwargs로 매개변수들을 받는다. 애초에 Entity랑 MyButton에서부터 가변 키워드 인자를 받아오고 있기 때문에
        # 저렇게 넘겨주고 다시 mybutton 에서 키워드 인자를 넘겨주면 초기화가 된다.

        # list = [proviso1,proviso2,proviso3,proviso4,proviso5]
        #
        # test = Draggable(parent=self, model='quad', texture='glass.png', color=color.white, scale=.2, x=-.2, y=-.2,
        #                  text='text5.')

        # on_click을 사용하기 위해서는 button 클래스여야한다. 따라서 클릭해야 할 객체들은 모두 button으로 만들자.
        # 이 때 hover시 버튼 객체의 특성상 칼라가 달라지는 문제가 발생하므로 이건 나중에 button 클래스에 속성 찾아봐야할듯.
        # on_click 메서드를 단서별로 다 만들기는 너무 비효율적이니까 하나의 on_click 함수로 만들어놓고 함수 내부에서 어떤 버튼 객체인지 검사하게끔 만들어야 한다.
        # 이벤트 리스너를 결국에 한개씩 다달아줘야할 거 같긴한데 일단 생각나는대로 되는 방법으로 구현하고 나중에 바꿔보자.







    def input(self, key):
        if key == 'x':
            print(key)
            self.disable()