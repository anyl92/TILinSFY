### CSS

(0, 1, 0) >우선순위가 더 높음  (0, 0, 1)   *순차적인 순서가 아님

!important > inline css > [#id > .class] > tag > * > browser기본세팅

* !important는 웬만하면 쓰지 말 것
* id / class 는 selecting을 위한 존재 . class가 가장 많이 쓰임 그다음 tag



우선순위가 같으면 순차적으로 진행?



p:first-child {}    - 핵심은 p, 그러나 첫째인 p/ 첫번째 자식인데 까고보니 p

p:last-child P{}   - 마지막 자식인데 까고보니 p

p:nth-child(2) {}   - 부모는 모르겠고 어쨌든 2번째 p

