var delivery = document.getElementById("delivery");
var direct = document.getElementById("direct");
var options = document.getElementsByClassName("appForm--list");

var deliveryFunction = function (event) {
  var deliveryDest = document.createElement("input");
  deliveryDest.placeholder = "주소를 정확히 입력해주세요.";
  deliveryDest.className = "deliveryDest";
  if (deliveryDest === null) {
    console.log(deliveryDest);
    return;
  } else {
    if (document.getElementsByClassName("deliveryDest").length >= 1) {
      return;
    }
    options[3].appendChild(deliveryDest);
  }
};
delivery.addEventListener("click", deliveryFunction, false);

var directFunction = function (event) {
  var checkElement = document.getElementsByClassName("deliveryDest");
  if (checkElement.length === 0) {
    return;
  } else {
    var delElement = document.getElementsByClassName("appForm--list");
    delElement[3].removeChild(delElement[3].lastChild);
  }
};

direct.addEventListener("click", directFunction);
