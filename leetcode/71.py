class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == '/':
            return '/'
        names_list = path.split('/')
        names_list = [
            name for name in names_list if name != '.' and name != '']
        ans_list = []
        for name in names_list:
            if name != '.' and name != '' and name != '..':
                ans_list.append(name)
            elif name == '..' and len(ans_list) >= 1:
                ans_list.pop()
        return '/' + '/'.join(ans_list)
