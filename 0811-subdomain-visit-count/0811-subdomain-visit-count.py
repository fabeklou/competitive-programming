class Solution:
    def countDomain(self, num: int, addr: str, hmap):
        domains = addr.split('.')
        length = len(domains)
        for i in range(length - 1, -1, -1):
            hmap['.'.join(domains[i:])] += num

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hmap = defaultdict(int)
        
        for cpd in cpdomains:
            count, addr = cpd.split()
            count_int = int(count)
            # set or update count of domains            
            self.countDomain(count_int, addr, hmap)

        return [f"{value} {key}" for key, value in hmap.items()]
