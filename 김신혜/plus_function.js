// js로 덧셈함수 정의
function 덧셈함수() {
	// 변수 a,b에 id가 inputA,inputB인 요소를 저장
	let a = document.getElementById("inputA").value;
	let b = document.getElementById("inputB").value;
	// id가 valueA,valueB인 요소의 텍스트를 a,b로
	document.getElementById("valueA").innerHTML = a;
	document.getElementById("valueB").innerHTML = b;
	// id가 valueC인 요소의 텍스트를 숫자로 변환한 a + b로
	document.getElementById("valueC").innerHTML = Number(a) + Number(b);
}
