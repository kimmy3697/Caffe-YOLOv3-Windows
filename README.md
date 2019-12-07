# caffe-yolov3-windows 설치, 커스텀 LMDB, 학습



#  Detection 기준으로 설명합니다. ㅠ 저도 이거 밖에 안해봤어요 ㅠㅠ

### Configuring and Building Caffe 

#### Requirements 준비물~

 - Visual Studio 2015(이거 2017에 개발도구만 2015써서 해볼랬는데 실패함)
 
 **VS 설치시 유의 ::**
 win sdk가 필요한데 정확히 뭔지 몰라서 보이는거 전부 체크하고 했음 ㅋㅋ 제대로 아시는분은 필요한것만 하시면 됩니다. 
 
 ![enter image description here](https://github.com/kimmy3697/Caffe-YOLOv3-Windows/blob/master/vs2015custom_install.PNG?raw=true)

 - [CMake](https://cmake.org/) 3.4 or higher (Visual Studio and [Ninja](https://ninja-build.org/) generators are supported)(그냥 최신버전 암거나 쓰셈) 참고로 왠만하면 설치프로그램으로 하시는게 편합니다. 시스템 패스도 설치하면서 자동으로 추가해주고 뭐 여튼 좋음. CMake 홈페이지로 가셔서 윈도우 버전의 msi 파일로 설치하세요~
 - Anaconda (그냥 프롬프트 암거나 쓰면 됨)
 - CUDAToolkit8.0 
 - any cuDNN version suitable with CUDAToolkit8.0
 - 주의할 점 CUDAToolkit 설치시 visual studio integration 항목을 포함하는지 반드시 확인할 것, 또한 설치 완료후 정상적으로 설치됨 뜨는지 확인할 것. 



### 빌드 하는 방법

**build_win.cmd 파일 편집**
script 폴더안에 build_win.cmd 파일을 우클릭으로 여시고 cuDNN 경로를 잡아 줘야됩니다. 제가 여러분을 위해 코드의 168번줄에 미리 표기해뒀으니 잡아 주시면 됩니다. cuDNN 파일의 압축을 푸시면 폴더 겁나 많고 파일도 겁나 많죠? 
압축풀어주신 경로를 168번 줄에 설정해주시면 됩니다.

![enter image description here](https://github.com/kimmy3697/Caffe-YOLOv3-Windows/blob/master/CodeCapture.PNG?raw=true)


**빌드 커맨드 파일 실행**
```
> cd $caffe_root
> script/build_win.cmd 
```


### Mobilenet-YOLO 데모 실행 (중간 점검 차원)

```
> cd $caffe_root/
> examples\demo_yolo_lite.cmd
```
뭔가 이미지가 나오고 바운딩 박스에 오브젝트를 검출해주면 여기까진 성공한거에요~

### 학습 데이터 준비 (LMDB 다운로드)

다운로드 [lmdb](https://drive.google.com/open?id=19pBP1NwomDvm43xxgDaRuj_X4KubwuCZ)

카페 루트폴더에 압축풀기 $caffe_root/ 

압축 해제 후 아래 경로가 제대로 있는지 확인할 것 "$caffe_root\examples\VOC0712\VOC0712_trainval_lmdb"

## 학습 데이터 준비 (LMDB 직접 만들기)

## 이미지 준비 (학습에 사용하고 싶은 이미지)
디텍션시에 사용하고 싶은 데이터를 먼저 수집하셔야 해요!
예를 들면 보행자 검출을 위해 도로에 설치된 카메라 영상 데이터라던가 뭐든지 상관없으니 일단 수집합시다. 
 ## Annotation 도구 사용
 이미지를 수집했으니 이미지에 맞는 레이블과 바운딩 박스를 설정하는 작업을 해줘야 하는데 보통의 경우 xml 이나 txt로 된 파일을 만드는 겁니다.  
![xml 파일내부는 대충 이런 모습입니다.](https://github.com/kimmy3697/Caffe-YOLOv3-Windows/blob/master/xmlExample.PNG?raw=true)![txt 파일내부는 대충 이런 모습입니다.](https://github.com/kimmy3697/Caffe-YOLOv3-Windows/blob/master/txtExample.PNG?raw=true)
위와 같이 만들건데 지금은 xml만 있으면 되요. txt로 하는 방법도 있다고 하더라구요. 대충 무슨 상황이냐면 이미지 하나에 총 8개의 오브젝트를 잡은거고 맨 앞에 숫자는 레이블의 번호에요. 우리 딥러닝 공부할 때 제일 첨에 배우는 MNIST 소프트맥스 맨끝에 0~9 까지 나오죠? 그거라고 생각하시면 되용. 

## labelImg 도구 사용
아주 친절하게도 우리의 헌신적인 연구자분들이 만들어주신 annotation 도구를 사용할 겁니다. 
[LabelImg 리포지토리 가기](https://github.com/kimmy3697/labelImg)
Fork 해서 가져온 리포지토리구요 윈도우버전만 사용한다는 가정하에 마크다운만 조금 수정했어요. 일단 링크의 리포지토리로 가서 마저 진행하시고 다시 이 문서로 돌아오시면 되요! 

아 참고로 말씀드리자면 지금 사용하는 xml 포맷은 pascal voc 포맷이고 yolo에서도 사용하는 포맷입니다. 그러니까 voc 데이터를 yolo에서도 사용할 수 있다~ 이말입니다! 아쉬겠어요? 

## 데이터 리스트 생성

 - pythonTool 폴더 안에 파이썬 코드 하나 만들어 넣었어요~ 간단한 코드지만 직접 만드는건 귀찮으니까... 그냥 이거 사용법을 알려드릴게요... 맘에 안드는 부분은 수정하시면 될 거에요.
여튼 anaconda 나 뭐 기타 python 실행 되는걸로 실행 시켜줍시다.
그러고 나면 뭐 입력하라고 하는데 생성할 데이터 리스트의 이름을 정해주시면 됩니다. 이름만 쓰시고 생성된 파일에 .txt를 붙이셔도 되고 아니면 그냥 바로 .txt 로 지정해주셔도 됩니다. 그러면 총 3번 폴더를 선택하라고 나오는데 첫번째는 이미지 폴더, 두번째는 어노테이션 폴더, 세번째는 데이터 리스트 저장할 폴더를 묻는겁니다. 주의 하실점은 앞에 두 폴더는 반드시 같은 폴더 하위에 있어야 합니다. 헷갈리시면 제가 만들어 놓은 pythonTool 폴더 내부에 예시가 있으니 DataSet 폴더의 img 폴더와 anno 폴더를 활용하시면 됩니다.
 - 데이터리스트 파일이 완성됬을때 아래와 같이 나오면 됩니다.
 - ![enter image description here](https://github.com/kimmy3697/Caffe-YOLOv3-Windows/blob/master/path_pairing_cap.png?raw=true)
 - 이제 우리 labelImg 만들때 

## LMDB 생성
LMDB 생성은 build/tools/Release 폴더안에 convert_annoset.exe 파일을 이용합니다. 해당 경로에서 powershell을 켜주시고 

•./convert_annoset --anno_type=detection --label_map_file=./outputTEST.prototxt --resize_width=320 --resize_height=320 --encoded=true C:\CaffeThings\DK_TEST_PILOT\TRAIN/ C:\CaffeThings\DK_TEST_PILOT\TRAIN\SpaceX.txt Resized_DK_LMDB_Train

•./convert_annoset --anno_type=detection --label_map_file=./outputTEST.prototxt --resize_width=320 --resize_height=320 --encoded=true C:\CaffeThings\DK_TEST_PILOT\TEST/ C:\CaffeThings\DK_TEST_PILOT\TEST\SpaceX_Test.txt Resized_DK_LMDB_Test

### Trainning Mobilenet-YOLOv3
  
```
> cd $caffe_root/
> examples\train_yolov3_lite.cmd
```

## Reference

> https://github.com/weiliu89/caffe/tree/ssd

> https://pjreddie.com/darknet/yolo/

> https://github.com/gklz1982/caffe-yolov2

> https://github.com/duangenquan/YoloV2NCS

> https://github.com/eric612/Vehicle-Detection

> https://github.com/eric612/MobileNet-SSD-windows

> https://github.com/eric612/Caffe-YOLOv3-Windows

## License and Citation


Please cite MobileNet-YOLO in your publications if it helps your research:

    @article{MobileNet-YOLO,
      Author = {eric612,Avisonic},
      Year = {2018}
    }
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MDc4NjYwNzgsMjAxNDk0NTY5MiwxMD
AyMTU5ODQxLC0yMTA4MTgxNDk5LDE2Njk0NTE3MjMsLTE4OTQ1
NjgyMDEsLTE5ODEyNTg4MDYsMTM2NjkyMzc1MSwxOTc4MzkxNj
YzLC04NjM0MzM4MDEsLTY0ODQxMjgyNyw4NDIzODEyMzcsLTE2
NzEyNzY0NTEsNjU4NTkzODBdfQ==
-->