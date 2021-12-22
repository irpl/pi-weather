module.exports = {
  apps: [
    {
      name: "weather",
      script: "./src/weather.py",
      args: [],
      env: {
          SERVER_URL: "http://192.168.100.222:3040/data",
      },
      exec_mode: "fork",
      instances: "1",
      wait_ready: true,
      autorestart: false,
      max_restarts: 5,
      interpreter: "./.venv/bin/python3.9"
    }
  ]
}
