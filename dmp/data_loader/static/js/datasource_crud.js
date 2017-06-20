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

  function createRow(){
      var field_name_elem = $('input[name=field_name0]').clone();
      var field_type_elem =$('select[name=field_type0]').clone();
      field_name_elem.attr('name', 'field_name'+i);
      field_name_elem.attr('id', 'id_field_name'+i);
      field_name_elem.val('');
      field_type_elem.attr('name','field_type'+i );
      field_type_elem.attr('id', 'id_field_type'+i);
      var outer_html = $('#field'+i).html($('<td></td>').append(field_name_elem));
      outer_html.append($('<td></td>').append(field_type_elem));
      outer_html.append("<td class='td-last'><a class='button button-green delete-row'>Delete</a></td>");
      return outer_html;
  }

  function addTableRow(){
            createRow();
            // $('#field'+i).html(createRow());
            $('#tab_logic').append('<tr id="field'+(i+1)+'"></tr>');
            initializeDeleteTableRow();
          i++;
  }

  function initializeDeleteTableRow(){
        $('.delete-row').click(function () {
            $(this).closest('tr').remove();
        });
  }

});