from flask import Flask, render_template,request
import pickle
# render_template is a method called from Flask package

#create object here app is object
app = Flask(__name__)


with open('churnran_svm.pkl', 'rb')as f:
    model = pickle.load(f)



# creating route to define API / endpoint
@app.route('/')  # by default GET http methods is taken here
def index():
    return render_template('index.html') #specify which page need to be displayed


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST','GET'])
def result():
    fixed_acidity=request.form.get('Fixed_Acidity')
    volatile_acidity=request.form.get('Volatile_Acidity')
    citric_acid=request.form.get('Citric_Acid')
    residual_sugar=request.form.get('residual_sugar')
    free_sulphur_dioxide=request.form.get('free_sulphur_dioxide')
    total_sulphur_dioxide=request.form.get('total_sulphur_dioxide')
    density=request.form.get('density')
    pH=request.form.get('pH')
    sulphate=request.form.get('sulphate')
    alcohol=request.form.get('alcohol')

    input=[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,free_sulphur_dioxide,total_sulphur_dioxide,density,pH,sulphate,alcohol]

    predict=model.predict([input])[0]
    print(predict)
    if predict == [0]:
        result="bad quality"
    else:
        result="good quality"

    return render_template('result.html',res=result)
    


    





if __name__ == '__main__':
    app.run(debug=True)

