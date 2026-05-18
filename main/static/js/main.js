$(document).ready(function(){
    // Hero Carousel Initialization
    $('.hero-carousel').slick({
        dots: true,
        infinite: true,
        speed: 1000,
        fade: true,
        cssEase: 'cubic-bezier(0.7, 0, 0.3, 1)',
        autoplay: true,
        autoplaySpeed: 5000,
        arrows: false,
        pauseOnHover: false
    });

    // Mobile Menu Toggle
    const mobileMenu = document.getElementById('mobile-menu');
    const navList = document.getElementById('nav-list');

    if(mobileMenu) {
        mobileMenu.addEventListener('click', () => {
            navList.classList.toggle('active');
            // Toggle icon between bars and times
            const icon = mobileMenu.querySelector('i');
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        });
    }

    // Smooth Scroll for Internal Links
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if( target.length ) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 90
            }, 1000);
        }
    });
});



document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.tab-btn');
    const productCards = document.querySelectorAll('.product-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // 1. Update Active Button State
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            // 2. Get Filter Value
            const filterValue = button.getAttribute('data-filter');

            // 3. Filter Products
            productCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');

                if (filterValue === 'all' || filterValue === cardCategory) {
                    // Show item with a smooth fade-in effect
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 10);
                } else {
                    // Hide item
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300); // Matches transition time
                }
            });
        });
    });
});

// Keep your existing Favorite toggle function
function toggleFavorite(btn) {
    const icon = btn.querySelector('i');
    icon.classList.toggle('far');
    icon.classList.toggle('fas');
    // Logic for azamericanestatebuyer.com style UI interactions
}