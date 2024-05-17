let interval = 1; // Mặc định là 1 phút
let countdownTime = interval * 60; // Thời gian đếm ngược tính bằng giây
let history = [];
let realtimeStarted = false;

document.getElementById("interval").addEventListener("change", function() {
    interval = parseInt(this.value);
    countdownTime = interval * 60;
});

function getRandomNumber() {
    return Math.floor(Math.random() * 10);
}

function getColorAndSize(number) {
    let size = number <= 4 ? "Nhỏ" : "Lớn";
    let color = "";

    if (number === 0 || number === 5) {
        color = "violet";
    } else if (number % 2 === 0) {
        color = "đỏ";
    } else {
        color = "xanh";
    }

    return { size, color };
}

function updateResult() {
    let number = getRandomNumber();
    let { size, color } = getColorAndSize(number);
    
    let sessionElement = document.getElementById("session");
    let session = parseInt(sessionElement.value);

    let resultHTML = document.createElement("div");
    resultHTML.textContent = `Phiên: ${session}, Số: ${number}, Loại: ${size}, Màu: ${color}`;
    resultHTML.className = `result ${size.toLowerCase()} ${color}`;

    // Thêm kết quả vào trong phần tử với ID là "result"
    document.getElementById("result").appendChild(resultHTML);

    // Lưu vào lịch sử
    history.unshift({ session, number, size, color });

    // Tự động tăng số phiên
    sessionElement.value = session + 1;

    // Ẩn hiệu ứng loading
    document.getElementById("loading").style.display = "none";

    // Hiển thị kết quả dưới dạng Swal.fire
    Swal.fire({
        title: 'Kết quả',
        html: resultHTML.outerHTML, // Sử dụng outerHTML để chuyển đổi thành chuỗi HTML
        icon: 'success',
        confirmButtonText: 'OK'
    }).then(() => {
        // Gọi lại hàm updateResult() để dự đoán phiên tiếp theo
        realtimeStarted = false; // Reset trạng thái để có thể bắt đầu lại
    });
}

function toggleHistory() {
    let historyElement = document.getElementById("history");
    if (historyElement.style.display === "block") {
        historyElement.style.display = "none";
    } else {
        historyElement.style.display = "block";
        renderHistory();
    }
}

function renderHistory() {
    let historyElement = document.getElementById("history");
    historyElement.innerHTML = "";
    history.forEach(entry => {
        let entryElement = document.createElement("div");
        entryElement.textContent = `Phiên: ${entry.session}, Số: ${entry.number}, Loại: ${entry.size}, Màu: ${entry.color}`;
        entryElement.className = `history-entry ${entry.size.toLowerCase()} ${entry.color}`;
        historyElement.appendChild(entryElement);
    });
}

function updateClock() {
    let now = new Date();
    let hours = String(now.getHours()).padStart(2, '0');
    let minutes = String(now.getMinutes()).padStart(2, '0');
    let seconds = String(now.getSeconds()).padStart(2, '0');

    document.getElementById("clock").textContent = `Thời gian thực: ${hours}:${minutes}:${seconds}`;
}

function updateCountdown() {
    let now = new Date();
    let seconds = now.getSeconds();
    let countdown = 60 - seconds;

    document.getElementById("countdown").textContent = `Đếm ngược: --:${countdown < 10 ? '0' : ''}${countdown}`;
}

setInterval(function() {
    updateClock();
    updateCountdown();
    let now = new Date();
    if (now.getSeconds() === 5 && !realtimeStarted) {
        realtimeStarted = true; // Đặt trạng thái để ngăn chặn nhiều lần chạy đồng thời
        document.getElementById("loading").style.display = "block";
        setTimeout(updateResult, 1000); // Giả lập hiệu ứng loading trong 1 giây
    }
}, 1000);
