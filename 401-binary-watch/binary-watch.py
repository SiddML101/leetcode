from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        for h in range(12):
            for m in range(60):
                if (h.bit_count() + m.bit_count()) == turnedOn:
                    result.append(f"{h}:{m:02d}")
        
        return result

        
        
        