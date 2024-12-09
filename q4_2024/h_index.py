"""
DCP:605

In academia, the h-index is a metric used to calculate the impact of a researcher's papers. 
It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. 
If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. 
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.

"""

paper_cits = [3,6,4,7,5,2]


def find_h_index(paper_citations):
    count_dict = {}
    for elem in paper_cits:
        cnt_val = len(list(filter(lambda x:x >= elem, paper_citations)))
        count_dict[elem] = cnt_val
        
    for k,v in count_dict.items():
        if k == v:
            return k

print(find_h_index(paper_cits))