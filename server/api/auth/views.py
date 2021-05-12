from api.auth import auth


@auth.route('/',methods=["POST"])
def index():
    print(323442433)
    return "ojbk"