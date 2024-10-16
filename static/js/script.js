function posting() {
    let name = $("#name").val();
    let email = $("#email").val();
    let message = $("#message").val();

    if (!message) {
        alert("Please fill your message :)");
        return;
    }

    $.ajax({
      type: "POST",
      url: "/message",
      data: {
        name_give: name,
        email_give: email,
        message_give: message,
      },
      success: function (response) {
        alert(response["msg"]);
        window.location.reload();
      },
    })
}

function reset() {
    $("#name").val("");
    $("#email").val("");
    $("#message").val("");
}