from pprint import pp


class Cookie:
  def __init__(self, color):
    self.color = color

  def get_color(self):
    return self.color

  def set_color(self, color):
    self.color = color

  def __str__(self):
    return f"Cookie['{self.color}']"

  def __repr__(self):
    return f"Cookie['{self.color}']"



cookie_one = Cookie("green")
cookie_two = Cookie("blue")
cookie_three = Cookie("red")

if __name__ == "__main__":
  pp([cookie_one, cookie_two, cookie_three])
  cookie_one.set_color("pink")
  pp([cookie_one, cookie_two, cookie_three])
