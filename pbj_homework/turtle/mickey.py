import turtle as t
# 시작점으로 이동
t.speed(10)

# 펜 설정
t.width(5)


class PenUpAndDown:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        t.penup()
        t.setposition(self.x, self.y)
        t.pendown()
        
    def circle(radius, move):
        t.circle(radius, move)

    def left(angel):
        t.left(angel)
        
# 타원 생성기
class Ellipse:
    def __init__(self, size):
        self.size = size

    def sharp(self):
        t.circle(self.size, 40)
        t.circle(10 , 100)
        print('1꼭짓점' ,t.pos())
        t.circle(self.size, 40)
        t.circle(self.size, 40)
        t.circle(10 , 100)
        print('2꼭짓점' ,t.pos())
        t.circle(self.size, 40)
    
    def round(self, round_index):
        self.round_index = round_index
        for i in range(1,3):      
            t.circle(self.size,90)    
            t.circle(self.size/round_index,90)  
            print('{0}꼭짓점'.format(i) ,t.pos())
        

class Color:
    def __init__(self,hex_code):
        self.hex_code = hex_code
    
    def all(self):
        t.pencolor('#{0}'.format(self.hex_code))
        t.fillcolor('#{0}'.format(self.hex_code))
        t.begin_fill()

    def fill(self):
        t.fillcolor('#{0}'.format(self.hex_code))
        t.begin_fill()
    
    def pen(self):
        t.pencolor('#{0}'.format(self.hex_code))

# 얼굴 그리기
PenUpAndDown(0,-200)
Color('000000').fill()
t.circle(200,360)
t.end_fill()


# 오른쪽 귀 그리기
PenUpAndDown(240,50)  #오른쪽 귀로 이동
Color('000000').fill()
t.circle(110,360)
t.end_fill()


# 왼쪽 귀 그리기
PenUpAndDown(-240,50) # 왼쪽 귀로 이동
Color('000000').fill()
t.circle(110,360)
t.end_fill()


# 피부 그리기
Color('ffdead').all()
PenUpAndDown(-40,-50)
t.left(40)
Ellipse(150).round(3)
t.end_fill()

Color('ffdead').fill()
t.left(5)
PenUpAndDown(80,-50)
Ellipse(150).round(3)
t.end_fill()

Color('ffdead').fill()
t.left(90)
PenUpAndDown(130,0)
Ellipse(180).round(2)
t.end_fill()
t.right(90)


# 왼쪽 눈 그리기
Color('000000').pen()
t.right(45)
PenUpAndDown(-70,50)
t.right(90)
Color('ffffff').fill()
Ellipse(100).sharp()
t.end_fill()

# 왼쪽 눈알 그리기
Color('000000').fill()
Ellipse(50).sharp()
t.end_fill()


# 오른쪽 눈 그리기
PenUpAndDown(20,50)
Color('ffffff').fill()
Ellipse(100).sharp()
t.end_fill()

# 오른쪽 눈알 그리기
Color('000000').fill()
Ellipse(50).sharp()
t.end_fill()

# 애굣살? 그리기
PenUpAndDown(60,-20)
t.left(240)
t.circle(120,60)

# 코 그리기
# t.speed(8)
Color('000000').all()
PenUpAndDown(40, -30)

t.right(75)
Ellipse(60).round(4)
t.end_fill()

t.exitonclick()