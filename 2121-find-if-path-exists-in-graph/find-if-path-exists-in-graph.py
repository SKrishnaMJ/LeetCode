class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        my_dict = defaultdict(list)
        for u,v in edges:
            my_dict[u].append(v)
            my_dict[v].append(u)
        setx = set()
        setx.add(source)
        st = [source]
        while st:
            node = st.pop()
            if node==destination:
                return True
            for n in my_dict[node]:
                if n not in setx:
                    setx.add(n)
                    st.append(n)
        return False

        