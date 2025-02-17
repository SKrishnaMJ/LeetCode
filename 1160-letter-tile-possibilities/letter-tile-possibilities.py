class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        setx=set()
        def part(path, available):
            setx.add(path)
            if not available:
                return
            for i in range(len(available)):
                part(path+available[i], available[:i]+available[i+1:])
        
        part(" ", tiles)
        return len(setx)-1

            



        
        