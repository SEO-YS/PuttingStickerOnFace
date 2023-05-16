const btn = document.querySelector(".loginBtn");
btn.addEventListener("click",function(e){
    const inputId = document.querySelector('.id').value;
    const inputPw = document.querySelector('.pwd').value;
    if(inputId.includes('@') && inputPw.length > 4){
        document.querySelector(".loginBtn").style.background = "rgb(46, 184, 223)";
    }else{
        alert("아이디나 비밀번호가 틀렸습니다!");
        document.querySelector(".loginBtn").style.background= "default";
    }
    return false; //경고창이 뜨면 넘어가지 않도록 설정
});
