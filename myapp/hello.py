import fire

def hello(name="World"):
  return "Hello sai %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)