def threshold ():
  n=0
  u=2
  while u<=8:
    n=n+1
    u=0.9*u+1
  return (n)

print(threshold())
