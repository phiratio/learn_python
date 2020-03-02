# class Apple(object):
#
#     def __init__(self):
#         self.zdr = "asl kp :D:D:D:D"
#
#     def apple(self):
#         print(self.zdr)
#
#
# hm = Apple()
# hm.apple()
# print(hm.zdr)


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


text = [123, 456, 789, 123, 456, 6677, 123, 9988, 44]
happy_bday = Song(text)

happy_bday.sing_me_a_song()
