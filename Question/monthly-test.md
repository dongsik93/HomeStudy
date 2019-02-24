# monthly-test



## 박스모델

- 바깥 여백 영역 : Margin
- 테두리 영역 : Border
- 안쪽 여백 영역 : Padding
- 내용 영역 : Content



#### 박스모델의 속성

- 바깥 여백 : margin
- 테두리 : border
- 안쪽여백 : padding
- 박스의 가로 크기 : width
- 박스의 세로 크기 : height
- 박스의 크기 기준 : box-sizing
- 박스의 배경 : background



#### 속성값 부여

- padding / margin : `xx`(위)  `yy`(오른쪽)  `zz`(아래)  `ww` (왼쪽)
  - 두개면, 즉 xx yy만 적으면 xx(위) yy(아래)
  - 세개면, 즉 xx yy zz 면 xx(위) yy(좌우) zz(아래)
- padding / margin-top / right / bottom / left
- padding / margin-auto : 요소를 가운데 정렬( 문단 정렬이 아니라 요소를 가운데에 위치시키는 것)



#### border

- 테두리를 만드는 속성
- border-width : 선의 두께
- border-style : 선의 모양
- border-color : 선의 색

```css
.c {
    border-top : solid red 10px
}
```

테두리를 둥글게 만들기

- boreder-radius : %, px



##### background-image

- background-image : url( 상대경로 / 절대경로 );



##### opacity

- 선택한 요소의 배경과 내용 모두를 투명하게 만든다
- rgba(255, 255, 255, 0,5) 이렇게 줄수도 있음 0.5!



## Bootstrap




```html
<div id="a" class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
    box box box
</div>

<div id="a" class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
    box box box
</div>

<div id="a" class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
    box box box
</div>

<div id="a" class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
    box box box
</div>
```



## django





















