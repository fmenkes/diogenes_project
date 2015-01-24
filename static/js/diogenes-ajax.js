$(".btn-delete").click(function() {
    if (confirm('Are you sure you want to delete this book?')) {
    var bookid;
    bookid = $(this).attr("data-bookid");
    $.get('/diogenes/delete_book/', {book_id: bookid}, function(){
        $('#diogenes_row_'+bookid).hide();
    });
    } else {

    }
});
$(".btn-edit").click(function() {
    var bookid;
    bookid = $(this).attr("data-bookid");
    $.get('/diogenes/edit_book/', {book_id: bookid});
});