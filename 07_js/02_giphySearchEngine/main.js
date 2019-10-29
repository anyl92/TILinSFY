// 1. input 태그 안의 값(value)을 잡는다.
// const input = document.querySelector('#js-userinput').value;

// 2-1. button 에 'click' 이 일어났을 때, input 에 ENTER 키를 쳤을 때,
// 2-2. 1에서 잡은 값을 요청으로 보낸다(이벤트 리스너를 단다).
// [무엇].addEventListener([언제], [어떻게]]])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const resultArea = document.querySelector('#js-result-area');

const API_KEY = 'G57tMyU5uZ3u7m8txL5oo8LLYL8KufQO';
const testWord = 'cat';
const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${testWord}&limit=5&offset=0&rating=G&lang=ko`;

// const whenPressed = function (event) {
//     console.log('꾸욱');
//     console.log(event);
// }


button.addEventListener('click', () => {
    const inputValue = inputArea.value;
    searchAndPush(inputValue);
});


inputArea.addEventListener('keypress', (event) => {
    // if (event.which === 13) {
    //     const inputValue = inputArea.value
    //     console.log(inputValue));
    // }
    if (event.which === 13) {
        const inputValue = inputArea.value;
        searchAndPush(inputValue);
    }
        // inputValue 로 giphy api 에 요청 보내서 받기
    // console.log('꾸욱');
    // console.log(event.key. event.which);
});


// 3. Giphy API 에서 넘겨준 Data 를 index.html 에서 보여준다.
const searchAndPush = (keyword) => {
    // resultArea.innerHTML = null

    const API_KEY = 'G57tMyU5uZ3u7m8txL5oo8LLYL8KufQO';
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=5&offset=0&rating=G&lang=ko`;

    const AJAX = new XMLHttpRequest();  // 요청 준비
    AJAX.open('GET', url);  // 오청 세팅
    AJAX.send();  // 요청 보내기

    AJAX.addEventListener('load', function (answer) {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        const dataSet = giphyData.data;

        inputArea.value = null;
        resultArea.innerHTML = null;

        for (const data of dataSet) {
            pushToDOM(data.images.downsized.url);
        }
        console.log(giphyData);

        // resultArea.innerHTML += giphyData.data[0].images.downsized.url;
        
    });

    const pushToDOM = (imageUrl) => {
        resultArea.innerHTML += `<img src="${imageUrl}">`;
    }
};



// const pushToDOM = (data) => {
//     resultArea.innerHTML += data;  // 화면에 보여준다.
// };

// const sendAjaxReq = () => {
    
//     // const res = AJAX.res;
//     // const response = AJAX.response;
//     // const giphyData = JSON.parse(response);
//     // console.log(giphyData);
// };