$(function() {
    // populate ddl car
    var car_ddl = $('#car');
    var car_id;
    car_ddl.empty()
    car_ddl.append('<option value="">--choose cars--</option>');
    car_ddl.prop('selectIndex', 0)
    $.ajax({
        type: 'GET',
        url: $SCRIPT_ROOT + '/_load_cars',
        success: (results) => {
            $.each(results.data, (i, item) => {
                car_ddl.append($('<option></option>').attr('value', item.id).text(item.name));
            });
        }
    });

    // change ddl car effect to populate ddl model 
    car_ddl.bind('change', function() {
        car_id = $(this).children("option:selected").val();
        populate_model(car_id);
    });
});

function populate_model(car_id) {
    var model_ddl = $('#model')
    model_ddl.empty()
    model_ddl.append('<option value="">--choose model--</option>')
    $.ajax({
        type: 'GET',
        url: $SCRIPT_ROOT + '_load_models',
        data: {
            'car_id': car_id
        },
        success: (results) => {
            $.each(results.data, (i, item) => {
                model_ddl.append($('<option></option>').attr('value', item.id).text(item.model))
            });
        }
    });
}
