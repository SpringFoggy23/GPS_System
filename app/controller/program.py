from flask import Blueprint,render_template, request,jsonify
from app.models.base import db
from app.models.program import Program

programBP = Blueprint('program',__name__)

@programBP.route('', methods=['GET'])
def get_program():
        with db.auto_commit():
               print(request.method)
               program = Program()
               program.Name = 'MedicalScience'
               program.UniversityName = 'HKU'
               program.GPALow = 3.4
               program.GPAUpper =3.7
               db.session.add(program) 

        return 'hello program'+request.method

@programBP.route('/update_GPA', methods=['GET'])

def change_GPA():
    with db.auto_commit():
        program = Program.query.get('Internet')
        program.GPALow = '2.3'
        program.GPAUpper='4.0'

    #return 'Change has done'+request.method
    return render_template('change.html',title='Successfully change Login')















# def updateGPA():
#         if request.method =='GET':
#            return render_template('program.html',title='Sample Program',header='Sample Case')
#         else:
          
#           Name=request.form.get['program-name']
#           GPALow=request.form.get['GPALower']
#           GPAUpper=request.form.get['GPAUpper']
#           print(Name,GPALow,GPAUpper)
#           #return render_template('Change.html',title='Change Done')
#           pro=Program.query.filter_by(Program.Name==Name).first()
#         #   if pro in program:
#         #         print(pro.jsonstr())
#         #   else:
#         #         return"invalid program"
          
#           if pro:
#                 #return render_template('Change.html',title='Change Done')
#                 result=Program.update(Program.Name,Program.GPALow, Program.GPAUpper)
#                 if result == 0:
#                         return render_template('Change.html',title='Change Done')
#                 elif result == 1:
#                         return jsonify({'msg': 'The value of GPA out of range'})
#                 elif result==2:
#                         return jsonify({'msg': 'GPALower should be less than GPAUpper'})
#                         # 返回JSON响应
#           else:
#              return render_template('program.html',title='Sample Program',header='Sample Case')




# @programBP.route('', methods=['PUT'])
# def update_program():
#     program = Program.query.get(program.Name = 'MedicalScience')
#     if not program:
#         return jsonify({'error': 'program not found'}), 404
#     gpa_lower = request.json.get('gpa_lower')
#     gpa_upper = request.json.get('gpa_upper')
#     if gpa_lower:
#         program.gpa_lower = gpa_lower
#     if gpa_upper:
#         program.gpa_upper = gpa_upper
#     db.session.commit()
#     return jsonify({'success': True})