import random
lottozahlen_alle = []
lottozahlen_alle.extend(range(1,50))
lottozahlen_gewinner = random.sample(lottozahlen_alle, 6)
lottozahlen_gewinner.sort()
print(lottozahlen_gewinner)
print(random.choices(lottozahlen_alle, k=6))