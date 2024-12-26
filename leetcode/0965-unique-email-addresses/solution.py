class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # l = []

        # for email in emails:
        #     s = ""
        #     for check in email.split('@')[0]:
        #         if check == '+':
        #             break
        #         if check!='.':
        #             s+=check
        #     e = s+'@'+email.split('@')[1]
        #     if e not in l:
        #         l.append(e)
        # return len(l)
        
        uniqueEmails = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            uniqueEmails.add(local + '@' + domain)

        return len(uniqueEmails)
        

