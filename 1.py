# import random
# user_id = [random.randint(1, 40) for _ in range(40)]
# result = list(a for a in user_id if (a>=10 and a<=20))
# print(result)
import random 
import time
def generate_user_ids():
    while True:
        yield random.randint(1, 999)
    
user_stream = generate_user_ids()
print('начинаем получать данные')
for i in range(10):
    print(next(user_stream)) 
    time.sleep(0.5)