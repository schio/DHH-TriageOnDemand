# 2018 DHH(Digital Health Hackathon)-TriageOnDemand



## 재난상황에서의 수요(환자)와 공급(의료진 및 키트 등) 실시간 모니터링 및 대응
------------------

ZEPPELIN을 통한 정보 제공

1. 대시보드 - 전체 환자 수, 트리아지 구분 별 환자 수, 전체 환자 리스트, 외부물자 리스트 등 제공
2. 환자 상세 검색 - 이름으로 환자 검색, 사진으로 환자 검색, 환자 상세 정보 제공
3. 각 재난 종료 후 결과보고 - 예방 사망률, ROC 커브 등 


Screenshots
-----------

![dashboard](https://user-images.githubusercontent.com/19237348/47692972-0d5a4100-dc3b-11e8-88f8-5041e88a117f.jpg)

![search](https://user-images.githubusercontent.com/19237348/47692974-0df2d780-dc3b-11e8-8f9a-44f2aa584baa.jpg)

![outcome](https://user-images.githubusercontent.com/19237348/47692973-0d5a4100-dc3b-11e8-99a8-c07212c3d5ad.jpg)






## 드론 영상을 통한 재난 현장 지도 리모델링
--------------
디바이스 장착을 통해 실시간 바이탈 사인, 위경도 수집
모델링 된 지도 상에 실시간 환자 위치 

지진재난상황 등에서는 기존의 지도이미지가 무용지물입니다.<br>
드론을 이용하여 재난현장을 촬영한 후 WebODM을 이용하여 모델링합니다.<br>
이후 환자에게 부착된 디바이스에서 받은 위경도를 모델링 된 이미지에 맵핑하여 전체 재난현장을 모니터링합니다.<br>

MESHLAB
---------------
![default](https://user-images.githubusercontent.com/19237348/47696858-e6583b00-dc4b-11e8-88b5-68cb48afcc1f.png)


WebODM
---------------
![1](https://user-images.githubusercontent.com/19237348/47697040-aa71a580-dc4c-11e8-99f5-4bb31da8e1eb.jpg)
![2](https://user-images.githubusercontent.com/19237348/47697041-aa71a580-dc4c-11e8-8b59-93fd4f8bcb74.jpg)

