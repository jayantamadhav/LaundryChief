$(document).ready(function () {
    if( $("#customerSearch").val() == ""){
        $("#customer").text("Customer not selected!");
    }
    else{
        $("#customer").text("Customer : " + $("#customerSearch").val());
    }
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');
    });

    var availableCustomers = []
    availableCustomers = [
    {% for customer in customers %}
    "{{ customer }}",
    {% endfor %}
    ];
    $( "#customerSearch" ).autocomplete({
        source: availableCustomers,
        response: function(event, ui) {
                    // ui.content is the array that's about to be sent to the response callback.
                    if (ui.content.length === 0) {
                        $("#empty-message").text("No results found, Try adding new Customer");
                    } 
                    else {
                        $("#empty-message").empty();
                    }
                },
                select: function(event, ui) {
                    $("#selectedCustomer").text("Customer : " + ui.item.value);   
                }
            });
    $( "#addCustomer").on('click', function(){
        var name = $( "#cust_name" ).val();
        $( "#customerSearch" ).val(name);
    });
    $('.table > tbody > tr > td > button').click(function(){
        var status = $(this).attr("id");
        var id = $(this).attr("data-catid"); 
        $.ajax({
            type:"POST",
            async: "true",
            cache:"false",
            url: "orderStatus",
            data:{ status: status, id: id },
            success: function(data) {
                if(status == "orderProcessing"){
                    $('.'+id).fadeOut("slow");
                    $(".ready_tbody").prepend("<tr class=\"" + data.id + "\"><th scope=\"row\">" + data.id + "</th><td>" + data.customer_name + "</td><td>"+ data.status +"</td><td><button type=\"button\" id=\"orderCleaned\" class=\"btn btn-info btn-lg\" data-catid=\"" + data.id + "\" style=\"font-size: 0.8em;padding:5px\">Paid ?</button></td></tr>");
                    location.reload();
                }
                else{
                    $('.'+id).fadeOut("slow");
                }
            },
            error: function(){
                alert("Nope");
            }
        });
    });
    $('#smartcart').smartCart();
    $('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
        localStorage.setItem('activeTab', $(e.target).attr('href'));
    });
    var activeTab = localStorage.getItem('activeTab');
    if(activeTab){
        $('#myTab a[href="' + activeTab + '"]').tab('show');
    }
});