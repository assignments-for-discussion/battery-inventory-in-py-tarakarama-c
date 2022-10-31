
def count_batteries_by_usage(cycles):
  l=0
  m=0
  h=0
  for x in cycles:
    if x <410:
      l+=1
    elif x>=410 and x=<949:
      m+=1
    else x>=950:
      h+=10
      
  return {
    "lowCount": l,
    "mediumCount": m,
    "highCount": h
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
