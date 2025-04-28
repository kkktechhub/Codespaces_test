# prompt: ジャンケンをプログラミングしてください

import random

def janken():
  hands = {0: "グー", 1: "チョキ", 2: "パー"}
  user_hand = int(input("0:グー, 1:チョキ, 2:パー\nあなたの手を入力してください: "))

  if user_hand not in hands:
      print("無効な入力です。0、1、または2を入力してください。")
      return

  computer_hand = random.randint(0, 2)

  print(f"あなたの選択: {hands[user_hand]}")
  print(f"コンピューターの選択: {hands[computer_hand]}")


  if user_hand == computer_hand:
      print("引き分けです！")
  elif (user_hand == 0 and computer_hand == 1) or \
       (user_hand == 1 and computer_hand == 2) or \
       (user_hand == 2 and computer_hand == 0):
      print("あなたの勝ちです！")
  else:
      print("コンピューターの勝ちです！")

janken()
