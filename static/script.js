// VinIA Cinema — anima as cortinas, texto, pipoca
(function () {
    const curtainL = document.getElementById("curtainLeft");
    const curtainR = document.getElementById("curtainRight");
    const title = document.getElementById("title");
    const name = document.getElementById("name");
    const subtitle = document.getElementById("subtitle");
    const replay = document.getElementById("replay");
    const popcornBox = document.getElementById("popcorn");

    function play() {
        // Reset
        [title, name, subtitle, replay].forEach(el => el.classList.remove("show"));
        curtainL.classList.remove("open");
        curtainR.classList.remove("open");
        popcornBox.innerHTML = "";

        // Sequência:
        // 0.0s — cortinas abrem
        // 1.6s — título aparece
        // 2.0s — nome aparece (com delay interno)
        // 2.8s — subtítulo
        // 3.2s — pipoca começa a cair
        // 3.6s — botão replay

        setTimeout(() => {
            curtainL.classList.add("open");
            curtainR.classList.add("open");
        }, 200);

        setTimeout(() => title.classList.add("show"), 1800);
        setTimeout(() => name.classList.add("show"), 2200);
        setTimeout(() => subtitle.classList.add("show"), 3000);
        setTimeout(() => startPopcorn(), 3200);
        setTimeout(() => replay.classList.add("show"), 3600);
    }

    function startPopcorn() {
        const COUNT = 60;
        for (let i = 0; i < COUNT; i++) {
            setTimeout(() => spawnKernel(), i * 90);
        }
    }

    function spawnKernel() {
        const el = document.createElement("div");
        el.className = "kernel";
        const x = Math.random() * 100;
        const drift = (Math.random() - 0.5) * 200;
        const duration = 2.5 + Math.random() * 1.5;
        const size = 4 + Math.random() * 8;
        el.style.left = `${x}vw`;
        el.style.top = `-10px`;
        el.style.width = `${size}px`;
        el.style.height = `${size}px`;
        el.style.setProperty("--drift", `${drift}px`);
        el.style.animationDuration = `${duration}s`;
        popcornBox.appendChild(el);
        setTimeout(() => el.remove(), (duration + 0.2) * 1000);
    }

    replay.addEventListener("click", play);

    // Auto-start on load
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", play);
    } else {
        play();
    }
})();