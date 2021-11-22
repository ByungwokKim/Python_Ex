import turtle as t
import random
import time
import math

score =0
s=t.Turtle()  # 점수 그려줄 s 터틀
s.up()
#s.goto(200,220)
s.color("white")
s.home
s.ht()

playing=False   #ta 적 거북이 1,2,3
ta = t.Turtle()
ta.shape("turtle")
ta.color("red")
ta.speed(15)
ta.up()
ta.goto(0,200)

ta1 = t.Turtle()
ta1.shape("turtle")
ta1.color("pink")
ta1.speed(15)
ta1.up()
ta1.goto(-200,0)

ta2 = t.Turtle()
ta2.shape("turtle")
ta2.color("orange")
ta2.speed(15)
ta2.up()
ta2.goto(-150,150)


pen = t.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
#pen.setx(-75)
#pen.goto(-140,220)
#pen.write(str(num), font=("Arial", 16))

# 터틀 먹이 코인
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
            s.clear()          #메세지 지워
            score = 0
            play()

def play():
      global score
      global playing
      t.forward(10)

      #적이 따라 올 확률
      if random.randint(1,3)==3:    
            ang = ta.towards(t.pos())       
            ta.seth(ang)
            
      #speed=score+5  
      t.forward(10)
      if random.randint(1,2)==2:
            ang1 = ta1.towards(t.pos())
            ta1.seth(ang1)

      t.forward(10)
      if random.randint(1,2)==2:
            ang2 = ta2.towards(t.pos())
            ta2.seth(ang2)
            
      # 맵 밖으로 못 나가게
      if t.xcor() > 220 or t.xcor() < -220 or t.ycor() > 220 or t.ycor() < -220:  
            t.right(180)
            t.forward(10)
      speed = 15
      ta.forward(speed+1) # 적 속도 
      ta1.forward(speed)
      ta2.forward(speed-2)
      t.forward(speed-1)

      if t.distance(ta)<20:         #1 적과 만나면 -죽음-
            t.clear()
            message("Game Over","T_T",f"score : {score}")
            score =0
            playing=False           #게임이 종료될 수 있도록 플레이어 폴스       
            ta.goto(180,-230)
            t.home()
            
      if t.distance(ta1)<20:         #2 적과 만나면 -죽음-
            t.clear()
            message("Game Over","T_T",f"score : {score}")
            score =0
            playing=False           #게임이 종료될 수 있도록 플레이어 폴스
            ta1.goto(-200,200)
            t.home()

      if t.distance(ta2)<20:         #3 적과 만나면 -죽음-
            t.clear()
            message("Game Over","T_T",f"score : {score}")
            score =0
            playing=False           #게임이 종료될 수 있도록 플레이어 폴스    
            ta2.goto(-50,150)
            t.home()
            
      if score >= 5:
            s.clear()
            message("Success","Game!!","5 점으로 성공!")
            playing = False()
            t.home()
            
      if playing:       #게임이 계속 이어가게 함
            t.ontimer(play,100)

      if t.distance(tm)<20:         #나와 먹이를 먹은 거리가 12 이내면 스코어 표시
            s.clear()         # 먹이를 먹는 순간 화면 클리어
            score +=1     # 먹었으니 스코어 =1
            s.goto(0,220)
            s.write(f"Score : {score}",False,"center",("",15))    #써 내 점수 몇인지
            star_x=random.randint(-210,210) #랜덤으로 보낼 범위 
            star_y=random.randint(-210,210)
            tm.goto(star_x,star_y) #먹이를 임의의 장소로 보냄
      
            

def message(m1,m2,m3):
      s.clear()
      s.goto(0,-50)
      s.write(m1,False,"center",(' ',15))
      s.goto(0,-75)
      s.write(m2,False,"center",(' ',15))
      s.goto(0,-100)
      s.write(m3,False,"center",(" ",15))
      #t.home()
      
message("방향키 이동 코인은 노란색!","[스페이스바 눌러 시작 5점 내기!]",f"Score : {score}")  # 시작 메세지
#환경 설정
t.title("도망치기 게임")      # 라벨 명
t.setup(500,500)              # 겜 사이즈 
t.bgcolor("black")
t.shape('turtle')             # 나는 거북이
t.shapesize(1.5)
t.speed(15)                    # 내 속도는 9부터 시작
t.up()
t.color("white")

t.onkeypress(turn_right,"Right") #키 입력 받기
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space") #스페이스바는 소문자
t.listen()

