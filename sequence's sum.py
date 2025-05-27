def sequence_sum (n):
  u=2
  s=0
  for i in range (0,n+1):
    s=s+u
    u=0.2*u+1
  return (s)

print(sequence_sum(10))
