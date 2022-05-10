function scoring(e) {
  star = document.getElementsByTagName("i");
  var loop = 0;
  if (e.classList.contains("score10")) {
    loop = 1;
  } else if (e.classList.contains("score8")) {
    loop = 2;
  } else if (e.classList.contains("score6")) {
    loop = 3;
  } else if (e.classList.contains("score4")) {
    loop = 4;
  } else if (e.classList.contains("score2")) {
    loop = 5;
  }

  for (var i = 0; i < loop; i++) {
    star[i].classList.remove("far");
    star[i].classList.add("fas");
  }
  console.log(loop);
  for (var i = loop; i < 5; i++) {
    if (star[i].classList.contains("fas")) {
      star[i].classList.remove("fas");
      star[i].classList.add("far");
    } else {
      return;
    }
  }
}
