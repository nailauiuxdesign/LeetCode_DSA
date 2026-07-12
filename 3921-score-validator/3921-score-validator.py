class Solution:
    def scoreValidator(self, events):
        score = 0
        wickets = 0

        for event in events:
            if event == "W":
                wickets += 1
            elif event == "WD" or event == "NB":
                score += 1
            else:
                score += int(event)
            if wickets == 10:
                break

        return [score, wickets]
