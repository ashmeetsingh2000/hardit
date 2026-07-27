document.body.classList.add("no-scroll");
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
        .querySelectorAll(".fade-in-up")
        .forEach(element => observer.observe(element));

}
function animateFirstFlowerGarden() {

    document
        .querySelectorAll("#firstFlowerGarden .scale-fade-in")
        .forEach(el => el.classList.add("show"));

}

const secondFlowerGarden = document.getElementById("secondFlowerGarden");
const observer2 = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animatesecondFlowerGarden();
            observer.unobserve(entry.target); // Run only once
        }
    });
}, {
    root: null,
    rootMargin: "0px 0px -100px 0px",
    threshold: 0
});

observer2.observe(secondFlowerGarden);
function animatesecondFlowerGarden() {

    document
        .querySelectorAll("#secondFlowerGarden .scale-fade-in")
        .forEach(el => el.classList.add("show"));

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
        document.body.classList.remove("no-scroll");

        startScrollAnimations();
        animateFirstFlowerGarden();

    }, 3000);

}
stamp.addEventListener("click", openEnvelope);
stampText.addEventListener("click", openEnvelope);

// ======================================= remove this ===============================================
// startScrollAnimations() 
// ======================================= remove this ===============================================


const targetDate = new Date("November 14, 2026 00:00:00").getTime();

const daysEl = document.getElementById("days");
const hoursEl = document.getElementById("hours");
const minutesEl = document.getElementById("minutes");
const secondsEl = document.getElementById("seconds");

function setValue(element, value){

    if(element.textContent === value) return;

    element.classList.remove("flip");

    void element.offsetWidth;

    element.textContent = value;
    element.classList.add("flip");

}

function updateCountdown(){

    const now = Date.now();
    const distance = targetDate - now;

    if(distance <= 0){

        setValue(daysEl,"00");
        setValue(hoursEl,"00");
        setValue(minutesEl,"00");
        setValue(secondsEl,"00");

        clearInterval(timer);
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((distance / (1000 * 60)) % 60);
    const seconds = Math.floor((distance / 1000) % 60);

    setValue(daysEl, String(days).padStart(2,"0"));
    setValue(hoursEl, String(hours).padStart(2,"0"));
    setValue(minutesEl, String(minutes).padStart(2,"0"));
    setValue(secondsEl, String(seconds).padStart(2,"0"));

}

updateCountdown();

const timer = setInterval(updateCountdown,1000);