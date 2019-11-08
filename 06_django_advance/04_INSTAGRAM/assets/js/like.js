// console.log('Working');
const likeButtons = document.querySelectorAll('.js-like-button');

likeButtons.forEach((likeButton) => {
    likeButton.addEventListener('click', function(event) {
        const URL = `/insta/${event.target.dataset.id}/like/`;
        
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';

        axios.post(URL)
            .then(res => {
                if (res.data.liked) {  // 지금 좋아요 함
                    event.target.classList.remove('far');
                    event.target.classList.add('fas');
                }
                else {  // 지금 좋아요 해제
                    event.target.classList.remove('fas');
                    event.target.classList.add('far');
                }
            });
    })
})
