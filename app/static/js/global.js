// Utils for DDL
$(function() {
    var DDL_Utils = {};

    DDL_Utils.populates = function(DDL) {
        DDL.empty();
        DDL.append('<option value="">--choose--</option>')
        $.ajax({
            type: 'GET',
            url: $SCRIPT_ROOT + '/_load_' + DDL.attr('name') + 's',
            success: (results) => {
                if (results.success) {
                    $.each(results.data, (i, item) => {
                        var n = item[DDL.attr('name')];
                        DDL.append($('<option></option>').attr('value', item.id).text(n));
                    });
                }
            }
        });
    };

    DDL_Utils.populate_by = function(DDL, id) {
        DDL.empty();
        DDL.append('<option value="">--choose--</option>');
        $.ajax({
            type: 'GET',
            url: $SCRIPT_ROOT + '/_load_' + DDL.attr('name') + 's',
            data: {
                'id': id
            },
            success: (results) => {
                if (results.success) {
                    $.each(results.data, (i, item) => {
                        var n = item[DDL.attr('name')];
                        DDL.append($('<option></option>').attr('value', item.id).text(n));
                    });
                }
            }
        });
    };

    window.DDL_Utils = window.$WS = DDL_Utils;
    
    return;
});
