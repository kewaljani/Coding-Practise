import json

def phrasel_search(P, Queries):
    ans = [[]]
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P = ["i would have", "they love", "i analyzed", "made decision"]
        Queries = ["since this morning i have analyzed all the data from the company and made my decision",
        "they love the idea",]
        p = []
        q = []
        for i in P:
            p.append(i.split(" "))
        for j in Queries:
            q.append(j.split(" "))
        top = 0
        front = 0
        flag = 0
        temp_str = ""
        found = []
        ans = []
        queries = q[0]
        while top<=len(q)-1:
            queries = q[top]
            for phrase in p:

                for i in queries:
                    if flag==1:
                        if front<=len(phrase)-1:
                            if count ==2:
                                temp_str = ""
                                front = 0
                                flag = 0
                                continue
                            elif phrase[front]!=i:
                                temp_str+=" "+i
                                count+=1
                            elif phrase[front]==i:
                                temp_str+=" "+i
                                count = 0
                                front+=1
                        if front>len(phrase)-1:
                            if temp_str!="":
                                found.append(temp_str)
                            temp_str = ""
                            front = 0
                            flag = 0
                        continue

                    if phrase[front] == i and flag==0:
                        temp_str+=i
                        count = 0
                        front+=1
                        flag = 1
            ans.append(found)
            found =[]
            top+=1
        print(ans)