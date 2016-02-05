# fortune-cowsay
fortune + cowsay + python + bottle + gunicorn + nginx = "fortune | cowsay" in-the-browser. Because.

## Installation
1. Ensure you have both 'fortune' and 'cowsay' installed
2. Clone this responsitory
3. Copy config files into nginx and /etc/init/ (modified accordingly) (your milege may vary according to system)
4. Start gunicorn: `sudo initctl start fortune-cow`
5. Restart nginx: `sudo service nginx restart`
6. Question things
