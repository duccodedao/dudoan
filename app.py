<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dự đoán số ngẫu nhiên</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, #ece9e6, #ffffff);
            color: #333;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            color: #4CAF50;
            margin-bottom: 20px;
        }
        #clock, #countdown {
            font-size: 1.5em;
            margin: 10px 0;
            padding: 10px 20px;
            border-radius: 5px;
            background: #f0f0f0;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .time-select, .session-input {
            margin: 20px 0;
        }
        .time-select label, .session-input label {
            font-size: 1.2em;
            margin-right: 10px;
        }
        .time-select select, .session-input input {
            padding: 10px;
            font-size: 1em;
            border-radius: 5px;
            border: 1px solid #ccc;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .result {
            font-size: 2em;
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ccc;
            width: 60%;
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .nhỏ, .lớn {
            color: black;
        }
        .đỏ {
            color: red;
        }
        .xanh {
            color: green;
        }
        .violet {
            color: violet;
        }
    </style>
</head>
<body>
    <h1>Dự đoán số ngẫu nhiên</h1>
    <p id="clock">Thời gian thực: --:--:--</p>
    <div class="time-select">
        <label for="interval">Chọn thời gian dự đoán: </label>
        <select id="interval">
            <option value="1">1 phút</option>
            <option value="3">3 phút</option>
            <option value="5">5 phút</option>
            <option value="10">10 phút</option>
        </select>
    </div>
    <p id="countdown">Đếm ngược: --:--</p>
    <div class="session-input">
        <label for="session">Nhập số phiên: </label>
        <input type="number" id="session" value="2223" min="0">
    </div>
    <p class="result" id="result">Chờ kết quả...</p>

    <script>
        let interval = 1; // Mặc định là 1 phút
        let countdownTime = interval * 60; // Thời gian đếm ngược tính bằng giây

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
            
            let resultElement = document.getElementById("result");
            let sessionElement = document.getElementById("session");
            let session = parseInt(sessionElement.value);

            resultElement.textContent = `Phiên: ${session}, Số: ${number}, Loại: ${size}, Màu: ${color}`;
            resultElement.className = `result ${size.toLowerCase()} ${color}`;

            // Tự động tăng số phiên
            sessionElement.value = session + 1;
        }

        function updateClock() {
            let now = new Date();
            let hours = String(now.getHours()).padStart(2, '0');
            let minutes = String(now.getMinutes()).padStart(2, '0');
            let seconds = String(now.getSeconds()).padStart(2, '0');

            document.getElementById("clock").textContent = `Thời gian thực: ${hours}:${minutes}:${seconds}`;
        }

        function updateCountdown() {
            if (countdownTime > 0) {
                countdownTime--;
                let minutes = String(Math.floor(countdownTime / 60)).padStart(2, '0');
                let seconds = String(countdownTime % 60).padStart(2, '0');
                document.getElementById("countdown").textContent = `Đếm ngược: ${minutes}:${seconds}`;
            } else {
                updateResult();
                countdownTime = interval * 60; // Reset thời gian đếm ngược
            }
        }

        setInterval(function() {
            updateClock();
            updateCountdown();
        }, 1000);
    </script>
</body>
</html>
