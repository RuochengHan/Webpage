from flask import render_template, request
from app import app
import os
import sys
sys.path.insert(1, '/scratch/ruhan/web/microblog/app/kernels')
from qc_calcu import qc_psi4

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/test')
def test():
  posts = [
    { 'author': {'username': 'ruocheng'},
      'body': 'hello, qqq',
    },
    { 'author': {'username': 'qianqian'},
      'body': 'hello, ccc',
    }
  ]
  return render_template('test.html', posts=posts)

@app.route('/calculator', methods=['GET'])
def calculator():
  return render_template('calculator.html')

@app.route('/calculator_result', methods=['POST'])
def calculator_result():
  """Route where we send calculator form input"""

  error = None
  result = None

  # request.form looks for:
  # html tags with matching "name= "
  first_input = request.form['Input1']  
  second_input = request.form['Input2']
  operation = request.form['operation']

  try:
    input1 = float(first_input)
    input2 = float(second_input)

    # On default, the operation on webpage is addition
    if operation == "+":
        result = input1 + input2

    elif operation == "-":
      result = input1 - input2

    elif operation == "/":
      result = input1 / input2 

    elif operation == "*":
      result = input1 * input2
    else:
      operation = "%"
      result = input1 % input2

    return render_template(
      'calculator.html',
      input1=input1,
      input2=input2,
      operation=operation,
      result=result,
      calculation_success=True
    )
        
  except ZeroDivisionError:
    return render_template(
      'calculator.html',
      input1=input1,
      input2=input2,
      operation=operation,
      result="Bad Input",
      calculation_success=False,
      error="You cannot divide by zero"
    )
        
  except ValueError:
    return render_template(
      'calculator.html',
      input1=first_input,
      input2=second_input,
      operation=operation,
      result="Bad Input",
      calculation_success=False,
      error="Cannot perform numeric operations with provided input"
    )


@app.route('/qc', methods=['GET'])
def qc():
  return render_template('qc.html')

@app.route('/qc_result', methods=['POST'])
def qc_result():
  atom1 = request.form['Atom1']  
  atom2 = request.form['Atom2']
  distance = request.form['distance']
  method = request.form['method']
  basis = request.form['basis']
  charge = request.form['charge']
  spin = request.form['spin']
  cores = request.form['cores']
  mem = request.form['mem']

  print(cores)
  print(mem)

  atom_list = ['H','He','Li','Be','B','C','N','O','F','Ne']
  tmp = [x.lower() for x in atom_list]
  atom_list.extend(tmp)

  if (atom1 not in atom_list) or (atom2 not in atom_list):
    return render_template('qc.html', success=False, error='Atom type not supported')

  elif not isfloat(distance):
    return render_template('qc.html', success=False, error='Distance input error')

  elif abs(float(distance)) > 8.0:
    return render_template('qc.html', success=False, error='Distance cannot be larger than 8.0 A')
    
  else:
    os.chdir('/scratch/ruhan/web/microblog/qc_tmp/')
    try:
      energy = qc_psi4(atom1, atom2, distance, charge, spin, method, basis, cores, mem)
      return render_template('qc.html', success=True, isresult=True, atom1=atom1, atom2=atom2, distance=distance, result=energy, charge=charge, spin=spin, method=method, basis=basis)

    except:
      return render_template('qc.html', success=True, isresult=False, error='Unknown failure')

@app.route('/qc_log', methods=['POST'])
def qc_log():
  with open("/scratch/ruhan/web/microblog/qc_tmp/output.dat", "r") as f:
    logs = f.readlines()
  return render_template('log.html', logs=logs)


if __name__ == "__main__":
  #app.run(ssl_context='adhoc')
  app.run()

