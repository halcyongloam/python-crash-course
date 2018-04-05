# store a name with whitespace on both sides of it, then print it with it
# stripped left, right, and totally. Vertical bars are used to show the
# whitespace
name = '    Candi    '
print('Original:' + '\n\t' + '|' + name + '|' + '\n'
      + 'Left:' + '\n\t' + '|' + name.lstrip() + '|' + '\n'
      + 'Right:' + '\n\t' + '|' + name.rstrip() + '|' + '\n'
      + 'Final:' + '\n\t' + '|' + name.strip() + '|')
