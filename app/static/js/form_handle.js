$(function() {
    // populate ddl car
    var car_ddl = $('#car');
    var model_ddl =  $('#model');
    var car_id;

    car_ddl.empty();
    car_ddl.append('<option value="">--choose cars--</option>');
    car_ddl.prop('selectIndex', 0)
    
    $.ajax({
        type: 'GET',
        url: $SCRIPT_ROOT + '/_load_cars',
        success: (results) => {
            if (results.status) {
                $.each(results.data, (i, item) => {
                    car_ddl.append($('<option></option>').attr('value', item.id).text(item.name));
                });
            }
        }
    });

    // change ddl car effect to populate ddl model 
    car_ddl.bind('change', function() {
        car_id = $(this).children('option:selected').val();
        populate_model(car_id);
    });

    // change ddl model effect to populate ddl version
    model_ddl.bind('change', function() {
        model_id = $(this).children('option:selected').val();
        populate_version(model_id);
    });
});

function populate_model(car_id) {
    var model_ddl = $('#model');
    model_ddl.empty();
    model_ddl.append('<option value="">--choose model--</option>')
    $.ajax({
        type: 'GET',
        url: $SCRIPT_ROOT + '/_load_models',
        data: {
            'car_id': car_id
        },
        success: (results) => {
            if (results.status) {
                $.each(results.data, (i, item) => {
                    model_ddl.append($('<option></option>').attr('value', item.id).text(item.model));
                });
            }
            // repopulate version to default index when ddl car get change
            populate_version(model_ddl.val())
        }
    });
}

function populate_version(model_id) {
    var version_ddl = $('#version');
    version_ddl.empty();
    version_ddl.append('<option value="">--choose version--</option>')
    $.ajax({
        type: 'GET',
        url: $SCRIPT_ROOT + '/_load_versions',
        data: {
            model_id: model_id
        },
        success: (results) => {
            if (results.status) {
                $.each(results.data, (i, item) => {
                    version_ddl.append($('<option></option>').attr('value', item.id).text(item.version));
                });
            }
        }
    });
}
