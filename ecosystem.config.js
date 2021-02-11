module.exports = {
  apps: [
    {
      name: "weather",
      script: "./src/weather.py",
      args: [],
      env: {
          SERVER_URL: "http://philliplogan.com:3040",
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
