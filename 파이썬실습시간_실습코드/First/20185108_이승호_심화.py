King = 1
Queen = 1
Look = 2
Bishop = 2
Night = 2
Phone = 8

find_King = int(input("찾은 킹의 개수를 입력하세요: "))
find_Queen = int(input("찾은 퀸의 개수를 입력하세요: "))
find_Look = int(input("찾은 룩의 개수를 입력하세요: "))
find_Bishop = int(input("찾은 비숍의 개수를 입력하세요: "))
find_Night = int(input("찾은 나이트의 개수를 입력하세요: "))
find_Phone = int(input("찾은 폰의 개수를 입력하세요: "))

King = King - find_King
Queen = Queen - find_Queen
Look = Look - find_Look
Bishop = Bishop - find_Bishop
Night = Night - find_Night
Phone = Phone - find_Phone

print(str(King) + " " + str(Queen) + " " + str(Look) + " " + str(Bishop) + " " + str(Night) + " " + str(Phone))




