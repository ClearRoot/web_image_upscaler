// image type check
var validateType = function (img) {
    return (['image/jpeg', 'image/jpg', 'image/png'].indexOf(img.type) > -1);
}

// image thumbnail
document.getElementById('imageSelector').addEventListener('change', function (e) {

    let elem = e.target;

    if (validateType(elem.files[0])) {
        let preview = document.querySelector('#thumb');
        preview.src = URL.createObjectURL(elem.files[0]);
        document.querySelector('#submit-div').style.display = 'block';
        preview.style.display = 'inline';
        preview.style.width = '15rem';
        preview.style.height = '15rem';
        preview.onload = function () {
            URL.revokeObjectURL(preview.src);
        }
    } else {
        let preview = document.querySelector('#thumb');
        preview.style.display = 'none';
        document.querySelector('#submit-div').style.display = 'none';
        console.log('이미지 파일이 아닙니다.');
    }
});

// submit
document.getElementById('submit-btn').addEventListener('click', function (e) {
    let elem = e.target;
    let submitDiv = document.querySelector('#submit-div');
    
    let spinnerSpan = document.createElement("span");
    spinnerSpan.className = 'visually-hidden';
    spinnerSpan.textContent = 'Loading...';
    
    let spinnerDiv = document.createElement("div");
    spinnerDiv.className = 'spinner-border';
    spinnerDiv.style.width = '3rem'
    spinnerDiv.style.height = '3rem'
    spinnerDiv.setAttribute('role', 'status');
    spinnerDiv.append(spinnerSpan);

    elem.style.display = 'none'
    submitDiv.append(spinnerDiv)
});