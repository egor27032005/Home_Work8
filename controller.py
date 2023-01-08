import model
import view
import for_teach

def button_clink():
    status=view.get_value()
    sername=view.get_value2()
    model.init(status,sername)
    if status=="teacher":
        result=model.teach_sear()
        for_teach.for_lesson(result)
    elif status=='student':
        objet=view.get_value3()
        model.init2(objet)
        result2=model.less_sear()
        view.view_data2(result2)