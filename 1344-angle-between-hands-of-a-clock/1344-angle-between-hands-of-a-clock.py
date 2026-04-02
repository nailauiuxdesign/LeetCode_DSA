class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_deg = minutes * 6
        hour_deg = ((hour + minutes / 60) / 12) * 360 % 360

        diff = abs(min_deg - hour_deg)
        return min(diff, 360 - diff)
