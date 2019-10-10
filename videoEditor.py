import cv2
import datetime

# SIMPLE RECORDER
def simpleRecorder():
  cap = cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(f'outputs\\{input("Please Set File name : ")}.avi', fourcc, 20, (640,480))

  #print(cap.isOpened())
  while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cdate = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,cdate,(10,80),font,0.7,(255,0,0),1)
        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
      else:
          break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

# SLOW MOTION EFFECT  
def slowMotion():
  cap = cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(f'outputs\\{input("Please Set File name : ")}.avi', fourcc, 8, (640,480))

  #print(cap.isOpened())
  while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
      else:
          break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
  
  
# FAST MOTION EFFECT   
def fastMotion():
  cap = cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(f'outputs\\{input("Please Set File name : ")}.avi', fourcc, 200, (640,480))

  #print(cap.isOpened())
  i=0
  while(cap.isOpened()):
      i=i+1
      ret, frame = cap.read()
      if ret == True:
        img = frame
        #cv2.imwrite(str(i)+"img.jpg",img) 
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
      else:
          break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

# REVERSE VIDEO
def reverseVideo():
  cap=cv2.VideoCapture(0)
  fourcc=cv2.VideoWriter_fourcc(*'XVID')
  out=cv2.VideoWriter(f'outputs\\{input("Please Set File name : ")}.avi',fourcc, 20,(640,480))
  img=[]
  while(cap.isOpened()):
      ret,frame=cap.read()
      if ret == True:
          img.append(frame)
          cv2.imshow('frame',frame)

          if cv2.waitKey(1) & 0xFF == ord('q'):
              break

      else:
          break

  cap.release()
  img.reverse()
  for item in img:
      out.write(item)
  out.release()
  cv2.destroyAllWindows()

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

# CONVERT TO B/W
def convertToBW():
  cap = cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(f'outputs\\{input("Please Set File name : ")}.avi', fourcc, 20, (640,480))

  #print(cap.isOpened())
  
  while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
        frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(frame1, cv2.COLOR_GRAY2BGR)
        out.write(gray)
     		       
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
      else:
          break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

def videoMerger():
  path1=input("Enter path for video1 : ")
  path2=input("Enter path for video2 : ")

  vid1 = cv2.VideoCapture(path1)
  vid2 = cv2.VideoCapture(path2)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(f'outputs\\{input("Please Set File name : ")}.avi', fourcc, 20.0, (640,480))
  frame_list=[]
  while True:
      ret ,frame = vid1.read()
      if ret==True:
          frame_list.append(frame)
      else:
          break
  while True:
      ret ,frame = vid2.read()
      if ret==True:
          frame_list.append(frame)
          
      else:
          break
  for frame in frame_list:
      out.write(frame)
  vid1.release()
  vid2.release()

# Image Extractor
def ImageExtractor():
  cap = cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(f'outputs\\{input("Please Set File name : ")}.avi', fourcc, 20, (640,480))

  #print(cap.isOpened())
  i=0
  while(cap.isOpened()):
      i=i+1
      ret, frame = cap.read()
      if ret == True:
        img = frame
        cv2.imwrite("extracted_images\\"+str(i)+"img.jpg",img) 
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
      else:
          break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

#main driver code
print("Welcome to Video Editor")
print("Choose a option from below list: ")
print("1. Reverse the video")
print("2. Slow Motion Effect")
print("3. Fast Motion Effect")
print("4. Extract Images from video")
print("5. Merge two videos")
print("6. Simple Recorder")
print("7. Convert Video into B/W")
print("8. Terminate")

options = {
                1 : reverseVideo,
                2 : slowMotion,
                3 : fastMotion,
                4 : ImageExtractor,
                5 : videoMerger,
                6 : simpleRecorder,
                7 : convertToBW,
}
choice = 0
try:
  while choice!=8:
    choice = int(input("Enter a number of your Choice(1/2/3/4/5/6/7/8) : "))
    options[choice]()
except:
  print("Invalid Choice")
  
    

  
