from flask import Flask, render_template, request
import math
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = "qa12qa"

@app.route("/")
@app.route("/home")
def home():
    return render_template('homepage.html')

@app.route("/Prime_factorization", methods=["GET", "POST"])
def Prime_factorization():

    errorlabel = ''
    output = ''
    output_list = []

    if request.method.upper() == "POST":
        inputed_number = request.form.get("i_number")

        if inputed_number=='' or inputed_number == None:
            errorlabel = "Please enter an integer!"

        else:
            n = int(inputed_number)

            if n==1:
                output_list.append("1")

            else: 
                while n % 2 == 0:
                    output_list.append("2")
                    n = n / 2
                    
                for i in range(3,int(math.sqrt(n))+1,2):            
                    while n % i== 0:
                        b = str(i)
                        output_list.append(b)
                        n = n / i
                        
                if n > 2:
                    a = str(n)
                    output_list.append(a)

    if len(output_list)==0:
        output = ''
    elif output_list == ["1"]:
        output = "1 which is neither prime nor composite"
    elif output_list != ["1"] and len(output_list) == 1:
        s = " ".join(str(e) for e in output_list)
        output = f"{s} which is prime"
    else:
        output = "*".join(output_list)

    return render_template('p_factorization.html', errorlabel = errorlabel, output = output)

@app.route("/Totient_Function_Computation", methods=["GET", "POST"])
def Totient_Function_Computation():

    def gcd(p,q):
        while q != 0:
            p, q = q, p%q
        return p

    def is_coprime(x, y):
        return gcd(x, y) == 1

    def phi_func(k):
        if k == 1:
            return 1
        else:
            n = [y for y in range(1,k) if is_coprime(k,y)]
            return len(n)

    errorlabel = ''
    output = ''

    if request.method.upper() == "POST":
        inputed_number = request.form.get("tf_number")

        if inputed_number=='' or inputed_number == None:
            errorlabel = "Please enter an integer!"

        else:
            n = int(inputed_number)
            output = str(phi_func(n))

    return render_template('Totient_fc.html', output = output, errorlabel = errorlabel)

@app.route("/Miller_Rabin_Algorithm",methods=["GET", "POST"])
def Miller_Rabin_Algorithm():
    def power(x, y, p):
        res = 1

        x = x % p
        while (y > 0):

            if (y & 1):
                res = (res * x) % p
            y = y>>1; 
            x = (x * x) % p
        
        return res;

    def miillerTest(d, n):
        a = 2 + random.randint(1, n - 4)
        x = power(a, d, n)

        if (x == 1 or x == n - 1):
            return True

        while (d != n - 1):
            x = (x * x) % n
            d *= 2

            if (x == 1):
                return False
            if (x == n - 1):
                return True
        return False

    def isPrime( n, k):     
        # Corner cases
        if (n <= 1 or n == 4):
            return False
        if (n <= 3):
            return True
    
        # Find r such that n =
        # 2^d * r + 1 for some r >= 1
        d = n - 1
        while (d % 2 == 0):
            d //= 2
    
        # Iterate given number of 'k' times
        for i in range(k):
            if (miillerTest(d, n) == False):
                return False
        return True

    errorlabel = ''
    output = ''

    if request.method.upper() == "POST":
        inputed_number = request.form.get("m_number")
        if inputed_number=='' or inputed_number == None:
            errorlabel = "Please enter an integer!"
        else:   
            n = int(inputed_number)
            k = 10
            if isPrime(n, k):
                output = "The inputed number is prime according to miller-rabin algorithm"
            else:
                output = "The inputed number is composite according to miller-rabin algorithm"

    return render_template('MRA.html', output = output, errorlabel = errorlabel)

@app.route("/Fast_Exponentiation",methods=["GET", "POST"])
def Fast_Exponentiation():
  
    def fe(x,e,m):
        X = x
        E = e
        Y = 1
        while E > 0:
            if E % 2 == 0:
                X = (X * X) % m
                E = E/2
            else:
                Y = (X * Y) % m
                E = E - 1
        return Y

    errorlabel = ''
    output = ''

    if request.method.upper() == "POST":
        a = request.form.get("f_number")
        b = request.form.get("f_number2")
        c = request.form.get("f_number3")

        if a=='' or a == None or b=='' or b == None or c=='' or c == None:
            errorlabel = "Missing Information!"
        else:
            A = int(a)
            B = int(b)
            C = int(c)

            resultt = fe(A,B,C)

            result = f"{A} ^ {B} mod({C}) = {resultt}"

            output = str(result)

    return render_template('Fast_exponentiation.html', errorlabel = errorlabel, output = output)

@app.route("/Chinese_Remainder_Theorem",methods=["GET", "POST"])
def Chinese_Remainder_Theorem():

    def inv(a, m) :
     
        m0 = m
        x0 = 0
        x1 = 1
    
        if (m == 1) :
            return 0
    
        while (a > 1) :
            q = a // m
    
            t = m
    
            m = a % m
            a = t
    
            t = x0
    
            x0 = x1 - q * x0
    
            x1 = t
        
        if (x1 < 0) :
            x1 = x1 + m0
    
        return x1
 
    def findMinX(num, rem, k) :
        
        prod = 1
        for i in range(0, k) :
            prod = prod * num[i]
    
        result = 0
    
        for i in range(0,k):
            pp = prod // num[i]
            result = result + rem[i] * inv(pp, num[i]) * pp
        
        return result % prod

    errorlabel = ''
    output = ''

    if request.method.upper() == "POST":
        m = request.form.get("crt_number")
        a = request.form.get("crt_number2")

        if a=='' or a == None or m=='' or m == None:
            errorlabel = "Missing Information!"
        else:
            try:
                mlist = m.split(",")
                alist = a.split(",")

                if len(mlist) != len(alist):
                    errorlabel = "please enter the same amount of numbers"

                for i in range(len(mlist)):
                    mlist[i] = int(mlist[i])
                    alist[i] = int(alist[i])

                k = len(mlist)
                result = findMinX(mlist, alist, k)
                output = f"A = {result}"
            except Exception as e:
                output = e.args
            
    return render_template('CRT.html', errorlabel = errorlabel, output = output)

if __name__ == '__main__':
    app.run(debug=True)
