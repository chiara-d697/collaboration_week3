correct_pin = 3125
count = 1
while count <= 3:
  supplied_pin = int(input("Please enter your PIN:"))
  if count >= 3:
      print("Three wrong attempts, your card has been blocked. Please contact your bank.")
      break
  elif supplied_pin != correct_pin and count == 2:
      print("Incorrect PIN. One attempt remaining")
      count += 1
  elif supplied_pin != correct_pin :
      print("Incorrect PIN. Two attempts Remaining.")
      count += 1
  else :
      print("PIN correct. Please proceed.")
      break