def solveHangMan(length, livesCount):
    lettersCorrect = []
    lettersUsed = {}
    while (livesCount > 0):

        c = chr(random(0, 26) + 96)
        if c not in letterUsed:
            letterUsed[c] = True

        lettersUsed.append(c)
        if not guess(c):
            livesCount = livesCount - 1
        else:
            lettersCorrect.append(c)
    if len(letters) == lenght:
        return True
    return False


def guess(c):
    if c in w:
        return True
    return False
#
# Your previous Java content is preserved below:
#
# /*
#  Hangman Game: (5 charactes and 6 lifes)
#
#  - - - - -
#  Guess A - No
#  No of lives = 5
#
#  A _ _ L _
#
#  WIN/LOST
#
#  Design a hangman solver method given number of letters in the word and number of lives
#
#  WIN/LOST solveHangman( Integer length, Integer livesCount)
#
#  API available:  guess(Char c)
#
#  */
#
#
#
