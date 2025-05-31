#/usr/bin/python3

class Ranking:
  def __init__(self):
    self.data = {}

  def __setitem__(self,key,value):
    self.data[key] = value

  def __getitem__(self, key):
    return self.data[key]

  def __str__(self):
    result = ""
      for key in sorted(self.data):
        result += f"{key}: {self.data[key]}\n"
      return result.strip()  

r=Ranking()
r[1]="Amancio Ortega"
r[2]="Carlos Slim"
r[3]="Bill Gates"
print(r[1])
print(r)


