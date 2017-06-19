$(document).on('change', ':file', function() {
    var input = $(this),
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.siblings('span').text(label);
});


$(document).ready(function(){
      var i=1;
     $("#add_row").click(function(){
         addTableRow();

     });

  function addTableRow(){
            $('#field'+i).html(
                "<td><input  name='name"+i+"' type='text' placeholder='Field name'  class='form-input'></td>" +
                "<td><input  name='type"+i+"' type='text' placeholder='Field type'  class='form-input'></td>"+
                "<td class='td-last'><a class='button button-green delete-row'>Delete</a></td>"
            );
            $('#tab_logic').append('<tr id="field'+(i+1)+'"></tr>');
            deleteTableRow();
          i++;
  }

  function deleteTableRow(){
        $('.delete-row').click(function () {
            $(this).closest('tr').remove();
        });
  }

});