const loader = document.getElementById("loader");
const stamp = document.getElementById("loaderStamp");
const stampText = document.getElementById("loaderStampText");

const observer = new IntersectionObserver((entries) => {

    entries.forEach((entry) => {

        if (entry.isIntersecting) {
            entry.target.classList.add("show");
            observer.unobserve(entry.target);
        }

    });

}, {
    threshold: 0.2
});

function startScrollAnimations() {

    document
        .querySelectorAll(".fade-in-up, .scale-fade-in")
        .forEach(element => observer.observe(element));

}

function openEnvelope() {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "instant"
    });
    loader.classList.add("open");

    setTimeout(() => {
        loader.classList.add("envelope-open");
    }, 2000);

    setTimeout(() => {

        loader.classList.add("finished");
        startScrollAnimations();

    }, 3000);

}
stamp.addEventListener("click", openEnvelope);
stampText.addEventListener("click", openEnvelope);