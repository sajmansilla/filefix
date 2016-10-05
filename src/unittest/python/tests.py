import __init__
import view
import model.clases
import control

from mockito import *

obj = mock()

# pass it around, eventually it will be used
obj.say('Hi')

# back in the tests, verify interactions
verify(obj).say('Hi')
verifyNoMoreInteractions(obj)

