import jwt
import base64

def fix(src):
    rem = len(src) % 4
    print(len(src), rem)
    return src + b'=' * rem

def cesi():
    jwt_token = jwt.encode({"name": "renlei", "age": 20}, 'abcd')
    header, pld, sig = jwt_token.split(b'.')
    print(header)
    print(pld)
    print(sig)
    print(base64.urlsafe_b64decode(header))
    f_pld = fix(pld)
    print(f_pld)
    print(base64.urlsafe_b64decode(f_pld))
    print(base64.urlsafe_b64decode(fix(sig)))



if __name__ == "__main__":
    cesi()