#secrets gera números aleatórios seguros

import secrets



random = secrets.SystemRandom() # permite usar tudo do random com o secret, e o seed é ignorado
#print(secrets.randbelow(100))
#print(secrets.choice([10, 11, 12]))
r_int = random.randint(10, 20)
#print(r_int)

from secrets import SystemRandom as Sr 
import string as s

print(''.join(Sr().choices(s.ascii_letters + s.digits, k=20)))

