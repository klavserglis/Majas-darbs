import time
print("Ko tev atgadinat?")
text = str(input())
print("Pec cik?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)