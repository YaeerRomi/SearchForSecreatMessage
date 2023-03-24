class findMessage():

  def __init__(self, textF, stepsF, letters):
    self.matrix = []
    self.matrixF = textF

    self.steps = []
    self.stepsF = stepsF

    self.fLetterPos = []
    self.firstLetters = letters

    self.readLetterMatrix()
    self.readSteps()
    self.findFirstLetters()

  def readLetterMatrix(self):
    matrixFile = open(self.matrixF, "r")
    mLines = matrixFile.readlines()
    # Removing the last character
    for i in mLines:
      i = list(i[0:-1])
      self.matrix.append(list(i))
    matrixFile.close()

  def readSteps(self):
    stepsFile = open(self.stepsF, 'r')
    sLines = stepsFile.readlines()
    numbers = []
    for i in sLines:
      numbers = []
      i = i[0:-1]  # Removing New Line Character
      for num in i.split():
        numbers.append(int(num))
      self.steps.append(numbers)
    stepsFile.close()

  def findFirstLetters(self):
    letter = self.firstLetters[0]
    for x in range(len(self.matrix)):
      for y in range(len(self.matrix[0])):
        if letter == self.matrix[x][y]:
          self.fLetterPos.append([x, y])
    if len(self.fLetterPos) == 0:
      print("First letter not found in matrix.")
      return False
    else:
      return True

  def findCombination(self):
    for pos in self.fLetterPos:
      message = self.firstLetters[0]
      currentPos = pos
      for s in range(1, len(self.steps)):
        currentStep = self.steps[s % len(self.steps) - 1]
        nextLetterPos = [(currentPos[0] + currentStep[0]) % len(self.matrix),
                         (currentPos[1] + currentStep[1]) % len(self.matrix[0])
                         ]
        #Row: (2 + 1) % 4 = 3
        #Column: (3 - 1) % 4 = 2
        currentPos = nextLetterPos
        nextLetter = self.matrix[nextLetterPos[0]][nextLetterPos[1]]
        message += nextLetter

      if message.startswith(self.firstLetters):
        print("Secret word found: " + message)
        return message

    print("Secret word not found.")
    return None

  def extract_message(self):
    if self.findFirstLetters():
      return self.findCombination()
    else:
      return "Message could not be extracted"


text = "cof"
game = findMessage("test2.txt", "steps2.txt", text)
game.extract_message()
