import turtle as t
import random

score = 0
playing=False   #ta 적 거북이 1,2,3
ta = t.Turtle()
ta.shape("turtle")
ta.color("red")
ta.speed(9)
ta.up()
ta.goto(0,200)

ta1 = t.Turtle()
ta1.shape("turtle")
ta1.color("pink")
ta1.speed(9)
ta1.up()
ta1.goto(-200,0)

ta2 = t.Turtle()
ta2.shape("turtle")
ta2.color("orange")
ta2.speed(9)
ta2.up()
ta2.goto(-150,150)


# 스코어 먹이
tm = t.Turtle()
tm.shape("circle")
tm.shapesize(0.6)
tm.color("yellow")
tm.speed(0) 
tm.up()
tm.goto(0,-200)

def turn_right():
      t.seth(0)
def turn_left():
      t.seth(180)
def turn_up():
      t.seth(90)
def turn_down():
      t.seth(270)

def start():
      global playing    #전체 사용을 위해 글로벌
      if playing ==False:  #게임 대기중이면
            playing=True
            t.clear()          #메세지 지워
            play()      

def play():
      global score
      global playing
      global ta1
      
      t.forward(10)
      if random.randint(1,3)==3:    #적이 따라 올 확률
            ang = ta.towards(t.pos())       
            ta.seth(ang)
      speed=score+5   # 점수가 높아질수록 스피드 올려서 난이도 업

      if random.randint(1,2)==2:
            ang1 = ta1.towards(t.pos())
            ta1.seth(ang1)

      if random.randint(1,2)==2:
            ang2 = ta2.towards(t.pos())
            ta2.seth(ang2)
            
      if speed >15: 
            speed=15  #적과 나의 속도는 15가 최대
      ta.forward(speed-2) # 적 속도 낮추기 
      ta1.forward(speed)
      ta2.forward(speed-1)
      t.forward(speed) 

      if t.distance(ta)<12:         #적과 만나면 -죽음-
            text="Score : "+str(score)
            message("게임 오버",text)
            playing=False           #게임이 종료될 수 있도록 플레이어 폴스
            score=0

      if t.distance(tm)<12:         #나와 먹이를 먹은 거리가 12 이내면 스코어 표시
            score +=1
            t.write(score)
            star_x=random.randint(-230,230) #랜덤으로 보낼 범위 
            star_y=random.randint(-230,230)
            tm.goto(star_x,star_y) #먹이를 임의의 장소로 보냄
            
      if playing:       #게임이 계속 이어가게 함
            t.ontimer(play,100)

def message(m1,m2):
      t.clear()
      t.goto(0,-150)
      t.write(m1,False,"center",(' ',15))
      t.goto(0,-100)
      t.write(m2,False,"center",(' ',15))
      t.home()

t.title("도망치기 게임")      # 라벨 명

t.setup(500,500)              # 겜 사이즈 
t.bgcolor("black")
t.shape('turtle')             # 나는 거북이
t.shapesize(1.5)
t.speed(9)                    # 내 속도는 9부터 시작
t.up()
t.color("white")

t.onkeypress(turn_right,"Right") #키 입력 받기
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space") #스페이스바는 소문자
t.listen()

message("방향키 이동 먹이는 노란색!","[스페이스바 누르면 시작]")  # 시작 메세지


