from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def menu():
    return redirect(url_for('home'))

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = "Muh Aizal"
        password = "070203"
        input_username = request.form.get("username")
        input_password = request.form.get("password")

        if input_username == username and input_password == password:
            return redirect(url_for("kereta"))
        else:
            return redirect(url_for("login"))
        
@app.route("/kereta", methods=["GET", "POST"])
def kereta():
    if request.method == "GET":
        return render_template("kereta.html")
    if request.method == "POST":
        tanggal_berangkat = request.form.get("tanggal_berangkat")
        tanggal_tiba = request.form.get("tanggal_tiba")

        data = [
            {"No": 1, "Nama Kereta": "Argo Bromo Anggrek", "Tanggal Berangkat": "2024-07-05", "Tanggal Tiba": "2024-07-06"},
            {"No": 2, "Nama Kereta": "Gajayana", "Tanggal Berangkat": "2024-07-08", "Tanggal Tiba": "2024-07-09"},
            {"No": 3, "Nama Kereta": "Taksaka", "Tanggal Berangkat": "2024-07-06", "Tanggal Tiba": "2024-07-07"}
        ]

        data = [
            kereta for kereta in data
        if kereta["Tanggal Berangkat"] == tanggal_berangkat and kereta["Tanggal Tiba"] == tanggal_tiba] 
        return render_template("kereta.html", data=data)

    return redirect(url_for("pembayaran"))

@app.route("/pembayaran", methods=["POST", "GET"])
def pembayaran():
    if request.method == "GET":
        return render_template("pembayaran.html")
    
    elif request.method == "POST":
        action = request.form.get("action")
        
        if action == "selanjutnya":
            input_nama_kereta = request.form.get("nama_kereta")
            input_stasiun_asal= request.form.get("stasiun_asal")
            input_stasiun_tujuan= request.form.get("stasiun_tujuan")
            input_harga_per_tiket = request.form.get("harga_per_tiket")
            input_jumlahpenumpang = request.form.get("jumlahpenumpang")
            input_metode_pembayaran = request.form.get("metode_pembayaran")

            if input_nama_kereta and input_stasiun_asal and input_stasiun_tujuan and input_harga_per_tiket and input_jumlahpenumpang and input_metode_pembayaran:
                return redirect(url_for("transaksi", 
                                        nama_kereta=input_nama_kereta, 
                                        stasiun_asal=input_stasiun_asal, 
                                        stasiun_tujuan=input_stasiun_tujuan, 
                                        harga_per_tiket=input_harga_per_tiket,
                                        jumlahpenumpang=input_jumlahpenumpang,
                                        metode_pembayaran=input_metode_pembayaran))
        elif action == "batal":
            return redirect(url_for('pembayaran'))
        
@app.route('/transaksi')
def transaksi():
    nama_kereta = request.args.get("nama_kereta")
    stasiun_asal= request.args.get("stasiun_asal")
    stasiun_tujuan= request.args.get("stasiun_tujuan")
    harga_per_tiket = request.args.get("harga_per_tiket")
    jumlahpenumpang = request.args.get("jumlahpenumpang")
    metode_pembayaran = request.args.get("metode_pembayaran")

    return render_template('transaksi.html',nama_kereta=nama_kereta, 
                          stasiun_asal=stasiun_asal, stasiun_tujuan=stasiun_tujuan, 
                         harga_per_tiket=harga_per_tiket,jumlahpenumpang=jumlahpenumpang,
                        metode_pembayaran=metode_pembayaran)