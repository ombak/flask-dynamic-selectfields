// Utils for DDL
$(function() {
    var DDL_Utils = {};    

    DDL_Utils.fade_out = function (_element) {
        _element.children('div').slideUp();
        setTimeout(function() {
            _element.children('div').remove();
            return;
        }, 500);
        return;
    };

    DDL_Utils.bindAction = function() {
        $('.notification > a').click(function() {
            $WS.fadeOut();
            return;
        });
    };

    DDL_Utils.fadeOut = function () {
        setTimeout(function () {
            $WS.fade_out($('.flash-messages-container'));
            return;
        }, 2500);
        return;
    };

    DDL_Utils.flash_message = function (message, category) {
        var _html = $('<div class="notification is-'+ category +'">'+ message +'</div>');
        var _clear_html = $('<div style="clear:both;"></div>');
        var _button = $('<a href="javascript:void(0)" class="delete"></a>');
        $('.flash-messages-container').append(_html);
        $('.flash-messages-container').children().append(_button);
        $('.flash-messages-container').append(_clear_html);
        $WS.bindAction();
        $WS.fadeOut();
        return;
    };

    DDL_Utils.populates = function(DDL) {
        DDL.empty();
        DDL.append('<option value="">--choose--</option>')
        $.ajax({
            type: 'GET',
            url: $SCRIPT_ROOT + '/_load_' + DDL.attr('name') + 's',
            beforeSend: function() {
                DDL.parent().addClass('is-loading');
            },
            success: (results) => {
                if (results.success) {
                    $.each(results.data, (i, item) => {
                        var n = item[DDL.attr('name')];
                        DDL.append($('<option></option>').attr('value', item.id).text(n));
                    });
                }
            },
            complete: function() {
                DDL.parent().removeClass('is-loading');
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
            beforeSend: function() {
                DDL.parent().addClass('is-loading');
            },
            success: (results) => {
                if (results.success) {
                    $.each(results.data, (i, item) => {
                        var n = item[DDL.attr('name')];
                        DDL.append($('<option></option>').attr('value', item.id).text(n));
                    });
                }
            },
            complete: function() {
                DDL.parent().removeClass('is-loading');
            }
        });
    };

    DDL_Utils.ajax_form = function(form) {
        form.submit(function(e) {
            $.ajax({
                url: $SCRIPT_ROOT + '/' + form.attr('action'),
                data: form.serialize(),
                type: 'POST',
                dataType: 'json',
                beforeSend: function() {
                    $('#btn-save').addClass('is-loading');
                },
                success: function(results) {
                    if (results.success) {
                        if (results.messages) {
                            $WS.flash_message(results.messages, 'primary');
                        }

                        if (results.next) {
                            setTimeout(function() {
                                document.location = results.next;
                            }, 2000);
                        }
                    }
                },
                complete: function() {
                    $('#btn-save').removeClass('is-loading');
                }
            });
            e.preventDefault()
        });
    };

    window.DDL_Utils = window.$WS = DDL_Utils;
    
    $WS.bindAction();
    $WS.fadeOut();

    return;
});
