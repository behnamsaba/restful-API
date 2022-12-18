from flask import Flask, render_template,request,redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db, Cupcake

app=Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'project'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
toolbar = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route("/api/cupcakes")
def all_json():
    cupcakes=[cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes/<int:id>")
def selected_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes",methods=["POST"])
def new_cupcake():

    try:
        new_cupcake=Cupcake(flavor=request.json['flavor'],size=request.json["size"],rating=request.json["rating"],image=request.json["image"])
    except:
        new_cupcake=Cupcake(flavor=request.json['flavor'],size=request.json["size"],rating=request.json["rating"])

    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json,201)


@app.route('/api/cupcakes/<int:id>',methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor=request.json.get("flavor",cupcake.flavor)
    cupcake.size=request.json.get("size",cupcake.size)
    cupcake.rating=request.json.get("rating",cupcake.rating)
    cupcake.image=request.json.get("image",cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())
    
@app.route("/api/cupcakes/<int:id>",methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")

@app.route("/")
def cupcake_frontend():
    return render_template("cupcake.html")