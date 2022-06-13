document.getElementById('tt').onclick = function(){
    var checkboxes=document.getElementsByName('de');
    for(var checkbox of checkboxes){
        checkbox.checked=this.checked
    }
}