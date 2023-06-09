from ursina import *
from prec.my_test.proviso import Proviso


class Find_Proviso(Entity):




    def __init__(self, player_data, item_data, number, **kwargs):

        super().__init__(parent=camera.ui, **kwargs)
        self.item_data = item_data



        # self.item2_5 = item_data.item["책"]

        Proviso.player_data = player_data  # Mybutton의 클래스 변수로 mapchapter에서 넘겨받은 player의 data를 넘겨준다.

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

        def compare_inventory(proviso_list):  # 현재 유저의 인벤토리와 증거끼리 비교해서 인벤토리에 있는 증거라면 단서 수집 화면에서 disable처리함.
            for i in proviso_list:
                for j in player_data.inventory:
                    if (i.name == j.name):
                        i.disable()

        # proviso = 1의 속성은 각 용의자에 해당하는 단서의 아이디값으로 조합시에 이용하면 됨.
        if number == 1:
            background = Entity(parent=self, model='quad', texture='restroom', color=color.white,
                                scale=(camera.aspect_ratio, 1))

            # 활용 부탁드립니다
            self.item1_1 = item_data.item["떨어진 영수증"]
            self.item1_2 = item_data.item["내려치기 딱 좋은 망치"]
            self.item1_3 = item_data.item["마스터 키"]
            self.item1_4 = item_data.item["휴대폰"]

            proviso1_1 = Proviso(parent=self, model='quad', texture=self.item1_1.texture, color=color.white, scale=0.05,
                                 position= (-.6,-.3,0), name=self.item1_1.name, proviso=self.item1_1.chapter_no,
                                 desc=self.item1_1.desc)

            proviso1_2 = Proviso(parent=self, model='quad', texture=self.item1_2.texture, color=color.white, scale=.1,
                                 position = (-.4, .1, 0), name=self.item1_2.name, proviso=self.item1_2.chapter_no, desc=self.item1_2.desc)

            proviso1_3 = Proviso(parent=self, model='quad', texture=self.item1_3.texture, color=color.white, scale=.1,
                                 position = (-.2, -.4, 0), name=self.item1_3.name, proviso=self.item1_3.chapter_no, desc=self.item1_3.desc)

            proviso1_4 = Proviso(parent=self, model='quad', texture=self.item1_4.texture, color=color.white, scale=.1,
                                 position=(0, -.2, 0), name=self.item1_4.name, proviso=self.item1_4.chapter_no, desc=self.item1_4.desc)

            proviso_list1 = [proviso1_1, proviso1_2, proviso1_3, proviso1_4]
            compare_inventory(proviso_list1)

            #
            # for i in player_data.inventory:
            #     print("player 인벤토리", player_data.inventory)
            #     print(i)
            #     if i.text :
            #         proviso_list1[proviso_list1.index(i)].disable()
            #         print(i.text)





        elif number == 2:
            print("chater2 실행")

            self.item2_1 = item_data.item["책"]
            self.item2_2 = item_data.item["벽돌"]
            self.item2_3 = item_data.item["롤 경기장 티켓"]
            self.item2_4 = item_data.item["ph 종이"]
            self.item2_5 = item_data.item["배터리"]


            background = Entity(parent=self, model='quad', texture='cabinet_inner', colr=color.white,
                                scale=(camera.aspect_ratio, 1),)

            proviso2_1 = Proviso(parent=self, model='quad', texture=self.item2_1.texture, color=color.white, scale=.2,
                                 position=(-0.1, -0.2, 0), name=self.item2_1.name, proviso=self.item2_1.chapter_no, desc=self.item2_1.desc)

            proviso2_2 = Proviso(parent=self, model='quad', texture=self.item2_2.texture, color=color.white, scale=.4,
                                 position = (0.15, -0.25, -1), name=self.item2_2.name, proviso=self.item2_2.chapter_no, desc=self.item2_2.desc)

            proviso2_3 = Proviso(parent=self, model='quad', texture=self.item2_3.texture, color=color.white, scale=.1,
                                 position = (0.1, -0.1, 0), name=self.item2_3.name, proviso=self.item2_3.chapter_no, desc=self.item2_3.desc)

            proviso2_4 = Proviso(parent=self, model='quad', texture=self.item2_4.texture, color=color.white, scale=.1,
                                 position = (0, -0.3, 0), name=self.item2_4.name, proviso=self.item2_4.chapter_no, desc=self.item2_4.desc)

            proviso2_5 = Proviso(parent=self, model='quad', texture=self.item2_5.texture, color=color.white, scale=.3,
                                 position = (-0.2, -0.3, 0), name=self.item2_5.name, proviso=self.item2_5.chapter_no, desc=self.item2_5.desc)

            proviso_list2 = [proviso2_1, proviso2_2, proviso2_3, proviso2_4, proviso2_5]
            compare_inventory(proviso_list2)

        elif number == 3:

            self.item3_1 = item_data.item["커터칼"]
            self.item3_2 = item_data.item["쪽지"]
            self.item3_3 = item_data.item["밧줄"]



            background = Entity(parent=self, model='quad', texture='big_cabinet_open1', colr=color.white,
                                scale=(camera.aspect_ratio, 1))

            proviso3_1 = Proviso(parent=self, model='quad', texture=self.item3_1.texture, color=color.white, scale=.2,
                                 x=-.2,
                                 y=-.2, name=self.item3_1.name, proviso=self.item3_1.chapter_no, desc=self.item3_1.desc)

            proviso3_2 = Proviso(parent=self, model='quad', texture=self.item3_2.texture, color=color.white, scale=.2,
                                 x=-.2,
                                 y=-.2, name=self.item3_2.name, proviso=self.item3_2.chapter_no, desc=self.item3_2.desc)

            proviso3_3 = Proviso(parent=self, model='quad', texture=self.item3_3.texture, color=color.white, scale=.2,
                                 x=-.2,
                                 y=-.2, name=self.item3_3.name, proviso=self.item3_3.chapter_no, desc=self.item3_3.desc)

            proviso_list2 = [proviso3_1, proviso3_2, proviso3_3]
            compare_inventory(proviso_list2)



        elif number == 4:


            self.item4_1 = item_data.item["비상용 망치"]
            self.item4_2 = item_data.item["조교 리스트"]
            self.item4_3 = item_data.item["블랙박스"]


            background = Entity(parent=self, model='quad', texture='under_car', colr=color.white,
                                scale=(camera.aspect_ratio, 1))

            proviso4_1 = Proviso(parent=self, model='quad', texture=self.item4_1.texture, color=color.white, scale=.2,
                                 position=(-.4, .1, 0), name=self.item4_1.name, proviso=self.item4_1.chapter_no, desc=self.item4_1.desc)

            proviso4_2 = Proviso(parent=self, model='quad', texture=self.item4_2.texture, color=color.white, scale=.2,
                                 position=(.0, .1, 0), name=self.item4_2.name, proviso=self.item4_2.chapter_no, desc=self.item4_2.desc)

            proviso4_3 = Proviso(parent=self, model='quad', texture=self.item4_3.texture, color=color.white, scale=.2,
                                 position=(.4, .1, 0), name=self.item4_3.name, proviso=self.item4_3.chapter_no, desc=self.item4_3.desc)

            proviso_list2 = [proviso4_1, proviso4_2, proviso4_3]
            compare_inventory(proviso_list2)


        elif number == 5:

            self.item5_1 = item_data.item["커플사진"]
            self.item5_2 = item_data.item["일기"]
            self.item5_3 = item_data.item["아이폰"]
            self.item5_4 = item_data.item["숫돌"]



            background = Entity(parent=self, model='quad', texture='gf1', colr=color.white,
                                scale=(camera.aspect_ratio, 1))

            proviso5_1 = Proviso(parent=self, model='quad', texture=self.item5_1.texture, color=color.white, scale=.2,
                                 position=(-.4, .4, 0), name=self.item5_1.name, proviso=self.item5_1.chapter_no, desc=self.item5_1.desc)

            proviso5_2 = Proviso(parent=self, model='quad', texture=self.item5_2.texture, color=color.white, scale=.1,
                                 position=(-.2, -.4, 0), name=self.item5_2.name, proviso=self.item5_2.chapter_no, desc=self.item5_2.desc)

            proviso5_3 = Proviso(parent=self, model='quad', texture=self.item5_3.texture, color=color.white, scale=.2,
                                 position=(.5, -.1, 0), name=self.item5_3.name, proviso=self.item5_3.chapter_no, desc=self.item5_3.desc)

            proviso5_4 = Proviso(parent=self, model='quad', texture=self.item5_4.texture, color=color.white, scale=.2,
                                 position=(0, -.3, 0), name=self.item5_4.name, proviso=self.item5_4.chapter_no, desc=self.item5_4.desc)

            proviso_list2 = [proviso5_1, proviso5_2, proviso5_3, proviso5_4]
            compare_inventory(proviso_list2)

    # 여기서 내가 만든 Proviso 클래스에서 매개변수로 **kwargs로 매개변수들을 받는다. 애초에 Entity랑 MyButton에서부터 가변 키워드 인자를 받아오고 있기 때문에
    # 저렇게 넘겨주고 다시 Proviso 에서 키워드 인자를 넘겨주면 초기화가 된다.

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
