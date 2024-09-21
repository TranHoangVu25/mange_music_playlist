import webbrowser


class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link
        self.seen = False
    def open(self):
        webbrowser.open(self.link)
        self.seen = True
class Playlist:
    def __init__(self,name,description,rating,videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

def enter_video():
    title = input("Enter title:")+"\n"
    link = input("Enter link:")+"\n"
    video = Video(title,link)
    return video
def print_video(video):
    print("Title:",video.title,end="")
    print("Link",video.link,end="")
def enter_videos():
    total = int(input("Enter num of video:"))
    videos = []
    for i in range(total):
        print("Video:",(i+1))
        video = enter_video()
        videos.append(video)
    return videos
def print_videos(videos):
    total = len(videos)
    for i in range(total):
        print("Video:",(i+1))
        print_video(videos[i])
def enter_playlist():
    name = input("Enter name:")+"\n"
    des = input("Enter des:")+"\n"
    rating = input("Enter rating(1-5):")+"\n"
    videos = enter_videos()
    playlist = Playlist(name,des,rating,videos)
    return playlist
def print_playlist(playlist):
    print("Name:",playlist.name,end="")
    print('Description:',playlist.description,end="")
    print("Rating",str(playlist.rating),end="")
    print_videos(playlist.videos)

def print_video_txt(file,video):
    file.write(video.title)
    file.write(video.link)

def print_videos_txt(file,videos):
    total = len(videos)
    file.write(str(total)+"\n")
    for i in range(total):
        print_video_txt(file,videos[i])

def print_playlist_txt(playlist):
    with open("output.txt", "w") as file:
        file.write(playlist.name)
        file.write(playlist.description)
        file.write(str(playlist.rating))
        print_videos_txt(file,playlist.videos)

def read_video_txt(file):
    tille = file.readline()
    link = file.readline()
    video = Video(tille,link)
    return video

def read_videos_txt(file):
    videos = []
    total = file.readline()
    for i in range(int(total)):
        vd = read_video_txt(file)
        videos.append(vd)
    return videos

def read_playlist_txt():
    with open("output.txt", "r") as file:
        name = file.readline()
        des = file.readline()
        rating = file.readline()
        videos = read_videos_txt(file)
        playlist = Playlist(name,des,rating,videos)
        return playlist


# function ensure choice in range (min,max)
# isdigit() check that choice is str or not if is str return true
def select_in_range(prompt,min,max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice = int(choice)
    return choice

# function add video
def add_video(playlist):
    print("Enter new video information:")
    title = input("Enter title")+"\n"
    link = input("Enter link:") +"\n"
    video = Video(title,link)
    playlist.videos.append(video)
    return playlist

def play_video(playlist):
    print_videos(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range("Select video (1,"+str(total)+":)",1,total)
    print("Open video: "+playlist.videos[choice-1].title+"---"+playlist.videos[choice-1].link)
    playlist.videos[choice-1].open()

def update_playlist(playlist):
    print("Update playlist")
    print("1.Name")
    print("2.Description")
    print("3.Rating")
    print("4.All")
    choice = select_in_range("Select option(1,3)",1,3)
    if choice == 1:
        name = input("Enter name:")
        playlist.name = name
        return playlist

    if choice == 2:
        description = input("Enter description:")
        playlist.description = description
        return playlist

    if choice == 3:
        rating = input("Enter rating:")
        playlist.rating = rating
        return playlist

    # if choice == 4:
    #     name = input("Enter name:")
    #     description = input("Enter description:")
    #     rating = input("Enter rating:")
    #     playlist = Playlist(name,description,rating)
    #     return playlist

def delete_video(playlist):
    choice = select_in_range("Select video that you want to delete(1"+str(len(playlist.videos)),1,len(playlist.videos))
    del playlist.videos[choice-1]
    return playlist

def show_menu():
    print("Main Menu:")
    print("---------------------")
    print("|1. Create playlist  |")
    print("|2. Show playlist    |")
    print("|3. Play a video     |")
    print("|4. Add a video      |")
    print("|5. Update playlist  |")
    print("|6. Delete a video   |")
    print("|7. Save and exit    |")
    print("---------------------")

def main():
    try:
        playlist = read_playlist_txt()
        print("Loaded data success")
    except:
        print("Welcome user!!")
    while True:
        show_menu()
        choice = select_in_range("Select an option (1-7):",1,7)
        if choice == 1:
            playlist = enter_playlist()
            input("\nPress Enter to continue.\n")
        elif choice == 2:
            print_playlist(playlist)
            input("\nPress Enter to continue.\n")
        elif choice == 3:
            playlist = play_video(playlist)
        elif choice == 4:
            playlist = add_video(playlist)
            input("\nPress Enter to continue.\n")

        elif choice == 5:
            playlist = update_playlist(playlist)
        elif choice == 6:
            playlist = delete_video(playlist)
        elif choice == 7:
            print_playlist_txt(playlist)
            input("\nPress Enter to continue.\n")
            break

main()