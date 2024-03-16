colors = ['red', 'green', 'purple']
shapes = ['squiggle', 'oval', 'diamond']
fillings = ['empty', 'striped', 'filled']
numbers = [1, 2, 3]

properties = {
  'color': colors,
  'shape': shapes,
  'filling': fillings,
  'number': numbers
}

def build_deck():
  deck = []
  for c in colors:
    for s in shapes:
      for f in fillings:
        for n in numbers:
          card = Card(c, s, f, n)
          deck.append(card)
  return deck

class Card:
  def __init__(self, color, shape, filling, number) -> None:
    self.color = color
    self.shape = shape
    self.filling = filling
    self.number = number


  def get_fitting_card(self, card):
    card1 = self.__dict__
    card2 = card.__dict__
    card3 = {}

    for key, val1 in card1.items():
      val2 = card2[key]
      if val1 == val2:
        card3[key] = val1
      else:
        card3[key] = [x for x in properties[key] if x != val1 and x != val2][0]

    return Card(*card3.values())


  def __eq__(self, card) -> bool:
    if card.color == self.color \
      and card.shape == self.shape \
      and card.filling == self.filling \
      and card.number == self.number:
      return True
    return False
  
  def __str__(self) -> str:
    return self.__dict__.__str__()
  
  def __repr__(self) -> str:
    return self.__str__()
