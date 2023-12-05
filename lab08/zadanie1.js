function funkcja_zwrotna(){
    let form = document.forms.item("formularztypy");
    let pole_tekstowe = form.elements.namedItem("pole_tekstowe");
    let pole_liczbowe = form.elements.namedItem("pole_liczbowe");
    console.log(pole_liczbowe.value + ':' + typeof pole_liczbowe.value);
    console.log(pole_tekstowe.value + ':' + typeof pole_tekstowe.value);
}

//window.prompt("Tekst1","Tekst2");

for(let i=0; i<4; i++){
    //let x = window.prompt();
    console.log(x + ":" + typeof x);
}

function sum_strings(arr) {
    return arr.reduce((sum, str) => {
        const num = parseInt(str, 10);
        if (!isNaN(num)) {
            return sum + num;
        }
        return sum;
    }, 0);
}