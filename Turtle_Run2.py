import turtle as t
import random

#변수 선언
t_speed = 5
score = 0
game_over = False

# 점수 표시
t.goto(0,220)
t.write(f"score : {score}", False ,"center",(" ",20))

#플레이어
player = t.Turtle()
player.shape("turtle")
player.shapesize(2)
player.up()
player.color("black")

# 코인
coin = t.Turtle()
coin.shape("circle")
coin.color("yellow")
coin.speed(0)
coin.up()
coin.goto(0,-150)

#키 이벤트 설정
def turn_right():
      player.seth(0)
def turn_left():
      player.seth(180)
def turn_up():
      player.seth(90)
def turn_down():
      player.seth(270)

# 키 이벤트
t.onkeypress(turn_right,"Right") #키 입력 받기
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
#t.onkeypress(start,"space") #스페이스바는 소문자
t.listen()

#적 3마리 추가
playing=False   # 겜 시작 전 애들 위치
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

# 코인 위치 랜덤 좌표 설정





# 게임 시작, 게임 설정
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
      global ta2
      global ta3
      
      t.forward(10)
      if random.randint(1,3)==3:    #적이 따라 올 확률
            ang = ta.towards(player.pos())       
            ta.seth(ang)
      speed=score+3   # 점수가 높아질수록 스피드 올려서 난이도 업
      if random.randint(1,2)==2:
            ang1 = ta1.towards(player.pos())
            ta1.seth(ang1)
            
      if random.randint(1,2)==2:
            ang2 = ta2.towards(player.pos())
            ta2.seth(ang2)

      if player.xcor() > 230 or player.xcor() < -230 or player.ycor() > 230 or player.ycor() < -230:
            player.right(180)

      if speed >15: 
            speed=15  #적과 나의 속도는 15가 최대
            ta.forward(speed-1) # 적 속도 낮추기 
            ta1.forward(speed)
            ta2.forward(speed-1)
            player.forward(speed)
            
      if t.distance(ta)<20:         #적과 만나면 -죽음-
            text="Score : "+str(score)
            message("게임 오버",text)
            playing=False           #게임이 종료될 수 있도록 플레이어 폴스
            score=0
            
      if player.distance(coin) < 20:      # 코인 먹는 범위
            speed+=1
            score +=1
            t.write(f"score : {score}",False,"center",("",20))
            t.clear()
            coin_x=random.randint(-230,230)
            coin_y=random.randint(-230,230)
            coin.goto(coin_x,coin_y)
      
      if playing:       #게임이 계속 이어가게 함
            t.ontimer(play,100)
            
def message(m1,m2):
      t.clear()
      t.goto(0,-150)
      t.write(m1,False,"center",(' ',15))
      t.goto(0,-100)
      t.write(m2,False,"center",(' ',15))
      t.home()

# 환경 설정
t.title("도망치기 게임2") 
t.setup(500,500)
t.bgcolor("skyblue")
t.up()
t.ht()


message("방향키 이동 코인은 노란색!","[스페이스바 누르면 시작]")  # 시작 메세지
