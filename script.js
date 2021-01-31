var x = window.prompt("Enter number of rows (up to 10): ");
var y = window.prompt("Enter number of columns (up to 10): ");
var lastClicked;
var grid = clickableGrid(x,y,function(el,row,col,i){
    el.className='clicked';
    // if (lastClicked) lastClicked.className='';
    // lastClicked = el;
});

document.body.appendChild(grid);
     
function clickableGrid( rows, cols, callback ){
    var grid = document.createElement('table');
    grid.className = 'grid';
    if (rows <= 10 && cols <= 10){
      for (var r=0;r<rows;++r){
        var tr = grid.appendChild(document.createElement('tr'));
        for (var c=0;c<cols;++c){
            var cell = tr.appendChild(document.createElement('td'));
            cell.addEventListener('click',(function(el,r,c){
                return function(){
                    callback(el,r,c);
                }
            })(cell,r,c),false);
        }
      }
    }
    return grid;
}
