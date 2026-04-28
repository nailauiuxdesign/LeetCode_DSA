class Solution:
    def numUniqueEmails(self, emails):
        unique = set()
        
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')

            unique.add(local + '@' + domain)
        return len(unique)