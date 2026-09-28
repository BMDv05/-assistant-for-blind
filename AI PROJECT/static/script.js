const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");

startBtn.addEventListener("click", () => {
    fetch("/start", { method: "POST" })
    .then(response => response.json())
    .then(data => alert("النظام " + data.status));
});

stopBtn.addEventListener("click", () => {
    fetch("/stop", { method: "POST" })
    .then(response => response.json())
    .then(data => alert("النظام " + data.status));
});

// تحديث القوائم كل 5 ثواني
setInterval(() => {
    fetch("/api/scenes")
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("scenesList");
            list.innerHTML = "";
            data.forEach(item => {
                const li = document.createElement("li");
                li.textContent = `${item.time} - ${item.scene}`;
                list.appendChild(li);
            });
        });

    fetch("/api/warnings")
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("warningsList");
            list.innerHTML = "";
            data.forEach(item => {
                const li = document.createElement("li");
                li.textContent = `${item.time} - ${item.warning}`;
                list.appendChild(li);
            });
        });
}, 5000);
