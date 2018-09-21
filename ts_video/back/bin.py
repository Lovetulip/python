
from core import kankanwu 
from cor import muit_down
def main():
    video_link = kankanwu.get_video_link()
    #for i in range(0,40):
    #    print("you can have choose some movie to download,index %s , name%s"%((i+1),video_link[i][0]))


    reply_Num = input("\033[33;1m please input index of movie \033[0m ").strip()
    
    print(video_link[int(reply_Num) - 1][1])
    reply_Num_link =kankanwu.get_source_link(video_link[int(reply_Num) - 1][1])
    if ".m3u8" in reply_Num_link: 
        muit_down.muit_thread(reply_Num_link)
    else :
        print("link has error")

if __name__ == "__main__":
    main()
