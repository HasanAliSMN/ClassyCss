const rangeSlider = document.getElementById("slider");
const container = document.getElementById("example-cont");

rangeSlider.addEventListener("mousemove", () => {
    console.log(rangeSlider.value);
    container.style.borderRadius = rangeSlider.value + "px";
});

function Append(){

}
function Clear(){
    txt1.value = '';
    for (let i = 1; i <= 7; i++) {
        document.getElementById(`txt${i}`).value = '';
    }
}