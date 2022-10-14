const navSlide = () => {

    const hamburger = document.querySelector('.hamburger');
    const menu = document.querySelector('.menu');
    const menuLinks = document.querySelectorAll('.menu a');

    hamburger.addEventListener('click', function () {
        menu.classList.toggle('menu-active');
        this.classList.toggle('is-active');

        menuLinks.forEach((link, index) => {
        if (link.style.animation){
          link.style.animation =''
        } else {
           link.style.animation = `navlinkfade 0.5s ease forwards ${index/5+0.5}s`;
        }
      });
        hamburger.classList.toggle('toggle')
});


}

navSlide()