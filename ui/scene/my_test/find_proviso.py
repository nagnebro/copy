
from ursina import *

from ui.scene.my_test.MyButton import MyButton

'''


class parent:

    def __init__(self,a):
        self.a = a



    def parentmethod(self):
        print(self.a)

class child(parent):

    def __init__(self,a,b):
        super().__init__(a)
        self.b = b


p = parent(30)
c = child(20,50)

p2 = parent(a=100) # 다음과 같이 인스턴스 변수를 매개변수로 주면서 초기화를 할 수도 있다.
print(p.a)
print(p2.a)
print(c.a,"  ",c.b)

p.parentmethod()
c.parentmethod()



app = Ursina()


# 여기서 input함수는 아마도 keys? mouse클래스에서 상속받아서 사용하는 것일거다.
def input(key):
    print(key)


app.run()


Entity의 다양한 인스턴스 변수들.

Entity() -> 매개변수 없이 생성가능하다
default 매개변수를 가지고 있고 나머지는 kwargs이다
kwargs는 keyword argument의 약자로 딕셔너리의 형태의 값을 받아온다
args는 argument로 여러개의 인자를(튜플) 받아온다.
Entity의 사전적 정의는 실재로 즉 실재하는 객체 따위를 만드는 클래스라고 이해하면 된다.
Entity클래스와 그를 상속하는 다양한 클래스를 통해 우리는 버튼과 사물과 객체 등
다양한 것들을 생성할 수 있게 된다. 이제부터는 그냥 그 클래스의 인스턴스 변수가 뭐가 있고
인스턴스 메서드가 뭐가 있는지를 이용해서 만들어나갈 뿐이다.
그리고 기본적으로 제공돼있는 sample을 참고해 내가 원하는 형태로 module을 바꿔서
사용할 줄 알아야 한다.

우선 지금 내가 해야할 일은 다음과 같다.

단서 수집 씬의 시작과 끝, 즉 모듈간의 이동은 배제하고 단순히 그 화면에서의 기능동작이나 ui만 설계한다
이 때 고려할 사항은 여러 장면에 응용될 프로그램일 것이기 때문에 그 점을 감안해서 코드를 작성해야 할것이다.

우선 리소스 같은 부분은 모두 제외해놓고 기능과 UI를 만들어야 할 것은
1. 흩뿌려진 단서들을 클릭 했을 때에 가운데에 단서 정보에 해당하는 text, img가 한번에 출력된다
                이미지
            내려치기에 좋은 망치이다.
            
이 때 단서는 여러가지가 있으므로 배열의 형태를 이용해 처리하는 것도 괜찮을 듯 하다. 
on_click과 같은 메서드는 오직 action 형태의 함수만 제공하기 때문에 내가 
button클래스를 상속받아 재정의해서(오버라이딩) 사용해야 한다.
우선 처음부터 만들어보자.
'''

app = Ursina() # ??

window.borderless = False # 창의 타이틀바 유무를 결정

background = Entity()

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

m = Button()



background = Entity(parent = camera.ui, model = 'quad', texture = 'restroom', colr = color.white ,scale=(camera.aspect_ratio,1))

proviso1 = MyButton(parent = camera.ui , model = 'quad',texture = 'glass.png', color = color.white , scale = .2 ,x=.3, y=.3, text='ㅁㄴㄹㅁㄴㄹ')
proviso2 = MyButton(parent = camera.ui , model = 'quad',texture = 'glass.png', color = color.white , scale = .2 ,x=.2, y=.3,text='text2.')
proviso3 = MyButton(parent = camera.ui , model = 'quad',texture = 'glass.png', color = color.white , scale = .2 ,x=.0, y=.3,text='text3.')
proviso4 = MyButton(parent = camera.ui , model = 'quad',texture = 'glass.png', color = color.white , scale = .2 ,x=-.1, y=.3,text='text4.')
proviso5 = MyButton(parent = camera.ui , model = 'quad',texture = 'glass.png', color = color.white , scale = .2 ,x=-.2, y=-.2,text='text5.')


test1= MyButton(parent = camera.ui , model = 'quad',texture = 'paper.png', color = color.white , scale = .2 ,x=-.4, y=-.4 , text= 'text2')
test2 = MyButton(parent = camera.ui , model = 'quad',texture = 'potion.png', color = color.white , scale = .2 ,x=-.5, y=-.5, text = 'text2')
# 여기서 내가 만든 MyButton 클래스에서 매개변수로 **kwargs로 매개변수들을 받는다. 애초에 Entity랑 MyButton에서부터 가변 키워드 인자를 받아오고 있기 때문에
# 저렇게 넘겨주고 다시 mybutton 에서 키워드 인자를 넘겨주면 초기화가 된다.



# list = [proviso1,proviso2,proviso3,proviso4,proviso5]


# on_click을 사용하기 위해서는 button 클래스여야한다. 따라서 클릭해야 할 객체들은 모두 button으로 만들자.
# 이 때 hover시 버튼 객체의 특성상 칼라가 달라지는 문제가 발생하므로 이건 나중에 button 클래스에 속성 찾아봐야할듯.
# on_click 메서드를 단서별로 다 만들기는 너무 비효율적이니까 하나의 on_click 함수로 만들어놓고 함수 내부에서 어떤 버튼 객체인지 검사하게끔 만들어야 한다.
# 이벤트 리스너를 결국에 한개씩 다달아줘야할 거 같긴한데 일단 생각나는대로 되는 방법으로 구현하고 나중에 바꿔보자.

def input(key):
    if key == "left_mouse_down":
        print('ho')


test = Draggable(arent = camera.ui , model = 'quad',texture = 'glass.png', color = color.white , scale = .2 ,x=-.2, y=-.2,text='text5.')



#on_click()
app.run() # 앱,창이 켜진다.


