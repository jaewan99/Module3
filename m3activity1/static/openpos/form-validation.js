$(document).ready(function () {
  var map = new Map();

  // button to delete an item from the existing stuffs

  $(document).on("click", ".delItemBtn", function () {
    var amt = $(this).parent().parent().find(".totalDelAmount").html();
    prc_amt = amt.split(" ");
    delAmount = prc_amt[2];

    // subtract from the total amount
    var tamt = parseFloat($("#totamt").html());
    tamt = tamt - delAmount;
    $("#totamt").html(tamt.toFixed(2));

    // remove the whole element
    this.parentElement.parentElement.parentElement.remove();
  });

  $(".itembut").click(function () {
    var amt = $(this).parent().parent().find(".lineamount").val();
    var nme = $(this).parent().parent().find(".iname").html();
    var nmeid = $(this).parent().parent().find(".nmeid").val();
    var prc = $(this).parent().parent().find(".iprice").html();
    var quan = $(this).parent().parent().find(".iquantity").html();
    var tamt = parseFloat($("#totamt").html());
    prc_amt = prc.split(" ");

    // stop the function when there's no amt
    if (amt == 0) {
      return false;
    }
    // remove the exisiting 'stuff' of an item, if there is
    var element = document.getElementById(nmeid);
    if (element != null) {
      // subtract the value to the total
      let minusVal =
        parseInt(document.getElementById("#" + nmeid).value) * prc_amt[1];
      tamt = tamt - minusVal;
      // remove the existing 'stuff'
      document
        .getElementById(nmeid)
        .parentElement.parentElement.parentElement.remove();
    }

    lt = parseFloat(prc_amt[1]) * parseFloat(amt);
    tamt = tamt + lt;
    $("#totamt").html(tamt.toFixed(2));
    stuff = " ";
    stuff =
      stuff +
      '<li class="list-group-item d-flex justify-content-between lh-sm">';
    stuff = stuff + "<div>";

    stuff = stuff + '<h6 class="my-0 idnme">' + nme + "</h6>";
    stuff =
      stuff + '<p style ="font-size: 12px">' + "ID Number: " + nmeid + "</p>";
    stuff =
      stuff +
      '<small class="text-muted">' +
      prc_amt[1] +
      ' x <span class="idamt" id= "' +
      nmeid +
      '">' +
      amt +
      "</span></small>";
    stuff = stuff + "</div>";
    stuff =
      stuff +
      '<input type="hidden" id= "#' +
      nmeid +
      '" value = "' +
      amt +
      '" >';

    //  addede a delete button
    stuff = stuff + "<div>";
    stuff =
      stuff +
      '<p class="text-muted totalDelAmount"> PHP ' +
      lt.toFixed(2) +
      "</p>";
    stuff = stuff + "<div class ='d-flex align-items-end justify-content-end'>";
    stuff =
      stuff +
      '<button class="btn btn-danger btn-sm h-50 delItemBtn">X' +
      "</button>";
    stuff = stuff + "</div>";
    stuff = stuff + "</div>";
    // end
    stuff =
      stuff +
      '<input type="hidden" class="nmeid-ord" id= "' +
      nmeid +
      '" value = "' +
      nmeid +
      '" >';

    stuff = stuff + "</li>";

    $("#ord").append(stuff);
    $(this).parent().parent().find(".lineamount").val(0);
    event.preventDefault();
  });

  $("#cls").click(function () {
    if ($("#totamt").html() == 0) {
      alert("Please add an item to the order");
      return false;
    }
    $("#ord li").each(function (i) {
      var idnme = $(this).find(".idnme").html();
      var idamt = $(this).find(".idamt").html();
      var idid = $(this).find(".nmeid-ord").val();
      var comb = idid + ":" + idamt;
      $("#complete_order").val($("#complete_order").val() + comb + "-");
    });
    $("#total_amount").val($("#totamt").html());
  });
});
function checkInputValue(input) {
  // Get the maximum allowed value from the 'max' attribute of the input
  var maxAllowed = parseInt(input.getAttribute("max"));

  // Get the current value of the input
  var currentValue = parseInt(input.value);

  // If the current value is greater than the maximum allowed
  if (currentValue > maxAllowed) {
    // Set the value of the input to the maximum allowed
    input.value = maxAllowed;
  }
  if (currentValue < 1) {
    input.value = 0;
  }
}
