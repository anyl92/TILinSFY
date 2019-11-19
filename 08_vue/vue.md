method : function 키워드로 저장했을 때

this -> me



method : () => {}

this -> window



watch를 쓰먄 안되는 이유 - 과목에 나올가능성 있

`https://kr.vuejs.org/v2/guide/computed.html`





$ npm install -g @vue/cli

$ vue create first-vue-cli

얘는 장고랑 달리 -g를 달면 가상환경 만들어주지 않아도 추가 설정이 필요 없다

$ cd first-vue-cli
$ npm run serve



js는 자동으로 일어나는 (python manage.py runserver 같은) 일이 거의 없다

내가 설치해줘야 하는데 그걸 대신해주는게 ^

package.json , bable.config.js

node_modules = venv



vue -> single file component SFC



package.json에서

```
"rules": {
      "no-console": "off"
},
```



src > main.js 이름을 바꿔도 되지만 설정도 바꿔줘야함



data 함수로 쓰면 안되는 이유 

데이터가 같은 배열 객체를 보고 있기 때문에 복사됨(포인팅하기 때문에 참조)



$ vue ui
주피터 같은 거