$(document).ready(function(){
   
  //the following 2 variables are using a jQuery 
  //  function to get values from the DOM
  var mark = $('.mark').html();
  var total = $('.total').html();
  var pes = mark/total*100;

  $('.perc').html(pes + '%');

/* The pass mark for provisional driving tests in zimbabwe
   is 88% i.e 22/25.

   So in the following conditional statements, the user
   is told whether he/she passed and the font colors 
   of the marks will be red or green depending on the pass
   mark.
*/

  if(mark < 22){    
     $('.perc').css('color','red');               
     $('.p_f').html("***You Failed***");
  }else{  
        $('.perc').css('color','green');   
        $('.p_f').html("***You Passed***");     
  }





});