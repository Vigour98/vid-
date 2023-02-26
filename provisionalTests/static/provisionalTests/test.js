$(document).ready(function(){
   
    questions = $('.single_question');       

    /* This {{for}} loop is appending the rounded div elements 
     * into the .prog div. The rounded div elements will be 
     * used as shortcuts to a specific question
     */
    for(i=0; i<questions.length; i++){
        j = i + 1;
        $('.prog').append('<div class="round">'+j+'</div>');
    }
     
    // caching all the rounded DIVs
    round = $('.round');

    /* This is used to view the selected question
     * and remove the current question on the screen
     */
    $(document).on('click', '.round', function(){
       $('.round').css('transform','scale(1)');                         
       $(this).css('transform','scale(1.5)'); 

        $('.single_question').hide();
        num = $(this).html();
        $(questions[num-1]).show();

    });
    
    /* initially all the questions are hidden so
     * the following line of code makes the first 
     * question to be visible
     */    
    $(questions[0]).show();   

    /* When the user select an answer the available question
       will dissaper and the next question will appera  */
    $(document).on('click', '.radio', function(){ 
        num = $(this).parent().parent().index(); //to get the index of the question         
        $('.round').css('transform','scale(1)');                         
        
        //to change the css for the rounded div elements
        $(round[num-2]).css({'color':'black',
                             'background':'red',
                             'box-shadow':'2px 2px 2px black',
                             'font-weight':'bold'
                            
                            });
        $(round[num-1]).css('transform','scale(1.5)');                    
        
        var next = $(this).parent().parent().next().html();
        if (next != ""){       
        $(this).parent().parent().hide();
        $(this).parent().parent().next().show();
        }
    });

    /* when user clicks the forward arrow, the next question 
       will appear */ 
    $(document).on('click', '.next', function(){
        event.preventDefault();       
        var next = $(this).parent().parent().next().html();
        var num = $(this).parent().parent().index();
        if(next != ""){
            $('.round').css('transform','scale(1)');    
            $(round[num-1]).css('transform','scale(1.5)');    
            $(this).parent().parent().hide();
            $(this).parent().parent().next().show();
        }
    });

    /* when user clicks the back arrow, the previous question 
       will appear */ 
    $(document).on('click', '.prev', function(){
       event.preventDefault();
       var prev = $(this).parent().parent().prev().html(); 
       var num = $(this).parent().parent().index();
        if (prev != ""){
            $('.round').css('transform','scale(1)'); 
            $(round[num-3]).css('transform','scale(1.5)'); 
            $(this).parent().parent().hide();
            $(this).parent().parent().prev().show();            
        }       
    });
    
});