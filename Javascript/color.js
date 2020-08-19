function changeColor() {
    var table = document.getElementById('table'),
        cells = table.getElementsByTagName('td');

    for (var i = 0, len = cells.length; i < len; i++) {
        // cells[i].onclick = function(){

        var number = this.innerHTML;

        if (number == 0) {
            this.innerHTML = '<span style="color:#FF0000"> 0 </span>'
            // number.innerHTML.replace('<span style="color: red;">0</span>');
        }
        if (number == 1) {
            this.innerHTML = '<span style="color: blue"> 1 </span>'
            // number.innerHTML.replace('<span style="color: red;">0</span>');
        }
        if (number == 2) {
            this.innerHTML = '<span style="color: yellow"> 2 </span>'
            // number.innerHTML.replace('<span style="color: red;">0</span>');
        }
        if (number == 3) {
            this.innerHTML = '<span style="color: green"> 3 </span>'
            // number.innerHTML.replace('<span style="color: red;">0</span>');
        }
        console.log(this.innerHTML);
        /* if you know it's going to be numeric:
        console.log(parseInt(this.innerHTML),10);
        */
        // }
    }
}