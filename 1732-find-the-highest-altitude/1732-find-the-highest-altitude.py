class Solution:
  def largestAltitude(self, gain: list[int]) -> int:
    res = 0
    altitude = 0
    for change in gain:
      altitude += change
      res = max(res, altitude)
    return res