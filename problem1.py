class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def connect_server():
    links = list()
    for i in range(12):
        links.append(Node(3))
        if i > 0:
            links[i-1].next = links[i]
            links[i].data *= links[i-1].data
    return links

class Problem1:
    def __init__(self,d):
        self.data = d
        self.data['unlock'] = False
        self.links = list()
        for i in range(12):
            self.links.append(Node(3))
            if i > 0:
                self.links[i-1].next = self.links[i]
                self.links[i].data *= self.links[i-1].data
    def get_contacts(self):
        return self.links[0]
    def unlock(self, passcode):
        if passcode == 6561:
            print(self.data)
            self.data['unlock'] = True
            print("Unlocked!")
        else:
            print("Access denied")


def unlock(passcode):
    p.unlock(passcode)
